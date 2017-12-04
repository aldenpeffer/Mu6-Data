#!/usr/bin/env python3
import json
import requests
import sys
from pprint import pprint

jsonHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

multipartHeaders = {
    'Accept': 'application/json'
}
# command line args:
# data/users.json data/artists.json data/albums.json data/tracks.json
# argv[0] is the prog name
# argv[1:] is the list of args excluding the prog name

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print("executing " + arg)
        with open(arg) as data_file:
            data = json.load(data_file)
            endpoint = data['endpoint']
            entities = data['entities']
            mimetype = data['mimetype']
            if mimetype == 'application/json':
                for entity in entities:
                    requests.post(endpoint, headers=jsonHeaders, data=entity)
            elif mimetype == 'multipart/form-data':
                for entity in entities:
                    requests.post('http://localhost:4567/album/add', headers=multipartHeaders, files={
                        'data': (entity['data'], open(entity['data'], 'rb')),
                        'metadata': (None, entity['metadata'])
                    })
            else:
                print("unsupported MIME type")

