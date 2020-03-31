import uuid
from slack_incoming_webhook import SlackIncomingWebhook
from music_cache import MusicCache
import requests
from bs4 import BeautifulSoup

# スクレイピング
url = 'https://funky802.com/service/OnairList/today'
res = requests.get(url)
bs = BeautifulSoup(res.text, 'lxml')
musics = bs.find('dl', attrs={'class': 'noa-song-list'})
musics = musics.find_all('dd')
music_cache = MusicCache()
for music in musics:
    song_name = music.find('span', attrs={'class': 'song-name'})
    artist = music.find('span', attrs={'class': 'artist-name'})
    # audio = song.find('span', attrs={'class': 'audition'})
    music_cache.insert(song_name.contents[0], artist.contents[0])

# DBと照合

# DBに入れる

# Slackに流す
# slack_incoming_webhook = SlackIncomingWebhook()
# slack_incoming_webhook.post(
#     channel='#recommend-music',
#     username='h-takahashi',
#     text=str(uuid.uuid4()),
#     icon='takashi',
# )