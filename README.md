# 名前
Photo Saver

# 概要
日向坂46公式のブログに掲載される写真をPCに保存し、携帯に送信するアプリケーション

# 制作の背景
このアプリケーションは、日向坂46のファンのために制作した。
日向坂46は公式ブログにて写真を掲載するが、携帯で保存するにはスクリーンショットをとる必要があった。
スクリーンショットではトリミングなど余計な手間が多いため、ユーザーが写真を気軽に保存できるアプリケーションを作成した。

# 使用技術
- python
- BeautifulSoup
- LINE Notify

# 技術選定の背景
### pythonを選定した理由
- スクレイピング用のライブラリ(BeautifulSoup)がある
- インターネットでの情報が豊富
- 大学の授業でも使用した

### LINE Notfyを選定した理由
- LINEが身近なアプリケーションであるから
- 携帯に送られた画像は携帯で気軽に保存できるから
  
### 使用方法
1. [LINE Notify公式サイト](https://notify-bot.line.me/ja/)にアクセス
2. ログイン
3. マイページからトークンを発行
4. 発行されたトークンをコードで指定された位置にペースト
5. プログラムを実行