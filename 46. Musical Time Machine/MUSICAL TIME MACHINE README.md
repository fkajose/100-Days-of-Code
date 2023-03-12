# Musical Time Machine

This script allows you to scrape the Billboard 100 list for a specific date and create a Spotify playlist with those songs.

## Setup

Before running the script, you need to do the following:

1. Create a Spotify account (if you don't already have one).
1. Create a new Spotify App [here](https://developer.spotify.com/dashboard/applications) and get your `Client ID` and `Client Secret`.
1. Set the Redirect URI of your app to `<http://localhost:8888/callback>`.
1. Add your `Client ID` and `Client Secret` as environment variables named `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`, respectively.
1. Install the required packages by running pip install -r requirements.txt in your terminal.

## Usage

To use this script, simply run `python main.py` in your terminal and follow the prompts.

1. Enter the date you want to travel to in the format `YYYY-MM-DD`.
1. The script will scrape the Billboard 100 list for that date and create a text file named `songs.txt` containing the list of songs.
1. The script will then search for each song on Spotify and create a new private playlist with the name `{date} Billboard 100` and add all the matching songs to it.

Note: If a song is not available on Spotify, the script will print a message indicating that the song has been skipped.
