""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
import time
import json
from connectors.core.connector import get_logger, ConnectorError
from connectors.core.utils import update_connnector_config

error_msg = {
    401: 'Authentication failed due to invalid credentials',
    429: 'Rate limit was exceeded',
    403: 'Token is invalid or expired',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}

logger = get_logger("forticloud_asset_management")


class MakeRestApiCall:

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://{0}/ES/api/registration/v3'.format(self.server_url)
        else:
            self.server_url = self.server_url + '/ES/api/registration/v3'
        self.api_id = config.get("api_id")
        self.password = config.get("password")
        self.client_id = config.get("client_id")
        self.verify_ssl = config.get("verify_ssl", True)
        self.authenticated = False
        self.headers = {}
        # Obtain the auth token which is required for Asset management calls
        self.login()


    def login(self):
        # Fill in here
        api_id = self.api_id
        password = self.password
        client_id = self.client_id

        headers = {
            "Content-Type": "application/json",
        }

        # Set up data parameter to authenticate to Forticloud FortiAuthenticator
        data = {
            "username": api_id,
            "password": password,
            "client_id": client_id,
            "grant_type": "password",
        }

        response = self.make_request(method= "POST", url="https://customerapiauth.fortinet.com/api/v1/oauth/token/",
                                     headers=headers, json_data=data)
        if response['status'] == 'success':
            self.authenticated = True
            self.headers = {"Authorization": f"Bearer {response['access_token']}"}
        else:
            logger.error("Error: {0}".format(response))
            raise ConnectorError('{0}'.format(response))


    def make_request(self, endpoint='', params=None, data=None, method='GET', headers=None, url=None, json_data=None):
        try:
            if url is None:
                url = self.server_url + endpoint

            response = requests.request(method=method, url=url,
                                        headers=headers, data=data, json=json_data, params=params,
                                        verify=self.verify_ssl)

            if response.ok:
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response.text
            else:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('{0}'.format(error_msg.get(response.status_code, response.text)))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('ssl_error')))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('time_out')))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
