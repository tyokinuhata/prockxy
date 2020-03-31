import configparser, requests, json

# スクレイピング

# DBと照合

# DBに入れる

# Slackに流す
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
INCOMING_WEBHOOK_URL = config['DEFAULT']['INCOMING_WEBHOOK_URL']

requests.post(INCOMING_WEBHOOK_URL, data = json.dumps({
        'channel': u'#recommend-music',
        'username': u'h-takahashi',
        'text': u'黙ってろこのカス',
        'icon_emoji': u':takashi:',
}))