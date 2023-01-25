import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from pprint import pprint


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
track_titles = soup.select("li ul li h3")
top_100_list = [song.get_text(strip=True) for song in track_titles]
# print(top_100_list)

# Create txt file containing the top 100 songs from that date
# with open("songs.txt", "w", encoding="utf-8") as file:
#     for song in top_100_list:
#         file.writelines(f"{song}\n")

# Authenticate Project with Spotify using unique Client ID/ Client Secret
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_id=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        client_secret="1ed38baacc3b46788f447af0c1cd25f0",
        show_dialog=True,
        cache_path="token.txt"
    )   
)

# Get user ID
user_id = sp.current_user()["id"]
# print(user_id)


#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in top_100_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.")

# print(song_uris)

# Create new playlist
playlist = sp.user_playlist_create(
    user=user_id, 
    name=f"{date} Billboard 100", 
    public=False, 
    description=f'Billboard 100 songs for {date}. Enjoy'
    )
        
# # Add tracks to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Successfully added songs to playlist!")
