import atexit
import base64
import datetime as dt
import glob
import hashlib
import json
import logging
import mmap
import os
import os.path
import subprocess
import sys
import tempfile
import time
import urllib.parse
import uuid
import tarfile

from http import HTTPStatus
from pathlib import Path
from time import gmtime
from time import strftime
from traceback import format_exception
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

import click
import coloredlogs
import halo
import pandas as pd
import paramiko
import questionary
import requests
import tabulate
import yaml
from dateutil import parser
from git import Repo
from inquirer.themes import GreenPassion, term
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
from tinynetrc import Netrc

logger = logging.getLogger("elbo.client")
coloredlogs.install(level='DEBUG',
                    logger=logger,
                    fmt='%(name)s %(message)s'
                    )

__version__ = "0.3"


# noinspection PyMethodMayBeStatic
class ElboConnector:
    #
    # Server endpoints
    #
    UPLOAD_URL_ENDPOINT = "upload_url"
    SCHEDULE_ENDPOINT = "schedule"
    PROVISION_ENDPOINT = "provision"
    CREATE_ENDPOINT = "create"
    LOGS_ENDPOINT = "logs"
    RESOURCE_ENDPOINT = "resource"
    DASHBOARD_ENDPOINT = "dashboard"
    SIGNUP_ENDPOINT = "signup"
    STATUS_ENDPOINT = "status"
    TASKS_ENDPOINT = "tasks"
    SHOW_ENDPOINT = "show"
    BALANCE_ENDPOINT = "balance"
    REMOVE_ENDPOINT = "rm"
    CANCEL_ENDPOINT = "cancel"
    EXCEPTION_REPORT_ENDPOINT = "exception_report"
    WANDB_DIRECTORY = "wandb"
    WORKSPACE_DIRECTORY = "workspace"
    OBJECT_INFO = "object_info"

    ELBO_TOKEN_FILE = os.path.expanduser("~/.elbo/token")
    ELBO_CACHE_DIR = os.path.expanduser("~/.elbo/cache")

    # TODO: Add back SSL in Cloud fare after fixing HTTP error 524 -- Long polling
    # noinspection HttpUrlsUsage
    ELBO_HOST = "http://prod.elbo.ai"
    ELBO_STAGING_HOST = "https://rbm.elbo.ai"
    ELBO_TEST_HOST = "http://localhost:5007"

    def __init__(self):
        self._host_name = ElboConnector.get_elbo_host()

    @staticmethod
    def get_elbo_host():
        if os.getenv('ELBO_TEST_MODE') is not None:
            return ElboConnector.ELBO_TEST_HOST
        elif os.getenv('ELBO_STAGING_MODE') is not None:
            return ElboConnector.ELBO_STAGING_HOST
        else:
            return ElboConnector.ELBO_HOST

    def get_auth_token(self):
        """
        Get the ELBO service authentication tokens using NETRC
        :return: The auth tokens
        """
        netrc = None
        try:
            netrc = Netrc()
        except FileNotFoundError as _:
            logger.error(f"could not find ~/.netrc file where auth tokens are stored. Please run `elbo login` again.")
            exit(-1)
        host_name = self._host_name
        tokens = netrc.get(host_name)
        if tokens['password'] is None:
            logger.error(f"please login to elbo service by running `elbo login`")
            exit(0)
        else:
            return tokens['password']

    def request(self, end_point, params=None, host=None, method='GET'):
        """
        Call the rest API get
        """
        if not host:
            host = self._host_name
        url = host + "/" + end_point
        token = self.get_auth_token()
        headers = {
            # Flask does not like `_` in header keys
            'TOKEN': token
        }

        try:
            # Keep a high timeout
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=10 * 60)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=params, timeout=10 * 60)
            else:
                logger.error(f"{method} not found for submission of request")
                response = None
                exit(-1)

        except requests.exceptions.ConnectionError as _:
            logger.error(f"unable to connect to ELBO Server, please try again...")
            return None
        except requests.exceptions.ReadTimeout as _:
            logger.error(f"timed out while trying to connect to the node. Usually the node starts execution, please"
                         f" check status using `elbo show`")
            return None

        if response.ok:
            response_json = response.text
            response_code = response.status_code
            if response_code == HTTPStatus.NOT_MODIFIED:
                logger.warning(f"task already cancelled or completed.")
                exit(0)
            response = json.loads(response_json)
        else:
            if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
                logger.error(f"🚨 {response.text}")
            elif response.status_code == HTTPStatus.UNAUTHORIZED:
                logger.error(f"🚨 we are not able to authorize you, could you try `elbo login` again?")
                exit(-1)
            elif response.status_code == HTTPStatus.NOT_FOUND:
                logger.error(f"🚨 got resource not found error")
            elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
                print("")
                logger.error(f"🚨 we hit a glitch --> {response.text}")
                logger.error(f"Please email contact@elbo.ai")
            else:
                logger.error(f"received unknown error code - {response.status_code} with message - {response.text}")
            response = None

        return response


