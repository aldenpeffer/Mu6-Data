#!/usr/bin/env python3
import json
import requests
import sys
from pprint import pprint

jsonHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

if __name__ == '__main__':
    data_path = 'data/users.json'
    with open(data_path) as data_file:
        print('building library...')
        user_json = json.load(data_file)
        user = user_json['entities'][0]['entity']
        cred = user['credentials']
        print('sending credentials... {:s}'.format(json.dumps(cred)))
        response = requests.post('https://api.mu6.xyz/login', headers=jsonHeaders, json=cred)
        uid = response.json()['user']['lid']
        for i in range (1, 20):
            url = 'https://api.mu6.xyz/list/' + str(uid) + '/' + str((i * 4))
            response = requests.get(url)
            print('Status: ' + str(response.status_code) + ' for ' + url)