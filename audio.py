from pytube import Playlist
from pytube import YouTube
import os #to rename the files extentions
print("-----------------------------------------------start------------------------------------------")

while type != "v" and type != "p":
    type = input("Do you want to download a video's audio or a playlist? (v/p): ")
if type == "p":    
    url = input("Enter the URL of the playlist you want to download as an audio: ")
    p = Playlist(url)
    # The playlist must be public
    emplacment = input("Enter the absolute path for your file: ")

    for video in p.videos:
        if (video.age_restricted == True):
            print("Age restricted video: " + video.title + " has not been downloaded.")
            continue
        else:
            try:
                vid = video.streams.filter(only_audio=True).order_by('abr').desc().first()# to get the highest quality audio
                out_file = vid.download(output_path=emplacment)  # download it in the specific folder
                base, ext = os.path.splitext(out_file)  # split the name of the file (in base) and its extension (in ext)
                new_file = base + '.mp3'  # add the .mp3 extension
                os.rename(out_file, new_file)  # rename the file
                print(vid.title + " has been successfully downloaded.")
            except:
                print("Video doesn't exist")# your playlist may contain a deleted video, so this will prevent the program from crashing
else:
    url = input("Enter the URL of the playlist you want to download as an audio: ")
    video = YouTube(url)
    # The video must be public
    emplacment = input("Enter the absolute path for your file: ")
    if (video.age_restricted == True):
        print("Age restricted video: " + video.title + " has not been downloaded.")
    else:
        try:
            vid = video.streams.filter(only_audio=True).order_by('abr').desc().first()# to get the highest quality audio
            out_file = vid.download(output_path=emplacment)  # download it in the specific folder
            base, ext = os.path.splitext(out_file)  # split the name of the file (in base) and its extension (in ext)
            new_file = base + '.mp3'  # add the .mp3 extension
            os.rename(out_file, new_file)  # rename the file
            print(vid.title + " has been successfully downloaded.")
        except:
            print("Video doesn't exist")# your playlist may contain a deleted video, so this will prevent the program from crashing
    
print("-----------------------------------------------end------------------------------------------")