__elbo_connector = ElboConnector()


def read_config(config_file):
    """
    Read the config file and verify that is valid and has all the requirements parameters
    :param config_file: The input config file
    :return: Python dictionary of YAML
    """
    with open(config_file) as fd:
        task_config = yaml.load(fd, Loader=yaml.FullLoader)

    keys = task_config.keys()

    valid_config = True
    if 'task_dir' not in keys:
        logger.error(f"needs 'task_dir' to be specified in '{config_file}'. This is the directory "
                     f"where your source code is present.")
        valid_config = False

    if 'run' not in keys:
        logger.error(f"needs 'run' to be specified in '{config_file}'. This is the command that should be "
                     f"run to start the task.")
        valid_config = False

    if 'artifacts' not in keys:
        logger.error(
            f"needs 'artifacts to be specified in '{config_file}'. This directory would be tar-balled and saved "
            f"as output for your task.")
        valid_config = False

    if not valid_config:
        return None

    return task_config


def get_upload_url():
    """
    Get the upload URL for the token
    """
    response = __elbo_connector.request(ElboConnector.UPLOAD_URL_ENDPOINT)
    if response is None:
        return None

    upload_url = response.get('uploadUrl')
    user_id = response.get('user_id')
    authorization_token = response.get('authorizationToken')
    session_id = response.get('session_id')
    show_low_balance_alert = response.get('add_low_balance_alert')
    user_first_name = response.get('user_first_name')
    return upload_url, user_id, authorization_token, session_id, show_low_balance_alert, user_first_name


def get_task_id_from_file_name(file_name):
    """
    Get the task id from the file name
    :param file_name: The file name
    :return: The task id
    """
    try:
        task_id = file_name.split('-')[2].split('.')[0]
    except IndexError as _:
        task_id = None

    return task_id


def download_file(download_url, download_directory, authorization=None, file_name=None):
    """
    TODO: This is copied over from common/utils in elbo-server Repo. Need to expose this in a common
    package

    Download the file at URL to the download directory. This stores the file in memory and writes to file system.
    This can be used for really large files which may not fit in memory.

    :param file_name:
    :param authorization: The download authorization token
    :param download_url: The download URL
    :param download_directory: The download directory
    :return: Path to file if download is successful, None otherwise
    """
    if not download_url:
        logger.error(f"No download URL")
        return

    if file_name is None:
        file_name = download_url.split('/')[-1]
        if file_name is None:
            logger.error(f"Could not infer filename from {download_url}")
            return None
    local_filename = os.path.join(download_directory, file_name)
    headers = {}
    if authorization is not None:
        headers = {
            'Authorization': authorization
        }

    try:
        with requests.get(download_url, stream=True, headers=headers) as r:
            r.raise_for_status()
            total_size_in_bytes = int(r.headers.get('content-length', 0))
            chunk_size = 8192
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        progress_bar.update(len(chunk))
            progress_bar.close()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == HTTPStatus.NOT_FOUND:
            logger.warning(f"{download_url} file does not exists.")
            logger.warning(f"Perhaps the task is not complete yet?")
        else:
            logger.error(f"Unable to request {download_url} exception - {e}")
        return None

    if os.path.exists(local_filename):
        return local_filename
    else:
        return None


def upload_file(file_path, upload_url, user_id, authorization_token, bucket_key=None):
    """
    Upload a file to the URL specified
    :param file_path: The file to upload
    :param upload_url: The upload URL
    :param user_id: The user id
    :param authorization_token: The auth token
    :param bucket_key: The user bucket key
    :return: The bucket key and the SHA256 hash of the uploaded file
    """
    content_type = "application/tar+gzip"
    with open(file_path, mode='rb') as fd:  # b is important -> binary
        file_contents = fd.read()

    file_hash = hashlib.sha1(file_contents).hexdigest()
    file_name = os.path.basename(file_path)
    if bucket_key is None:
        bucket_key = os.path.join(user_id, file_name)
    headers = {
        'Authorization': authorization_token,
        'X-Bz-File-Name': bucket_key,
        'Content-Type': content_type,
        'X-Bz-Content-Sha1': file_hash,
        'X-Bz-Info-Author': 'None',
        'X-Bz-Server-Side-Encryption': 'AES256'
    }

    file_size = os.stat(file_path).st_size
    with open(file_path, "rb") as f:
        # TODO: Use memory mapped to reduce memory usage while uploading
        with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            wrapped_file = CallbackIOWrapper(t.update, f, "read")
            count = 0
            while True:
                try:
                    if count == 5:
                        logger.error(f"too many connection errors...")
                        break
                    upload_response = requests.post(upload_url, headers=headers, data=wrapped_file)
                    break
                except ConnectionResetError as _:
                    # This can happen if we are uploading large files, wait for some time...
                    count = count + 1
                    logger.warning(f"Connection error, retrying ...")
                    time.sleep(10)

    if upload_response.status_code == 200:
        task_id = get_task_id_from_file_name(file_name)
    else:
        logger.error(f"failed task upload, response: {upload_response}")
        return None

    return bucket_key, file_hash, task_id


