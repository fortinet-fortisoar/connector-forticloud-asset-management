""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from .make_rest_api_call import MakeRestApiCall


def generic_api_call(config: dict, params: dict) -> dict:
    method = params.get("method")  # GET/POST/PUT/DELETE
    endpoint = params.get("endpoint")  # edit endpoint
    payload = params.get("payload", {})

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data = payload)
    return response
