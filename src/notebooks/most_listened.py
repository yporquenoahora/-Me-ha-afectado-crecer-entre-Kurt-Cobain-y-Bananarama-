
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os


os.getcwd()
scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9d24693b130840829fc41aabcada8c66",
                                               client_secret="1d8ba6c6e2ab4c8aa0bac0f3fe408142",
                                               redirect_uri="http://localhost:1234",
                                               scope='user-top-read user-follow-read'))


ranges = ['short_term', 'medium_term', 'long_term']
res = []

for sp_range in ranges:
    #print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):          
        res.append({"name":item["name"], "artists":item['artists'][0]['name'], "id": item["uri"].split(":")[-1]})
    print()

df = pd.DataFrame(res)



aAnalisysTrack = []
aAnalisysBeats = []
aAnalisysSections = []
aAnalisysSegments = []
aAnalisysTatums = []


tracks = []
afeatures = []
for i in res:
    features = sp.audio_features(i["id"])    
    features.append({"id": i["id"]})
    track = sp.track(i["id"])
    track.update({"id": i["id"]})
    
    track.update({"artists_name": track["album"]["artists"][0]["name"]})
    album_release = track["album"]["release_date"]
    
    track.update({"release_date": album_release})
    tracks.append(track)
    afeatures.append(features[0])


print("features:::",afeatures[0].keys())
print("tracks::", tracks[0].get("id"))



dfTracks = pd.DataFrame(tracks)
dfFeatures = pd.DataFrame(afeatures)

joinAll = pd.merge(dfTracks, dfFeatures, on="id", how="outer")
joinAll.set_index('id')

#print(joinAll.columns)

merge = joinAll.loc[:, ['name',  "artists_name","album","release_date","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature","explicit","popularity", "duration_ms_y", "id"]]
print(type(merge))
merge.set_index("id")
#dfTracks.head()
#playlist_tracks[0].get("track").get("album").get("release_date")

dfTracks.to_csv("src/data/most_listened_songs.csv", encoding='utf-8')
dfFeatures.to_csv("src/data/most_listened_songs_features.csv", encoding='utf-8')
joinAll.to_csv("src/data/most_listened.csv", encoding='utf-8')
merge.to_csv("src/data/merge.csv", encoding='utf-8')

#print(df)
