from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# Create your views here.
def index(request):
    if request.method=='POST':
        playlist_values = request.POST.get('uri')
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
        client_secret="", redirect_uri="http://localhost:8888/callback",
        scope="playlist-modify-public"))
        results = spotify.playlist_add_items(playlist_values, items=["1AT4xjNarTswd0UZ5FlmKF"])
        return render(request,'base.html',{"results":results})
    else:
# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()
      return render(request,'base.html',)
