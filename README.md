# flaskKOH
webアプリ作成勉強用

# 必要ライブラリ
```
$ python -m pip install Flask
```

# Herokuにデプロイするには
PythonのWeb Server Gateway Interface（WSGI）を実装するHTTPサーバーをインストール
```
$ python -m pip install gunicorn
```
リポジトリのルートディレクトリにファイルを３つ作成
```
$ python -m pip freeze -l > requirements.txt
$ echo "web: gunicorn [起動ファイル名]:app --log-file -" > Procfile
$ echo python-3.x.x > runtime.txt   # バージョン
```