def request_task_run(bucket_key, file_hash, task_config, session_id):
    """
    Request the receiver to run the task.

    :param bucket_key: The bucket key - The file path in the Bucket
    :param file_hash: The file hash. The receiver will check if the file hash on the Bucket is the same as specified
    :param task_config: The task config provided by the user in the YAML file
    :param session_id: The session id
    here.
    :return: None
    """
    params = {
        'session_id': session_id,
        'bucket_key': bucket_key,
        'file_hash': file_hash,
        'task_config': base64.b64encode(bytes(json.dumps(task_config), 'utf-8'))
    }

    response = __elbo_connector.request(ElboConnector.SCHEDULE_ENDPOINT, params=params)
    return response


def request_machine_create():
    """
    Request the receiver to run the task.
    :return: None
    """
    params = {}
    response = __elbo_connector.request(ElboConnector.CREATE_ENDPOINT, params=params)
    return response


def provision_machine_create_compute(compute_type, session_id, open_ports):
    """
    Request to provision the chosen to compute type.
    """
    params = {
        'chosen_compute_type': base64.b64encode(bytes(json.dumps(compute_type), 'utf-8')),
        'session_id': session_id,
        'open_ports': open_ports
    }

    response = __elbo_connector.request(ElboConnector.CREATE_ENDPOINT, params=params)
    return response


def provision_compute(compute_type, session_id, task_config, config_file_path):
    """
    Request to provision the chosen to compute type.

    :param task_config: The task config
    :param config_file_path: The config file path
    :param compute_type: To compute type
    :param session_id The session id
    :return:
    """
    params = {
        'chosen_compute_type': base64.b64encode(bytes(json.dumps(compute_type), 'utf-8')),
        'session_id': session_id,
        'config_file_path': config_file_path,
        'task_config': base64.b64encode(bytes(json.dumps(task_config), 'utf-8'))
    }

    response = __elbo_connector.request(ElboConnector.PROVISION_ENDPOINT, params=params)
    return response


class ElboTheme(GreenPassion):
    def __init__(self):
        super().__init__()
        self.Question.mark_color = term.yellow
        self.Question.brackets_color = term.pink
        self.Question.default_color = term.yellow
        self.Checkbox.selection_color = term.bold_black_on_pink
        self.Checkbox.selection_icon = "❯"
        self.Checkbox.selected_icon = "◉"
        self.Checkbox.selected_color = term.pink
        self.Checkbox.unselected_color = term.normal
        self.Checkbox.unselected_icon = "◯"
        self.List.selection_color = term.bold_black_on_pink
        self.List.selection_cursor = "❯"
        self.List.unselected_color = term.normal


def prompt_user(compute_options):
    """
    Prompt the user with compute options and get the selection
    :param compute_options: The list of compute options
    :return: The selected option
    """
    options = []
    mapping = {}

    def get_sorting_key(x):
        x_parsed = json.loads(x[1])
        return x_parsed['cost']

    compute_options = dict(sorted(compute_options.items(), key=lambda x: get_sorting_key(x)))
    for k, v in compute_options.items():
        v = json.loads(v)
        if v.get('spot') is True:
            suffix = "(spot)"
        else:
            suffix = ""
        k = k.replace(" (spot)", "")
        provider = v['provider']

        if "linode" in provider.lower():
            provider = f"{provider} (~ 9 mins to provision) (billed hourly)"
        option = f" ${v['cost']:7.4f}/hour {k:>26} {v['num_cpu']:>3} cpu {v['mem']:>5}Gb mem " \
                 f"{v['gpu_mem']:>4}Gb gpu-mem {provider} {suffix}"
        options.append(option)
        mapping[option] = v

    if len(options) > 1:
        logger.info(f"number of compute choices - {len(options)}")
        chosen = questionary.select("Please choose:",
                                    choices=options,
                                    ).ask()
        if chosen is None:
            logger.warning(f"None selected, exiting.")
            exit(0)
            return None
        chosen_compute_type = mapping[chosen]
    elif len(options) == 0:
        logger.error(
            f"was unable to find compute options at the moment. Please email support@elbo.ai if this continues.")
        return None
    else:
        chosen_compute_type = list(mapping.values())[0]

    return chosen_compute_type


@click.group()
def cli():
    """elbo.ai - Train more, pay less
    """
    pass


@cli.command(name='login')
@click.option('--token',
              prompt='Please enter or paste your token from https://elbo.ai/welcome',
              hide_input=True)
def login(token):
    """
    Login to the ELBO service.
    """
    net_rc_file = os.path.join(os.path.expanduser('~'), '.netrc')
    if not os.path.exists(net_rc_file):
        # Create file if it doesn't exist
        logger.info(f"Creating {net_rc_file}")
        Path(net_rc_file).touch()
    netrc = Netrc()
    host_name = ElboConnector.get_elbo_host()
    netrc[host_name]['password'] = token
    netrc.save()

    logger.info(f"ELBO token saved to ~/.netrc")


