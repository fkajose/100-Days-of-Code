import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
track_titles = soup.select("li ul li h3")
top_100_list = [track.getText().replace("\n", "").replace("\t", "") for track in track_titles]
# print(top_100_list)

# Create txt file containing the top 100 songs from that date
with open("songs.txt", "w", encoding="utf-8") as file:
    for song in top_100_list:
        file.writelines(f"{song}\n")

# Authenticate Project with Spotify using your unique Client ID/ Client Secret
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

