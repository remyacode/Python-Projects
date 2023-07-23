#playlist

from pytube import Playlist

pl=Playlist("")

print(f'Downloading: {pl.title} ')

for video in pl.videos:
    video.streams.first().download()