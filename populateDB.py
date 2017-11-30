#!usr/bin/env python
import requests

#POST Artists
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
}
#ArtistId = 1
data = '{"user":{"title":"Portugal The Man","accountType":"ARTIST"},"credentials":{"email":"a@gmail.com","password":"p"}}'
requests.post('http://localhost:4567/user/add', headers=headers, data=data)
print("Posted Artist with ID=1")
#ArtistId = 2
data = '{"user":{"title":"Rise Against","accountType":"ARTIST"},"credentials":{"email":"b@gmail.com","password":"p"}}'
requests.post('http://localhost:4567/user/add', headers=headers, data=data)
print("Posted Artist with ID=2")
#ArtistId = 3
data = '{"user":{"title":"Shakira","accountType":"ARTIST"},"credentials":{"email":"c@gmail.com","password":"p"}}'
requests.post('http://localhost:4567/user/add', headers=headers, data=data)
print("Posted Artist with ID=3")
#ArtistId = 4
data = '{"user":{"title":"Simon and Garfunkel","accountType":"ARTIST"},"credentials":{"email":"d@gmail.com","password":"p"}}'
requests.post('http://localhost:4567/user/add', headers=headers, data=data)
print("Posted Artist with ID=4")

#POST Album
headers = {
    'Accept': 'application/json',
}
#AlbumId = 5
albumImagePath = 'images/Portugal._The_Man_Woodstock_album_cover.jpg'
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'Woodstock\',\'artistId\':1,\'releaseDate\':\'1970-01-01\'}'),
}
print("Posted Album with ID=5")
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
#AlbumId = 6
albumImagePath = "images/Rise_Against_-_The_Sufferer_&_The_Witness.jpg"
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'The Sufferer and The Witness\',\'artistId\':2,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Album with ID=6")
#AlbumId = 7
albumImagePath = "images/Shakira_Oral_Fixation_2.jpg"
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'Oral Fixation 2\',\'artistId\':3,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Album with ID=7")
#AlbumId = 8
albumImagePath = "images/Shakira_sale_el_sol_single_cover.jpg"
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'Sale el Sol\',\'artistId\':3,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Album with ID=8")
#AlbumId = 9
albumImagePath = "images/Simon_and_Garfunk_Mrs._Robinson.jpg"
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'Mrs.Robinson\',\'artistId\':4,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Album with ID=9")
#AlbumId = 10
albumImagePath = "images/Simon_and_Garfunkel,_Bridge_over_Troubled_Water.jpg"
files = {
    'data': (albumImagePath, open(albumImagePath, 'rb')),
    'metadata': (None, '{\'title\':\'Bridge Over Troubled Water\',\'artistId\':4,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Album with ID=10")

#POST Track
#TrackId = 1
audioPath = "audio/Portugal_The_Man_-_Feel_It_Still_Official_Video.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Feel It Still\',\'artistId\':1,\'albumId\':5,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=1")
#TrackId = 2
audioPath = "audio/Rise_Against_-_Prayer_Of_The_Refugee.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Prayer of The Refugee\',\'artistId\':2,\'albumId\':6,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=2")
#TrackId = 3
audioPath = "audio/Rise_Against_-_Savior.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Savior\',\'artistId\':2,\'albumId\':6,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=3")
#TrackId = 4
audioPath = "audio/Shakira_-_Hips_Dont_Lie_ft_Wyclef_Jean.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Hips Dont Lie\',\'artistId\':3,\'albumId\':7,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=4")
#TrackId = 5
audioPath = "audio/Shakira_-_Waka_Waka_This_Time_for_Africa_The_Official_2010_FIFA_World_Cup_Song.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Waka Waka\',\'artistId\':3,\'albumId\':8,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=5")
#TrackId = 6
audioPath = "audio/Simon_and_Garfunkel_-_Bridge_Over_Troubled_Water.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Bridge Over Troubled Water\',\'artistId\':4,\'albumId\':10,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=6")
#TrackId = 7
audioPath = "audio/Simon_Garfunkel_-_Mrs_Robinson_Audio.mp3"
files = {
    'data': (audioPath, open(audioPath, 'rb')),
    'metadata': (None, '{\'title\':\'Mrs.Robinson\',\'artistId\':4,\'albumId\':9,\'releaseDate\':\'1970-01-01\'}'),
}
requests.post('http://localhost:4567/album/add', headers=headers, files=files)
print("Posted Track with ID=7")
