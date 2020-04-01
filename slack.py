import configparser, requests, json, random
from musics import Musics

class Slack:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        self.INCOMING_WEBHOOK_URL = config['DEFAULT']['INCOMING_WEBHOOK_URL']
        self.CHANNEL = '#{}'.format(config['DEFAULT']['CHANNEL'])
        self.USERNAME = config['DEFAULT']['USERNAME']
        self.ICON = config['DEFAULT']['ICON']

    def post(self, text):
        requests.post(self.INCOMING_WEBHOOK_URL, data = json.dumps({
            'channel': self.CHANNEL,
            'username': self.USERNAME,
            'text': text,
            'icon_emoji': ':{}:'.format(self.ICON),
        }))
        return self

if __name__ == '__main__':
    print('Posting message ...')
    musics = Musics()
    end = musics.count()
    begin = 1 if end - 200 < 1 else end - 200
    music = musics.find(id = random.randint(begin, end))
    slack = Slack()
    slack.post(text=u'{}\n{} - {}'.format(music[3], music[1], music[2]))
    print('Succeed!')