import os 
import json

client_id = 79189
client_secret = 'dc67a4805c7b98fdbdafae70744e24741bfaba6b'
refresh_token = 'f2f8e308915b4c209fca0727beb43bd27d6ec735'
os.system(f"curl -X POST https://www.strava.com/api/v3/oauth/token \
  -d client_id={client_id} \
  -d client_secret={client_secret} \
  -d grant_type=refresh_token \
  -d refresh_token={refresh_token} \
  -o keys.JSON"
)

with open("keys.JSON") as f:
    json_data = json.load(f)

access_token = json_data['access_token']


access_token = '0c13d93fbeae34cb1509160c67860939e910b470' 