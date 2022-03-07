from asyncio.constants import ACCEPT_RETRY_DELAY
import json
from strava_api_details import * 
import os 
from typing import dict

id = 701809


def return_segment_api(id: int, access_token:str) -> None:
    os.system(f"curl -X GET https://www.strava.com/api/v3/segments/{id} -H 'Authorization: Bearer {access_token}' -o segment_{id}.JSON")


return_segment_api(id, access_token)
def return_segment_local(id, access_token) -> dict:
    with open(f'segment_{id}.JSON') as f:
        json_data = json.load(f)
    return json_data

ret

# def get_segment_climbing_details(segment: json):
#     average_grade = segment['average_grade']
#     return average_grade




