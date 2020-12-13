import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import pprint

client_id = '...'
client_secret = '...'

client_credentials_manager = SpotifyClientCredentials (client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

artistList = ["The Beatles", "The Clash", "Snoop Dogg", "America", "Jamiroquai", "Faithless", "The Rolling Stones", "Gorillaz", "Phoenix", "Daft Punk"]

for artistName in artistList:

    name = artistName
    tracks = []
    artistListName = []
    artistListUri = []
    popularity = ""

    resultArtists = sp.search(q='artist:' + name, type='artist')

    for artist in resultArtists['artists']['items']:
        if(artist["name"].lower() == name.lower()):
            if(artist["popularity"] > 1):
                popularity = artist["name"], ", Popularité :", artist["popularity"], ", Uri :", artist["uri"]
                print(popularity)

    if len(popularity) < 1:

        for track in tracks:
            resultTrack = sp.search(q='track:' + track, type='track')
            for items in resultTrack['tracks']["items"]:
                for artist in items["album"]["artists"]:
                    if artist["name"].lower() == name.lower():
                        artistListName.append(artist["name"])
                        artistListUri.append(artist["uri"])

        artistByUri = sp.artist(artistListUri[0])
        print(artistByUri["name"], ", Popularité :", artistByUri["popularity"], ", Uri :", artistListUri[0])









