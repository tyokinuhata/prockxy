
import requests
from bs4 import BeautifulSoup
from musics import Musics

class Scrape:
    def __init__(self):
        self.url = 'https://funky802.com/service/OnairList/today'
        self.musics = Musics()

    def __call__(self):
        res = requests.get(self.url)
        bs = BeautifulSoup(res.text, 'lxml')
        musics = bs.find('dl', attrs={'class': 'noa-song-list'})
        musics = musics.find_all('dd')
        for music in musics:
            song_name = music.find('span', attrs={'class': 'song-name'}).contents[0]
            artist = music.find('span', attrs={'class': 'artist-name'}).contents[0]
            dummy_url = '/elements/shared/images/dummy.jpg'
            cd_jacket = 'https://funky802.com{}'.format(dummy_url) if music.find('img')['src'] == dummy_url else music.find('img')['src']
            exists = self.musics.exists(song_name, artist)
            if (not exists):
                self.musics.insert(song_name, artist, cd_jacket)

if __name__ == '__main__':
    print('Scraping musics ...')
    scrape = Scrape()
    scrape()
    print('Succeed!')