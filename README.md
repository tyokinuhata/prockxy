# Prockxy
*[FM802のオンエア曲目](https://funky802.com/service/OnairList/today)をスクレイピングし, Slack APIのIncoming Webhookでチャンネルに新曲をレコメンドします。*

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
$ pipenv run job                    // "pipenv run scrape"と"pipenv run slack"を定期実行する.
$ pipenv run job &                  // 本番環境の場合(バックグラウンド実行)
```

### 仕様

- FM802のオンエア曲目のスクレイピングは12時間に１回、Slackへのレコメンドは１時間に１回走る
- スクレイピングしたデータは一旦ローカルのSQLiteにキャッシュされる(重複曲はキャッシュされない)
- レコメンドは最新200件のデータからランダムに選択される