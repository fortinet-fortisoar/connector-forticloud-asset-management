""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""
from .make_rest_api_call import MakeRestApiCall
from .product_actions import list_assets, register_product, update_description, product_details, update_location, \
    decommission_product
from .license_actions import register_license, download_license
from .service_actions import register_service
from .generic_api_call import generic_api_call


def _check_health(config: dict) -> bool:
    try:
        MK = MakeRestApiCall(config=config)
        if MK.authenticated:
            return True
        else:
            return False
    except Exception as e:
        raise Exception(e)


operations = {
    "list_assets": list_assets,
    "register_product": register_product,
    "update_description": update_description,
    "product_details": product_details,
    "update_location": update_location,
    "decommission_product": decommission_product,
    "register_license": register_license,
    "download_license": download_license,
    "register_service": register_service,
    "generic_api_call": generic_api_call
}
