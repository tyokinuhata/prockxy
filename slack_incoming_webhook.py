import configparser, requests, json

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