@cli.command(name='status')
def status():
    """
    Get ELBO server status.
    """
    member_status = "❌"
    db_status = "❌"
    server_status = "❌"

    response = __elbo_connector.request(ElboConnector.STATUS_ENDPOINT)
    if response is not None:
        db_status = '✅' if response.get('db') is True else db_status
        member_status = '✅' if response.get('membership') is True else db_status
        server_status = '✅' if response.get('server') is True else db_status

    logger.info(f"Membership: {member_status}")
    logger.info(f"Database  : {db_status}")
    logger.info(f"Server    : {server_status}")


@cli.command(name='ps')
@click.option('-r', '--running', help='Show only running tasks', flag_value='Running')
@click.option('-c', '--completed', help='Show only completed tasks', flag_value='Completed')
def ps(running, completed):
    """
    Show list of all tasks.
    """
    if running:
        logger.info(f"looking up running tasks ...")
    else:
        logger.info(f"looking up your tasks ...")
    response = __elbo_connector.request(ElboConnector.TASKS_ENDPOINT)
    if response is None:
        logger.error(f"is unable to get tasks list")
        return

    tasks_list = response['records']
    if len(tasks_list) == 0:
        logger.info(f"no tasks found, how about starting an instance with `elbo create` ?")
        return

    df = pd.DataFrame(tasks_list)
    df = df.fillna('')
    if 'Artifacts URL' in df:
        del df['Artifacts URL']
    if 'Logs URL' in df:
        del df['Logs URL']
    if 'SSH' in df:
        del df['SSH']
    if 'Source URL' in df:
        del df['Source URL']
    if 'last' in df:
        del df['last']

    time_columns = [
        'Run Time',
        'Start Time',
        'Submission Time',
        'Completion Time',
        'Billed Upto Time',
        'Created Time'
    ]

    for column in time_columns:
        if column in df.columns:
            # Format time to local time zone
            df[column] = df[column].apply(transform_date())

    df = df.sort_values(by=['Task ID'])
    df = df.set_index('Task ID')
    if running == "Running":
        df = df.loc[df['Status'] == running]
    elif completed == "Completed":
        df = df.loc[df['Status'] == completed]
    if len(df) == 0:
        logger.info(f"no running tasks...")
    else:
        print(tabulate.tabulate(df, headers="keys", tablefmt="pretty"))

    if len(df) > 0:
        print("")
        print("")
        print(f"Related task commands: \n")
        print("\telbo show [task_id]")
        print("\telbo kill [task_id]")
        print("\telbo ssh [task_id]")
        print("\telbo download [task_id]\n")


@cli.command(name='kill')
@click.argument('task_id')
def cancel(task_id):
    """
    Stop the task.
    """
    logger.info(f"Stopping task - {task_id}")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.CANCEL_ENDPOINT,
                                        params=params)
    if response is not None:
        logger.info(f"Task with id = {task_id} is marked for cancellation.")


@cli.command(name='show')
@click.argument('task_id')
def show(task_id):
    """
    Show the task.
    """
    logger.info(f"Fetching task - {task_id}")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.SHOW_ENDPOINT,
                                        params=params)
    if response is not None:
        logger.info(f"Task with id = {task_id}:")
        record = response['records']
        is_running = record['Status'].lower() == "running"
        for k, v in response['records'].items():
            # TODO: Present these fields in a better way
            if "Authorization" in k:
                continue
            if k == "SSH":
                if not is_running:
                    continue
            if 'Run Time' in k:
                v = format_time(v)
            elif 'Time' in k:
                v = format_date(v)
            if 'URL' not in k and k != 'last':
                print(f"{k:<24}: {v}")


@cli.command(name='balance')
def balance():
    """
    Show the users balance
    """
    response = __elbo_connector.request(ElboConnector.BALANCE_ENDPOINT,
                                        params={})
    if response is not None:
        account_balance = response['Balance']
        deposit_url = response['URL']
        logger.info(f"Your account balance is ${account_balance}. Deposit funds using {deposit_url}.")


# TODO: Today this command does not do anything, exclude it until we figure out how to handle
# stale jobs
def rm(task_id):
    """
    Permanently delete the task.
    """
    logger.info(f"Removing task - {task_id}")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.REMOVE_ENDPOINT,
                                        params=params)
    if response is not None:
        logger.info(f"Task with id={task_id} is marked for removal.")


