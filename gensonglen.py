#!/usr/bin/env python3
import json
import os
import math

from mutagen.mp3 import MP3

def update_with(runtimes, data):
    endpoint = data['endpoint']
    entities = data['entities']
    mimetype = data['mimetype']
    saveitem = data['saveitem'] if 'saveitem' in data else {}
    for entity in entities:
        if 'metadata' in entity['entity']:
            if 'runTime' in entity['entity']['metadata']:
                entity['entity']['metadata']['runTime'] = runtimes[entity['entity']['data']]
        if 'dependents' in entity:
            update_with(runtimes, entity['dependents'])

if __name__ == '__main__':
    songlens = {}
    updated_json = ''
    for filename in os.listdir('audio'):
        try:
            audio = MP3('audio/' + filename)
            songlens['audio/' + filename] = format_time(audio.info.length)
        except:
            songlens['audio/' + filename] = ''
    with open('data/artists.json') as artist_file:
        updated_json = json.load(artist_file)
        update_with(songlens, updated_json)
    with open('data/updated_artists.json', 'w') as update_file:
        update_file.write(json.dumps(updated_json))

def format_time(time):
    rounded = round(time)
    minutes = str(math.floor(rounded/60))
    seconds = str(rounded%60) if rounded%60 >= 10 else '0' + str(rounded%60)
    return minutes + ":" + seconds