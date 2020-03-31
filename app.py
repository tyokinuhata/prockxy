import uuid
from slack_incoming_webhook import SlackIncomingWebhook
import requests
from bs4 import BeautifulSoup

# スクレイピング
url = 'https://funky802.com/service/OnairList/today'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
songs = soup.find('dl', attrs={'class': 'noa-song-list'})
songs = songs.find_all('dd')
for song in songs:
    song_name = song.find('span', attrs={'class': 'song-name'})
    artist = song.find('span', attrs={'class': 'artist-name'})
    # audio = song.find('span', attrs={'class': 'audition'})
    print(song_name.contents[0], artist.contents[0])

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