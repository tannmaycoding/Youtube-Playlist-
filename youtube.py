from pytube import Channel, Playlist, YouTube
import pandas as pd

playlistInput = input("Give Playlist Path: ")

playlist = Playlist(playlistInput)
df = pd.DataFrame({}, columns=["Video", "URL", "Views"])
videoList = []
uRLList = []
viewsList = []
channelList = []
for video in playlist.videos:
    videoList.append(video.title)
    uRLList.append(video.watch_url)
    viewsList.append(video.views)
    channelList.append(video.author)

df["Video"] = videoList
df["URL"] = uRLList
df["Views"] = viewsList
df["Channel"] = channelList

print(df)
