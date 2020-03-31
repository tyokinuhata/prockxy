import configparser, requests, json, uuid

# スクレイピング

# DBと照合

# DBに入れる

# Slackに流す
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
INCOMING_WEBHOOK_URL = config['DEFAULT']['INCOMING_WEBHOOK_URL']
text = str(uuid.uuid4())

requests.post(INCOMING_WEBHOOK_URL, data = json.dumps({
    'channel': '#recommend-music',
    'username': 'h-takahashi',
    'text': text,
    'icon_emoji': ':takashi:',
}))