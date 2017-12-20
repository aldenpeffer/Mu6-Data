#!/usr/bin/env python3
import json
import requests
import sys
from pprint import pprint

jsonHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

multipartHeaders = {
    'Accept': 'application/json'
}

def send(base_url, data, saved={}):
    endpoint = data['endpoint']
    entities = data['entities']
    mimetype = data['mimetype']
    saveitem = data['saveitem'] if 'saveitem' in data else {}
    if mimetype == 'application/json':
        for entity in entities:
            for attribute in saved:
                if attribute in entity['entity']:
                    entity['entity'][attribute] = saved[attribute]
            print('Request : {:s}\n{:s}'.format(endpoint, str(entity['entity'])))
            response = requests.post(base_url + endpoint, headers=jsonHeaders, json=entity['entity'])
            print('Response: {:d}\n{:s}'.format(response.status_code, response.text))
            print()
            error = False
            try:
                for keymap in saveitem:
                    val = response.json()
                    for key in keymap['path']:
                        val = val[key]
                    saved[keymap['name']] = val
            except:
                error = True
            if 'dependents' in entity and not error:
                send(base_url, entity['dependents'], saved)
    elif mimetype == 'multipart/form-data':
        for entity in entities:
            for attribute in saved:
                if attribute in entity['entity']['metadata']:
                    entity['entity']['metadata'][attribute] = saved[attribute]
            print('Request : {:s}\n{:s}'.format(endpoint, str(entity['entity'])))
            response = requests.post(base_url + endpoint, headers=multipartHeaders, files={
                'metadata': (None, json.dumps(entity['entity']['metadata']), 'application/json'),
                'data': (entity['entity']['data'], open(entity['entity']['data'], 'rb'))
            })
            print('Response: {:d}\n{:s}'.format(response.status_code, response.text))
            print()
            error = False
            try:
                for keymap in saveitem:
                    val = response.json()
                    for key in keymap['path']:
                        val = val[key]
                    saved[keymap['name']] = val
            except:
                error = True
            if 'dependents' in entity and not error:
                send(base_url, entity['dependents'], saved)
    else:
        print("unsupported MIME type")

if __name__ == '__main__':
        #config = json.loads('{"base_url": "https://api.mu6.xyz","files": ["data/admin.json", "data/users.json", "data/artists.json"]}')
        config = json.loads('{"base_url": "http://localhost:4567","files": ["data/admin.json", "data/users.json", "data/artists.json"]}')
        for data_path in config['files']:
            with open(data_path) as data_file:
                print('executing {:s}...'.format(data_path))
                print()
                send(config['base_url'], json.load(data_file))

    # ye olden days of command line args:
    # for arg in sys.argv[1:]:
    #     with open(arg) as data_file:
    #         send(json.load(data_file), {})