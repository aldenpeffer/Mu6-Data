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

baseUrl = "https://mu6.xyz"
# command line args:
# data/artists.json data/albums.json data/tracks.json
# argv[0] is the prog name
# argv[1:] is the list of args excluding the prog name

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print("executing " + arg)
        with open(arg) as data_file:
            data = json.load(data_file)
            endpoint = baseUrl + data['endpoint']
            entities = data['entities']
            mimetype = data['mimetype']
            if mimetype == 'application/json':
                for entity in entities:
                    response = requests.post(endpoint, headers=jsonHeaders, json=entity)
                    print('Status: ' + str(response.status_code))
            elif mimetype == 'multipart/form-data':
                for entity in entities:
                    response = requests.post(endpoint, headers=multipartHeaders, files={
                        'metadata': (None, json.dumps(entity['metadata']), 'application/json'),
                        'data': (entity['data'], open(entity['data'], 'rb'))
                    })
                    print('Status: ' + str(response.status_code))
            else:
                print("unsupported MIME type")

