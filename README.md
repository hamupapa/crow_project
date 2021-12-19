# flaskKOH
webアプリ作成勉強用

# 仮想環境作成
```
$ python3 -m venv venv
```

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
$ echo python-3.x.x > runtime.txt   # バージョン herokuのバージョン指定あり
```
※起動ファイルがディレクトリ内にある場合は、ディレクトリを移動するためにProcfileを以下のように作成する必要がある
```
$ echo "web: gunicorn --chdir [ディレクトリ名] [起動ファイル名]:app --log-file -" > Procfile
```
