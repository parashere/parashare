# Parashare Django アプリケーション

Parashareの傘シェアリングシステムをDjangoで実装したWebアプリケーションです。

## セットアップ手順

### 1. 仮想環境の作成と有効化

```bash
# Windowsの場合
python -m venv venv
venv\Scripts\activate

# macOS/Linuxの場合
python3 -m venv venv
source venv/bin/activate
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. データベースの初期化

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. スーパーユーザーの作成（オプション）

```bash
python manage.py createsuperuser
```

### 5. 静的ファイルの準備

以下のSVGファイルを `static/images/` ディレクトリにコピーしてください：
- `umbrella.svg`
- `credit-card.svg`

### 6. 開発サーバーの起動

```bash
python manage.py runserver
```

アプリケーションは http://127.0.0.1:8000/ でアクセスできます。

## ファイル構成

```
django_parashare/
├── manage.py
├── requirements.txt
├── parashare/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── parashare_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── startup.html
│   └── standby.html
└── static/
    └── images/
        ├── umbrella.svg
        └── credit-card.svg
```

## 機能

- **立ち上げ画面** (`/`): システム起動時の画面、1秒後に自動でスタンバイ画面に遷移
- **スタンバイ画面** (`/standby/`): 学生証タッチ待ち画面、3秒後に認証成功画面に遷移

## 変更点

元のHTMLファイルから以下の変更を行いました：

1. **Djangoテンプレートタグの追加**:
   - `{% load static %}` で静的ファイルローダーを有効化
   - `{% static 'images/...' %}` で画像パスを動的に生成
   - `{% url "standby" %}` でURL逆引きを使用

2. **CSS変数の置き換え**:
   - `var(--dl-color-theme-*)` を具体的な色値に変更

3. **Django設定**:
   - 日本語化（`LANGUAGE_CODE = 'ja'`, `TIME_ZONE = 'Asia/Tokyo'`）
   - 静的ファイル設定
   - アプリケーション登録

## 今後の拡張

- NFC読み取り機能の実装
- データベースモデルの追加（学生情報、傘在庫管理など）
- API エンドポイントの追加
- 認証・認可システムの実装
