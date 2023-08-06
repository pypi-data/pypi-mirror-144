# coding: utf-8

# Copyright 2020-2021 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import time
import requests
import uuid
from datetime import datetime
from configparser import ConfigParser
from .logger import SVTLogger

# logger = SVTLogger().get_logger()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if "FACTS_CLIENT_ENV" in os.environ:
    environment = os.environ['FACTS_CLIENT_ENV']
else:
    environment = "prod"


timeouts = "TIMEOUTS"
credentials = "CREDENTIALS"
training_data = "TRAINING_DATA"
configDir = "tests/config.ini"

config = ConfigParser()
config.read(configDir)

def get_env():
    return environment


def get_facts_client_credentials():
    return json.loads(config.get(environment, 'facts_credentials'))

def get_wml_credentials(env=environment):
    return json.loads(config.get(env, 'wml_credentials'))

def is_sanity():
    return True if "SANITY" in get_env() else False


def _get_timeout(name):
    timeout = json.loads(config.get(timeouts, name))

    return timeout * 4 if is_sanity() else timeout


def get_payload_timeout():
    return _get_timeout(name='payload_timeout')


def get_performance_timeout():
    return _get_timeout(name='performance_timeout')

def is_icp():
    if "CP4D" in get_env():
        return True
    elif "ICP" in get_env():
        return True
    elif "OPEN_SHIFT" in get_env():
        return True
    elif "OPENSHIFT" in get_env():
        return True

    return False

# def is_wml_v4():
#     if "WML_V4" in os.environ:
#         if str(os.environ['WML_V4']).lower() == 'true':
#             return True
#     if is_icp():
#         return True
#     return False