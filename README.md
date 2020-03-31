# Prockxy
*Prockxyは流行曲(主に邦ロック)を探してリコメンドするサービスです。*  
*目下のところは[FM802のオンエア曲目](https://funky802.com/service/OnairList/today)を取得し, Slack APIのIncoming Webhookでチャンネルにリコメンドすることを目標に開発されています。*  
*Prockxyは最終的に様々なメディアから流行曲を探し, 様々なプラットフォームに発信することを目標にしており, プロキシのように振る舞うことからProxy x RockでProckxyという名前が与えられました。*

### 環境構築

```bash
$ git clone https://github.com/tyokinuhata/prockxy.git
$ cd prockxy
$ cp config.ini.example config.ini  // After that, add Incoming Webhook URL
$ touch database.sqlite
$ pipenv run db                     // Create database
$ pipenv run scrape                 // Scraping musics
$ pipenv run slack                  // Post music recommend to slack
$ pipenv run cron
```