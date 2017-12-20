from mutagen.mp3 import MP3
import os
import math

if __name__ == '__main__':
	songlens = []
	for filename in os.listdir('audio'):
		songlen = {}
		try:
			audio = MP3('audio/' + filename)
			length = audio.info.length
			length =  round(length)
			minutes = str(math.floor(length/60))
			seconds = str(length%60) if length%60 >= 10 else '0' + str(length%60)
			formatted_len =  minutes + ":" + seconds
			songlen[filename] = formatted_len
			songlens.append(songlen)
		except:
			songlen[filename] = ''
	print(songlens)
