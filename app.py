from dotenv import load_dotenv # access .env variables
import os

load_dotenv()

# https://api.genius.com/oauth/authorize?
# client_id=os.environ.get("client_id")
# client_secret=os.environ.get("client_secret")
# redirect_uri="www.google.com"
# scope="me"
# state="sTat3"
# response_type="code"

# print(client_id)
# print(client_secret)

from lyricsgenius import Genius

token=os.environ.get("token")

genius = Genius(token)

which_artist = input("Which artist are you thinking of? ")
artist = genius.search_artist(which_artist, max_songs=3, sort="title")
# print(artist.songs)

which_song = input("Which song are you thinking of? ")

song = genius.search_song(which_song, artist.name)

print(song.lyrics)

# client_credentials_manager = SpotifyClientCredentials()
# client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# def fetch_lyrics(search_term):
#     response = client.search(q=search_term, type="artist", limit=20)
#     return response

# search_term = "378195" # input("Please enter the name of a musical artist you like: ")

# results = fetch_artists(search_term)
