# バックエンド起動方法

## DBのインストール

postgresqlをインストール

/sqlの中身がデータベースの中身

---

## サーバにsshした後

`source virtual/parashare/bin/activate`

`cd parashare/backend`

`uvicorn app.main:app --host 0.0.0.0 --port 8000`

---

## エラーが出る場合

以下のようなエラーの場合
`ModuleNotFoundError: No module named 'app.db'`

以下を実行することで修正出来る。
```
touch app/__init__.py
touch app/db/__init__.py
touch app/routes/__init__.py
touch app/schemas/__init__.py
```

原因はappという単語がライブラリの認識になってしまい
`ここ→app`.main:appをフォルダとして認識できないからである。
上記のように指定してあげることでエラーを回避することが出来る。