@cli.command(name='download')
@click.argument('task_id')
def download(task_id):
    """
    Download the artifacts for the task.
    """
    logger.info(f"downloading artifacts for task - {task_id}")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.RESOURCE_ENDPOINT,
                                        params=params)
    if response is None:
        logger.info(f"Could not retrieve artifact download URL for {task_id}")
        return

    artifact_auth = response['client_artifact_auth']
    artifact_url = urllib.parse.unquote(response['client_url'])
    temp_dir = tempfile.mkdtemp()
    local_dir_name = download_task_artifacts(artifact_url, temp_dir, artifact_auth, None)
    if local_dir_name is not None and os.path.exists(local_dir_name):
        logger.info(f"artifacts downloaded to temporary directory: {local_dir_name}")


@cli.command(name='ssh')
@click.argument('task_id')
def ssh_task(task_id):
    """
    SSH into the machine running the task.
    """
    logger.info(f"Trying to SSH into task - {task_id}...")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.SHOW_ENDPOINT,
                                        params=params)

    if response is not None and response['records'] is not None:
        ssh_command = response['records']['SSH']
        password = response['records']['Password']
        logger.info(f"Running Command : {ssh_command}")
        logger.info(f"Enter this password when prompted: {password}")
        os.system(ssh_command)
    else:
        logger.warning(f"SSH information not found for task - {task_id}, is it still running?")


# TODO: Enable once we get this working
# @cli.command(name='logs')
# @click.option('--task_id',
#              required=True,
#              hide_input=False)
def logs(task_id):
    """
    Show logs from the task.
    """
    # TODO:
    logger.info(f"Getting logs of - {task_id}...")
    params = {
        'task_id': task_id
    }
    response = __elbo_connector.request(ElboConnector.LOGS_ENDPOINT,
                                        params=params)
    if response is not None:
        logger.info(response)


def get_real_time_logs(server_ip):
    # noinspection HttpUrlsUsage
    log_address = f"http://{server_ip}/stream"
    connection_errors = 0
    while True:
        try:
            request = requests.get(log_address, stream=True)
            if request.encoding is None:
                request.encoding = 'utf-8'

            for line in request.iter_lines(decode_unicode=True):
                if line and line != "0":
                    logger.info(f"{server_ip}> {line}")
            time.sleep(2)
        except requests.exceptions.ConnectionError as _:
            # Connection errors can happen when SSH is trying to get established
            print('.', end='')
            time.sleep(5)
            connection_errors = connection_errors + 1
            if connection_errors > 10:
                print("*")
                break
            pass
        except Exception as _e:
            logger.error(f"Hit {_e}")
            break


def extract_file(local_file_name):
    os.makedirs(ElboConnector.ELBO_CACHE_DIR, exist_ok=True)
    temp_dir = tempfile.mkdtemp()
    if local_file_name.endswith("tar.gz") or local_file_name.endswith(".tgz"):
        tar = tarfile.open(local_file_name, "r:gz")
        tar.extractall(temp_dir)
        tar.close()
    elif local_file_name.endswith("tar"):
        tar = tarfile.open(local_file_name, "r:")
        tar.extractall(temp_dir)
        tar.close()
    return temp_dir


def download_task_artifacts(artifact_url, output_directory, artifact_auth, artifact_file):
    local_file_name = download_file(artifact_url, output_directory, artifact_auth, artifact_file)
    extracted_dir = extract_file(local_file_name)

    # Check if WandB directory exists, if it does, try to sync WandB
    workspace_dir = os.path.join(extracted_dir, ElboConnector.WORKSPACE_DIRECTORY)
    files = os.listdir(workspace_dir)
    if ElboConnector.WANDB_DIRECTORY in files:
        sync_wandb = questionary.confirm("detected weights and biases offline data, "
                                         "do you want to sync them to wandb.ai?",
                                         qmark="elbo.client").ask()
        if sync_wandb:
            current_dir = os.getcwd()
            os.chdir(extracted_dir)
            fix_symlinks_command = f'find {extracted_dir}  -lname "*" -exec sh -c \'ln -snf ' \
                                   f'"{extracted_dir}/$(readlink "$1")" "$1"\' sh ' + '\\{\\} \\;'
            os.system(fix_symlinks_command)
            wandb_offline_dir = os.path.join(workspace_dir, "wandb/offline-run-*")
            wandb_command = f"wandb sync --include-offline {wandb_offline_dir}"
            os.system(wandb_command)
            os.chdir(current_dir)

    return extracted_dir


