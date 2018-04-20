""" Import required libraries """
import os
import json
import httplib2

from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/drive']
BASE_URL = "https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}:append?alt=json&valueInputOption={value_input_option}"
REQUEST_HEADERS = {
    'content-type': 'application/json',
    'accept-encoding': 'gzip, deflate',
    'accept': 'application/json',
    'user-agent': 'google-api-python-client/1.6.4 (gzip)'
}


def get_authorized_http(service_account_json):
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        service_account_json, scopes=SCOPES)
    http = credentials.authorize(httplib2.Http(timeout=120))

    return http


def main(spreadsheet_id, range, value_list, service_account_json, major_dimension="ROWS", value_input_option="RAW"):
    """ Append to google sheet """

    http = get_authorized_http(service_account_json)
    url_formatted = BASE_URL.format(
        spreadsheet_id=spreadsheet_id,
        range=range,
        value_input_option=value_input_option)

    # format body
    value_range_body = {
        "range": range,
        "values": value_list,
        "majorDimension": major_dimension
    }
    
    value_range_body = json.dumps(value_range_body)
    
    # make a request
    try:
        a, result = http.request(url_formatted, 'POST',
            body=value_range_body,
            headers=REQUEST_HEADERS
        )
    except Exception, e:
        return {
            "success": False,
            "message": "Something went wrong.",
            "code": 401
        }

    return result