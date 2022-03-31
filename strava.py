import os
import requests
from requests.structures import CaseInsensitiveDict
import json
import polyline
import numpy as np
import time

from strava_key_gen import access_token
from physics.params import rider_weight,frontal_area,coef_drag,weight_else,coef_rolling_resistance,air_density,coef_drag,drive_losses
from physics.functions import get_power_given_speed, converge_on_speed_given_power



class wkgCalculation:
    def __init__(self, id : int):
        self._id = id
        self._access_token = access_token
        self._is_processed = self._is_already_processed()
        self._strava_json = self._return_segment_from_api()
        self._lat_lon = self._get_lat_lon()
        self._elev_lat_lon = self._api_caller()
        
    def _is_already_processed(self):
        return str(self._id) in os.listdir('data')

    def _return_segment_from_api(self):
        if not self._is_processed:
            url = f"https://www.strava.com/api/v3/segments/{self._id}"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = f"Bearer {self._access_token}"
            resp = requests.get(url, headers=headers)
        else: 
            f = open('data' + str(id) + '/strava_json.json')
            resp = json.load(f) 
        return resp

    def _get_lat_lon(self):
        return self._strava_json['name'], polyline.decode(self._strava_json['map']['polyline']) 

    def _dump_data_to_folder(self):
        with open('data' + str(id) + '/strava_json.json', 'w') as f:
            json.dump(self._strava_json.json(), f)


    def _build_api_call(self):
        length = len(self._lat_lon)
        iterations =int(np.ceil(length/100)) 
        start, end = 0, 100
        string_lists = []
        for i in range(iterations):
            string = ''
            for j in range(start, end):
                lat, lon = self._lat_lon[j][0], self._lat_lon[j][1]
                string += str(lat) + ',' + str(lon)+ '|'
            string_lists.append(string[:-1]) # drop the last pipe
            start += 100
            
            if end + 100 > len(self._lat_lon):
                end = len(self._lat_lon) 
            else:
                end += 100
        
        return string_lists

    def _get_elev_lat_lon(call_string):
        url = f"https://api.opentopodata.org/v1/eudem25m?locations={call_string}"
        resp = requests.get(url)
        resp = resp.json()['results']
        result_list = []
        for i in range(len(resp)):
            result_list.append([resp[i]['elevation'], resp[i]['location']['lat'], resp[i]['location']['lng']])
        return result_list


    def _api_caller(self):
        if not self._is_processed:
            calls =  self._build_api_call()
            result_list = []
            for call in calls:
                time.sleep(1) # sleep for 1 second to prevent api limit
                result_list += self._get_elev_lat_lon(call)
            ell_np=np.array([np.array(xi) for xi in result_list])
        else:
            ell_np = np.load('data/' + str(id)+'/elevation_lat_lon.npy')
        return ell_np

    

    def _plot(self):
        pass
