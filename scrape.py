
import requests
from bs4 import BeautifulSoup
from cache_musics import CacheMusics

class Scrape:

    def __init__(self):
        self.url = 'https://funky802.com/service/OnairList/today'
        self.cache_musics = CacheMusics()

    def __call__(self):
        res = requests.get(self.url)
        bs = BeautifulSoup(res.text, 'lxml')
        musics = bs.find('dl', attrs={'class': 'noa-song-list'})
        musics = musics.find_all('dd')
        for music in musics:
            song_name = music.find('span', attrs={'class': 'song-name'})
            artist = music.find('span', attrs={'class': 'artist-name'})
            # audio = song.find('span', attrs={'class': 'audition'})
            self.cache_musics.insert(song_name.contents[0], artist.contents[0])

if __name__ == '__main__':
    print('Scraping musics ...')
    scrape = Scrape()
    scrape()
    print('Succeed!')