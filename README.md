# Prockxy
*[FM802のオンエア曲目](https://funky802.com/service/OnairList/today)をスクレイピングし, Slack APIのIncoming Webhookでチャンネルに新曲をリコメンドします。*  

### 環境構築

```bash
$ git clone https://github.com/tyokinuhata/prockxy.git
$ cd prockxy
$ pipenv install
$ cp config.ini.example config.ini  // その後, Slackから発行したIncoming WebhookのURLを追記する
$ touch database.sqlite
```

### コマンド

```
$ pipenv run db                     // DBを作り直す
$ pipenv run scrape                 // FM802からスクレイピングしてくる
$ pipenv run slack                  // Slackに投稿する
$ pipenv run cron                   // "pipenv run scrape"と"pipenv run slack"を定期実行する. 本番環境では "pipenv run cron &"でバックグラウンド実行にする
```