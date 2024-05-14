import os
import json
import requests
import logging as logger
from requests_oauthlib import OAuth1
from wooapitest.src.configs.hosts_config import API_HOSTS
from wooapitest.src.utils.credentials_utils import CredentialsUtility


class RequestsUtility(object):
    def __init__(self):
        self.payload = None
        self.url = None
        self.headers = None
        self.rs_json = None
        self.expected_status_code = None
        self.status_code = None

        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'dev')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds["wc_key"], wc_creds["wc_secret"])
        logger.debug(f"Inside requestsUtility env is {self.env} and baseurl is {self.base_url}")

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code. " \
                                                              f"Expected status code: {self.expected_status_code} Actual status code: {self.status_code} " \
                                                              f"URL: {self.url} Headers: {self.headers} " \
                                                              f"Response: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        self.headers = headers
        self.payload = payload
        self.expected_status_code = expected_status_code

        logger.info(f"Sending post request with url is {self.url} payload is {self.payload} headers is {self.headers}")

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.info(f"Post API response {self.rs_json}")
        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        self.headers = headers
        self.payload = payload
        self.expected_status_code = expected_status_code

        logger.info(f"Sending get request with url is {self.url} payload is {self.payload} headers is {self.headers}")

        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.info(f"Get API response {self.rs_json}")
        return self.rs_json
