# import necessary libraries
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import re

# Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='9a2e8ac413984e96a36b07310ee343bc', 
    client_secret='27eb568407b74bbf93bbb913f251d5c0' 
))

# Playlist URL
playlist_url = "https://open.spotify.com/playlist/4K3pSspaSSQZPh0bRnND3h"
playlist_match = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url)

if playlist_match:
    playlist_id = playlist_match.group(1)
    print("Extracted Playlist ID:", playlist_id)
    print("Fetching playlist data...")

else:
    print("Error: Could not extract Playlist ID. Check the URL format.")
    exit()

# Playlist details
playlist_info = sp.playlist(playlist_id)
playlist_name = playlist_info['name']
print(f"Fetching tracks from Playlist: {playlist_name}")

# Fetch all tracks in the playlist
playlist_tracks = sp.playlist_tracks(playlist_id)

# Store track data
track_data_list = []

for item in playlist_tracks['items']:
    track = item['track']
    track_data = {
        'Track Name': track['name'],
        'Artist': track['artists'][0]['name'],
        'Album': track['album']['name'],
        'Popularity': track['popularity'],
        'Duration (minutes)': track['duration_ms'] / 60000
    }
    track_data_list.append(track_data)

# Convert metadata to DataFrame
df = pd.DataFrame(track_data_list)
print("\nPlaylist Track Data:")
print(df)

# Save playlist data to CSV
df.to_csv('spotify_playlist_data.csv', index=False)
print("\nData saved to spotify_playlist_data.csv")


if df.empty:
    print("No track data available for visualization.")
    exit()

print("\nFull Playlist Details:")

print(df.to_string(index=False))
print("Finsihed fetching playlist data.")

#pip freeze > requirements.txt