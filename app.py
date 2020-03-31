import configparser, requests, json, uuid
from slack_incoming_webhook import SlackIncomingWebhook

# スクレイピング

# DBと照合

# DBに入れる

# Slackに流す
slack_incoming_webhook = SlackIncomingWebhook()
slack_incoming_webhook.post(
    channel='#recommend-music',
    username='h-takahashi',
    text=str(uuid.uuid4()),
    icon='takashi',
)