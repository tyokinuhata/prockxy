import configparser, requests, json, random
from musics import Musics

class SlackIncomingWebhook:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        self.INCOMING_WEBHOOK_URL = config['DEFAULT']['INCOMING_WEBHOOK_URL']

    def post(self, channel, username, text, icon):
        requests.post(self.INCOMING_WEBHOOK_URL, data = json.dumps({
            'channel': channel,
            'username': username,
            'text': text,
            'icon_emoji': ':{}:'.format(icon),
        }))
        return self

if __name__ == '__main__':
    print('Posting message ...')
    musics = Musics()
    end = musics.count()
    begin = 1 if end - 200 < 1 else end - 200
    music = musics.find(id = random.randint(begin, end))
    slack_incoming_webhook = SlackIncomingWebhook()
    slack_incoming_webhook.post(
        channel='#recommend-music',
        username='h-takahashi',
        text=u'{} - {}'.format(music[1], music[2]),
        icon='takashi',
    )
    print('Succeed!')