# noinspection HttpUrlsUsage
def process_compute_provisioned_response(response_json, ssh_only=False):
    """
    Process the response from the server for provisioned compute
    :param ssh_only: Is this task SSH only?
    :param response_json: The response json
    :return: None
    """
    response = response_json
    server_ip = response['ip']
    task_id = response['task_id']
    password = response['password']

    logger.info(f"compute node ip {server_ip}")
    #
    # TODO: Could we route the traffic through CloudFare so we get https endpoint?
    # One problem may be the use of port 2222 for SSH which will not work if we proxy through CloudFare
    #
    if not ssh_only:
        logger.info(f"task with ID {task_id} is submitted successfully.")
        logger.info("----------------------------------------------")
        logger.info(f"ssh using - ssh root@{response['ip']} -p 2222")
        logger.info(f"scp using - scp root@{response['ip']} -p 2222")
        logger.info(f"password: {password}")
        logger.info("----------------------------------------------")
        print("")
        logger.info(f"here are URLS for task logs ...")
        logger.info(f"setup logs        - http://{server_ip}/setup")
        logger.info(f"requirements logs - http://{server_ip}/requirements")
        logger.info(f"task logs         - http://{server_ip}/task")
        print("")
        logger.info(f"TIP: 💡 see task details with command: `elbo show {task_id}`")
        print("")
        logger.info(f"⏳ It may take a minute or two for the node to be reachable.")
    else:
        logger.info("----------------------------------------------")
        logger.info(f"ssh using - ssh root@{response['ip']} -p 2222")
        logger.info(f"scp using - scp root@{response['ip']} -p 2222")
        logger.info(f"password: {password}")
        logger.info("----------------------------------------------")
        print("")
        logger.info(f"TIP: 💡 copy your SSH public key to the server for password less login using:")
        logger.info(f"ssh-copy-id -p 2222 root@{response['ip']}")
        print("")
        logger.info(f"TIP: 💡 cancel task using command: `elbo kill {task_id}`")
        print("")
        logger.info(f"⏳ It may take a minute or two for the node to be reachable.")

    return server_ip, password


def say_hello(user_first_name=None):
    # TODO: Add fortune? Random greetings?
    if user_first_name is None:
        logger.info(f"Hey there 👋")
    else:
        logger.info(f"Hey {user_first_name} 👋, welcome!")


def cp_file_to_elbo(filename, source_object, destination_dir):
    url_response = get_upload_url()
    if url_response is None:
        logger.error(f"is unable to authenticate with server..")
        exit(-6)

    upload_url, user_id, authorization_token, session_id, show_low_balance_alert, user_first_name = url_response
    if upload_url is not None and user_id is not None and authorization_token is not None:
        rel_path = os.path.relpath(filename, start=source_object)
        if rel_path == ".":
            bucket_key = os.path.join(user_id, destination_dir, os.path.basename(source_object))
        else:
            bucket_key = os.path.join(user_id, destination_dir, os.path.basename(source_object), rel_path)

        if not bucket_key.startswith(user_id):
            logger.error(f"something is wrong with the destination, please email this bug report to hi@elbo.ai")
            exit(0)

        logger.info(f"uploading {filename} -> elbo://{bucket_key} ...")
        _ = upload_file(filename, upload_url, user_id, authorization_token)


def cp_to_elbo(file_path, destination_dir):
    """
    Copy the local file path to elbo storage
    :param file_path: The local file path
    :param destination_dir: The elbo path
    :return:
    """
    if os.path.isabs(file_path):
        source_object = file_path
    else:
        source_object = os.path.join(os.getcwd(), file_path)

    if not os.path.exists(file_path):
        logger.error(f"Unable to find {file_path}, does it exist?")
        return 0

    if destination_dir == "." or destination_dir == "/":
        # User intends to copy to root
        destination_dir = ""

    if os.path.isdir(source_object):
        for filename in glob.iglob(os.path.join(source_object, '**/**'), recursive=True):
            if os.path.isdir(filename):
                continue
            cp_file_to_elbo(filename, source_object, destination_dir)
    else:
        cp_file_to_elbo(file_path, source_object, destination_dir)


@cli.command(name="cp")
@click.argument('file_path')
@click.argument('destination_dir')
def cp(file_path, destination_dir):
    """
    Copy the file at the given path to the destination directory in your ELBO storage. If the give file path is a
    directory, then all files in this directory will be copied recursively.
    """
    if file_path.startswith("elbo://"):
        # Download files
        pass
    else:
        # Upload to elbo
        cp_to_elbo(file_path, destination_dir)


# @cli.command(name="ls")
# @click.argument('path')
def ls(path):
    """
    Show the directory or file information for the given path in object store
    :param path: The object path
    :return:
    """
    if path.startswith("elbo://"):
        path = path.replace("elbo://", "")

    params = {
        'object_name': path
    }
    response = __elbo_connector.request(ElboConnector.OBJECT_INFO,
                                        params=params)
    if response is None:
        logger.warning(f"no information found for {path}")
    else:
        path_info = json.loads(response)
        logger.info(f"path information - {path_info}")


"""
@click.option('--docker-image',
              '-di',
              type=str,
              multiple=False,
              help='The docker image to use for creation.')
"""


@cli.command(name='create')
@click.option('--open-port',
              '-p',
              type=int,
              multiple=True,
              help='The port that should be opened on the instance.')
