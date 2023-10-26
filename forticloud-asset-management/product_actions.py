""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from .make_rest_api_call import MakeRestApiCall


# Returns product list based on product SN search pattern or support package expiration date
def list_assets(config: dict, params: dict) -> dict:
    endpoint = "/products/list"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    serial_number = params.get("serial_number")
    expire_before = params.get("expire_before")

    data = {
        "serialNumber": serial_number
    }
    # Only add expiry day if one is provided
    if expire_before:
        data.update({"expireBefore": expire_before})

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


# Register multiple products and contracts in one request
def register_product(config: dict, params: dict) -> dict:
    endpoint = "/products/register"  # edit endpoint
    method = "POST"
    serial_number = params.get("serial_number")
    contract_number = params.get("contract_number", "").strip() or None
    description = params.get("description")
    asset_group_ids = params.get("asset_group_ids", []) or None
    replaced_serial_number = params.get("replaced_serial_number", "") or None
    additional_info = params.get("additional_info", "")
    cloud_key = params.get("cloud_key") or None
    is_government = params.get("is_government", False)

    data = {"registrationUnits": [
        {
            "serialNumber": serial_number,
            "contractNumber": contract_number,
            "description": description,
            "assetGroupIds": asset_group_ids,
            "replacedSerialNumber": replaced_serial_number,
            "additionalInfo": additional_info,
            "cloudKey": cloud_key,
            "isGovernment": is_government,
            # "location": {"ref": "#/locations/0"}
        }
    ]
    }

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


# Update description of a product
def update_description(config: dict, params: dict) -> dict:
    endpoint = "/products/description"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    serial_number = params.get("serial_number")
    description = params.get("description")
    data = {
        "serialNumber": serial_number,
        "description": description
    }

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


# Returns product detailed information, including active support coverage and associated licenses
def product_details(config: dict, params: dict) -> dict:
    endpoint = "/products/details"
    method = "POST"  # GET/POST/PUT/DELETE
    serial_number = params.get("serial_number")
    data = {
        "serialNumber": serial_number
    }

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


# Update description of a product
def update_location(config: dict, params: dict) -> dict:
    endpoint = "/products/location"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    serial_number = params.pop("serial_number")
    location_data = {k: v for k, v in params.items() if v}
    data = {
        "serialNumber": serial_number,
        "location": location_data
    }
    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


# Decommission products using serial number
def decommission_product(config: dict, params: dict) -> dict:
    endpoint = "/products/decommission"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    serial_numbers = params.pop("serial_numbers")

    # convert serial numbers to a list if not already
    if type(serial_numbers) == str:
        serial_numbers = serial_numbers.split(",")
        serial_numbers = [serial_number.strip() for serial_number in serial_numbers]

    data = {
        "serialNumbers": serial_numbers,
    }
    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response
