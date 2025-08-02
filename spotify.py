import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

emotion_playlists = {
   "Happy": "5iR7JBR9Ot6ZPgs4GaPOm2",
    "Sad": "3Kd8XtyN0CmFVZ0SxJTi37",
    "Angry": "5ymqBA8vZSnPEZfDJeuhH1",
    "Overwhelmed": "1LWyQBS7lXGMvHg17m8udS",
    "Worse": "3vleBofUVfr7nfyYLgyPUZ"
}
messages = {
    "Happy": "Here is a happy playlist just for you <3",
    "Sad": "Here is a sad playlist just for you, hope you are doing better soon <3",
    "Angry": "Here is your angry playlist, please calm down a little !!",
    "Overwhelmed": "Here is a playlist to help you relax and feel better",
    "Worse": "You just need to listen to some rock and rock your body. Here you go!!"
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-read-private"
))

emotion = input("How are you feeling right now? Happy, Sad, Angry, Overwhelmed or Worse? ").title()

if emotion in emotion_playlists:
    playlist_id = emotion_playlists[emotion]
    try:
        playlist = sp.playlist(playlist_id, market="from_token")


        print(f"\n{messages[emotion]}")
        print(f" Playlist: {playlist['name']}")
        print(f" Description: {playlist.get('description', 'No description')}")

        print("\n🎶 Songs:")
        for item in playlist['tracks']['items'][:10]:
            track = item['track']
            name = track['name']
            artist = track['artists'][0]['name']
            print(f"→ {name} - {artist}")
    except Exception as e:
        print("Error accessing playlist:", e)
else:
    print("Sorry, I don't have a playlist for that emotion right now, but you can always listen to your favorite music! Take care <3")