def create(open_port):
    """
    Create an instance and get SSH access to it.
    """
    if len(open_port) > 0:
        logger.info(f"creating instance with open port(s) - {open_port}")
    else:
        logger.info(f"creating instance ...")

    spinner = halo.Halo(text='elbo.client is finding compute options (this may take a while)',
                        spinner='bouncingBall',
                        placement='left')
    print("")
    spinner.start()
    response = request_machine_create()
    if not response:
        logger.error(f"Unable to get compute type options")
        return

    options = response['results']
    session_id = response['session_id']
    user_first_name = response['user_first_name']
    spinner.stop()
    say_hello(user_first_name)
    ip = None
    password = None
    if options is not None:
        chosen_type = prompt_user(options)
        spinner = halo.Halo(text='elbo.client is provisioning compute (usually takes ~ 4 minutes, ☕️ time!)',
                            spinner='bouncingBall',
                            placement='left')
        spinner.start()
        response_json = provision_machine_create_compute(chosen_type, session_id, open_ports=list(open_port))
        spinner.stop()
        if response_json is not None:
            ip, password = process_compute_provisioned_response(response_json, ssh_only=True)
            client = paramiko.SSHClient()
            wait_for_ssh_ready(client, ip, password)
        else:
            logger.error(f"something went wrong with provisioning, please try again ...")
    else:
        logger.error(f"is unable to get compute options from ELBO servers")

    return ip, password


def wait_for_ssh_ready(client, ip, password):
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    spinner = halo.Halo(text='elbo.client is waiting for node to be ready ...',
                        spinner='bouncingBall',
                        placement='left')
    print("")
    spinner.start()
    while True:
        try:
            client.connect(hostname=ip, username="root", port=2222, password=password)
            spinner.stop()
            break
        except BadHostKeyException as _:
            time.sleep(4)
        except AuthenticationException as _:
            time.sleep(2)
        except SSHException as _:
            time.sleep(4)
        except paramiko.ssh_exception.NoValidConnectionsError as _:
            time.sleep(4)


@cli.command(name='notebook')
def notebook():
    """
    Start a Jupyter Lab session.
    """
    note_book_git_url = "https://github.com/elbo-ai/elbo-examples"
    notebook_token_command = "/opt/conda/bin/jupyter-lab list | grep token | cut -d'=' -f2 | cut -d' ' -f1"
    logger.info(f"creating notebook using config at project {note_book_git_url} ...")
    temp_dir = tempfile.mkdtemp()
    logger.info(f"cloning {note_book_git_url} to {temp_dir} ...")
    Repo.clone_from(note_book_git_url, temp_dir)
    config_file_path = os.path.join(temp_dir, "notebook/elbo.yaml")
    logger.info(f"Submitting notebook run config : {config_file_path}")
    ip, password = run_internal(config_file_path)
    client = paramiko.SSHClient()
    wait_for_ssh_ready(client, ip, password)

    counter = 0
    token = None
    logger.info(f"node started ..")
    spinner = halo.Halo(text='elbo.client is waiting for jupyter notebook to start ...',
                        spinner='bouncingBall',
                        placement='left')
    print("")
    spinner.start()
    while True:
        if counter > 30:
            # 5 minutes
            spinner.stop()
            break
        stdin, stdout, stderr = client.exec_command(notebook_token_command)
        output = stdout.readlines()
        if len(output) > 0:
            token = output[0].rstrip()
            spinner.stop()
            logger.info(f"Notebook URL = http://{ip}:8080/?token={token}")
            break
        counter = counter + 1
        time.sleep(10)

    if token is None:
        logger.warning(f"sorry, unable to find token, please SSH into {ip} port 2222 with password {password}.")
        logger.warning(f"and run command -> {notebook_token_command}")


def run_internal(config):
    if not os.path.exists(config):
        logger.error(f"is unable to find '{config}', is the path correct?")
        exit(-1)

    task_config = read_config(config)
    if task_config is None:
        exit(-2)

    if 'name' in task_config:
        logger.info(f"is starting '{task_config['name']}' submission ...")
    else:
        logger.error(f"please specify a task `name` in {config} file.")
        exit(-3)

    url_response = get_upload_url()
    if url_response is None:
        logger.error(f"is unable to authenticate with server..")
        exit(-6)
    upload_url, user_id, authorization_token, session_id, show_low_balance_alert, user_first_name = url_response
    if user_first_name:
        say_hello(user_first_name)

    if show_low_balance_alert:
        #
        # Allow user to continue scheduling. The job will complete even if balance is low
        #
        logger.warning(f"The balance on your account is too low, please deposit funds 🙏")

    ip = None
    password = None
    if upload_url is not None and user_id is not None and authorization_token is not None:
        temp_file_name = get_temp_file_path(tgz=True)
        # Get directory path relative to config file
        config_directory = os.path.dirname(config)
        task_dir = os.path.join(config_directory, task_config['task_dir'])
        create_tar_gz_archive(temp_file_name, task_dir)
        logger.info(f"is uploading sources from {task_dir}...")
        bucket_key, file_hash, task_id = upload_file(temp_file_name, upload_url, user_id, authorization_token)
        if bucket_key is not None and file_hash is not None:
            spinner = halo.Halo(text='elbo.client is finding compute options (this may take a while)',
                                spinner='bouncingBall',
                                placement='left')
            print("")
            spinner.start()
            response = request_task_run(bucket_key, file_hash, task_config, session_id)
            spinner.stop()
            if response is not None:
                chosen_type = prompt_user(response)
                spinner = halo.Halo(text='elbo.client is provisioning compute (usually takes ~ 4 minutes, ☕️ time!)',
                                    spinner='bouncingBall',
                                    placement='left')
                spinner.start()
                response_json = provision_compute(chosen_type, session_id, task_config, config)
                spinner.stop()
                if response_json is not None:
                    ip, password = process_compute_provisioned_response(response_json,
                                                                        ssh_only=False)
                    client = paramiko.SSHClient()
                    wait_for_ssh_ready(client, ip, password)
                else:
                    logger.error(f"something went wrong with provisioning, please try again ...")
            else:
                logger.error(f"is unable to get compute options from ELBO servers")
        else:
            logger.info(f":(. something went wrong with upload, please send us a bug report at bugs@elbo.ai")

    else:
        if user_id is None:
            logger.error(f"is unable to verify your membership.")
            logger.error("please obtain your token from https://elbo.ai/welcome, and run `elbo login`")
        else:
            logger.info(f"is unable to obtain upload url. Please report this to bugs@elbo.ai.")

    return ip, password


