import configparser, requests, json, random
from cache_musics import CacheMusics

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
    cache_musics = CacheMusics()
    music = cache_musics.find(id = random.randint(1, cache_musics.count()))
    slack_incoming_webhook = SlackIncomingWebhook()
    slack_incoming_webhook.post(
        channel='#recommend-music',
        username='h-takahashi',
        text=u'{} - {}'.format(music[1], music[2]),
        icon='takashi',
    )
    print('Succeed!')