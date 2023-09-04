from .make_rest_api_call import MakeRestApiCall


# Returns product list based on product SN search pattern or support package expiration date
def register_license(config: dict, params: dict) -> dict:
    endpoint = "/licenses/register"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    license_registration_code = params.get("license_registration_code", "")
    serial_number = params.get("serial_number", "")
    description = params.get("description")
    additional_info = params.get("additional_info", "")
    is_government = params.get("is_government", False)

    data = {
        "licenseRegistrationCode": license_registration_code,
        "serialNumber": serial_number,
        "description": description,
        "additionalInfo": additional_info,
        "isGovernment": is_government
    }

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response


def download_license(config: dict, params: dict) -> dict:
    endpoint = "/licenses/download"
    method = "POST"  # GET/POST/PUT/DELETE
    serial_number = params.get("serial_number", "")

    data = {
        "serialNumber": serial_number
    }

    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response