@cli.command(name='run')
@click.option('--config',
              type=click.Path(),
              default="elbo.yaml", help='The path of the ELBO yaml configuration file')
def run(config):
    """
    Submit a task specified by the config file.
    """
    run_internal(config)


def create_tar_gz_archive(output_filename, source_dir):
    """
    Create a tar gzip file

    :param output_filename: The name of the output file
    :param source_dir: The directory to tar and gzip
    :return: None
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def generate_short_rand_string():
    """
    Generate a short random string
    :return: The random string
    """
    return str(uuid.uuid4())[:8]


def get_temp_file_path(tgz=False):
    """
    Generate a name for temp file
    :return: A random temp file name
    """
    rand_string = f"elbo-archive-{generate_short_rand_string()}"
    if tgz:
        rand_string = f"{rand_string}.tgz"

    path = os.path.join(tempfile.mkdtemp(), rand_string)
    return path


def is_elbo_outdated():
    output = subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'elbo'])
    output = str(output, encoding='utf-8').split('\n')
    installed_version = 0
    for line in output:
        if "Version:" in line:
            installed_version = line.split(" ")[1]
    try:
        response = requests.get(f'https://pypi.org/pypi/elbo/json')
        latest_version = response.json()['info']['version']
    except requests.exceptions.ConnectionError as _:
        return False, installed_version
    return installed_version != latest_version, latest_version


def exit_handler():
    is_outdated, latest_version = is_elbo_outdated()
    if is_outdated:
        logger.warning(f"A new version of elbo is available, please install using:")
        logger.warning(f"pip3 install elbo=={latest_version}")


def format_date(date):
    if date is None:
        return ""
    if type(date) is int:
        logger.warning(f"Invalid date found - {date}")
        return ""
    if len(date) > 0:
        # Convert and print date time in local timezone
        return parser.parse(date).astimezone().strftime("%m/%d/%y %H:%M")
    return ""


def format_time(time_delta_in_seconds):
    if time_delta_in_seconds is None:
        return ""

    if type(time_delta_in_seconds) is str:
        if len(time_delta_in_seconds) == 0:
            return ""
        try:
            time_delta_in_seconds = int(time_delta_in_seconds)
        except ValueError as _:
            try:
                from tzlocal import get_localzone  # $ pip install tzlocal
                local_tz = get_localzone()
                date_time = dt.datetime.strptime(time_delta_in_seconds, "%H:%M:%S.%f").replace(tzinfo=local_tz)
                time_delta_in_seconds = date_time.timestamp()
                time_delta_in_seconds = strftime("%Hh:%Mm:%Ss", time.localtime(time_delta_in_seconds))
                return time_delta_in_seconds
            except ValueError as _:
                return time_delta_in_seconds

    if type(time_delta_in_seconds) is float:
        time_delta_in_seconds = int(time_delta_in_seconds)

    time_delta_in_seconds = strftime("%Hh:%Mm:%Ss", gmtime(time_delta_in_seconds))
    return time_delta_in_seconds


def transform_date():
    return lambda x: format_date(x)


atexit.register(exit_handler)


def elbo_except_hook(exception_type, value, traceback):
    report = ''.join(format_exception(exception_type, value, traceback, 50))
    print(report)
    params = {
        'exception_report': str(report)
    }
    _ = __elbo_connector.request(ElboConnector.EXCEPTION_REPORT_ENDPOINT,
                                 params=params,
                                 method='POST')
    sys.__excepthook__(exception_type, value, traceback)


# noinspection SpellCheckingInspection
sys.excepthook = elbo_except_hook

if __name__ == '__main__':
    cli()
