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

base_url = "https://api.mu6.xyz"
# command line args:
# data/artists.json data/albums.json data/tracks.json
# argv[0] is the prog name
# argv[1:] is the list of args excluding the prog name



def send(data, saved):
    endpoint = data['endpoint']
    entities = data['entities']
    mimetype = data['mimetype']
    saveitem = data['saveitem']
    if mimetype == 'application/json':
        for entity in entities:
            for attribute in saved:
                if attribute in entity['entity']:
                    entity['entity'][attribute] = saved[attribute]
                    print('amended:')
                    print(entity['entity'])
            print('Request : {:s}'.format(str(entity['entity'])))
            response = requests.post(base_url + endpoint, headers=jsonHeaders, json=entity['entity'])
            print('Response: {:d}'.format(response.status_code))
            error = False
            try:
                for keymap in saveitem:
                    val = response.json()
                    for key in keymap['path']:
                        val = val[key]
                    saved[keymap['name']] = val
            except:
                error = True
            if entity['dependents'] and not error:
                send(entity['dependents'], saved)
    elif mimetype == 'multipart/form-data':
        for entity in entities:
            for attribute in saved:
                if attribute in entity['entity']['metadata']:
                    entity['entity']['metadata'][attribute] = saved[attribute]
                    print('amended:')
                    print(entity['entity']['metadata'])
            print('Request : {:s}'.format(str(entity['entity'])))
            response = requests.post(base_url + endpoint, headers=multipartHeaders, files={
                'metadata': (None, json.dumps(entity['entity']['metadata']), 'application/json'),
                'data': (entity['entity']['data'], open(entity['entity']['data'], 'rb'))
            })
            print('Response: {:d}'.format(response.status_code))
            exit()
    else:
        print("unsupported MIME type")

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        with open(arg) as data_file:
            send(json.load(data_file), {})