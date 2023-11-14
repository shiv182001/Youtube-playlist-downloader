import os
from pytube import Playlist
from dotenv import load_dotenv

load_dotenv()
playlist_url = input("Enter the playlist url: ")
playlist_obj = Playlist(playlist_url)
for yt_obj in playlist_obj.videos:
    yt_stream = yt_obj.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr').desc()
    
    if yt_stream:
       yt_stream = yt_stream[0]

    print (f'Found stream:\nNAME: {yt_stream.title}\nBITRATE: {yt_stream.abr}\nTYPE: {yt_stream.subtype}')
    print ('Starting to download, please wait...')
    save = yt_stream.download(filename=yt_stream.title + ".mp3")
    print ('File saved: ', save)