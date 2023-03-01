from pytube import YouTube
from sys import argv

link = input('link here: ')
yt = YouTube(link)

print('Title ', yt.title)
print('View ', yt.views)

yd = yt.streams.get_highest_resolution()

#Change this Path, you can add path with a '/'
yd.download("/Users/YOURNAME/YOURPATH")

input('Press any Button...')