from .make_rest_api_call import MakeRestApiCall


def register_service(config: dict, params: dict) -> dict:
    endpoint = "/services/register"  # edit endpoint
    method = "POST"  # GET/POST/PUT/DELETE
    contract_number = params.get("contract_number", "").strip() or None
    description = params.get("description")
    additional_info = params.get("additional_info", "")
    is_government = params.get("is_government", False)
    
    data = {
        "contractNumber": contract_number,
        "description": description,
        "additionalInfo": additional_info,
        "isGovernment": is_government
    }
    forticare = MakeRestApiCall(config=config)
    response = forticare.make_request(endpoint=endpoint, method=method, headers=forticare.headers, json_data=data)
    return response
