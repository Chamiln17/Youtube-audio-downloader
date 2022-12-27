from pytube import YouTube
from pytube import Playlist
import os
url = input("enter the url of the playlist you want to download as an audio :") 
p = Playlist(url)
# The playlist must be public 
emplacment= input("Enter the absolute path for your file:")
for video in p.videos :
    vid =video.streams.get_by_itag(251) #getting by itag , a code that refers to a specific sound or audio quality
    try:
        out_file = vid.download(output_path=emplacment) #download it in the specific folder 
        base, ext = os.path.splitext(out_file) # split the name of the file (in base ) and its extension ( in ext )
        new_file = base + '.mp3' #add the .mp3 extension
        os.rename(out_file, new_file) #rename the file 
        print(vid.title + " has been successfully downloaded.")
    except:
        print("Video doesn't exist")
print ("-----------------------------------------------end------------------------------------------")
