from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Now downloading:", yt.title)

yd = yt.streams.get_highest_resolution() 
yd.download("C:/Users/CourtneyStow/Documents/Youtube-downloads/")