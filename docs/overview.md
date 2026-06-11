# プロジェクト概要 — Parashare

## 目的

**Parashare** は中京大学の **学内傘シェアリングシステム** です。
2025年度の中京大学プロジェクト活動助成金に採択されたプロジェクトとして開発されています。

QRコードに代わり、**NFC（学生証 / スマートフォンの FeliCa）認証**と **RFID（傘タグ）** を組み合わせることで、傘の貸出・返却を自動化します。学籍番号と利用履歴を連動させることで、傘の紛失対策や不正利用の抑止も図ります。

### 成果目標

- U-22 プログラミング・コンテストをはじめとする複数コンテストへの出場・受賞
- 学内での実運用に向けたシステム構築・導入
- 学籍番号と連動した利用履歴管理・紛失対策

## 技術スタック

| 領域 | 技術 |
|------|------|
| NFC 認証 | `nfcpy`、PN532、学生証 / FeliCa |
| RFID（傘タグ） | UHF RFID リーダ（シリアル / `pyserial`、`/dev/ttyACM0`） |
| 貸出端末 | Raspberry Pi、Django、サーボモーター電子錠（`gpiozero` + pigpio、GPIO13） |
| 端末 UI | Django テンプレート（`0.html`〜`9.html`）+ ブラウザ JavaScript |
| サーバー / API | FastAPI、SQLAlchemy（async）、PostgreSQL |
| モバイルアプリ | Expo / React Native（`expo-router`） |
| ホームページ | Web サイト（Docker でデプロイ） |
| 故障検知（予定） | OpenCV 画像認識 |

## リポジトリ構成（5リポジトリ）

| リポジトリ | 役割 |
|-----------|------|
| **parashare** | 統括・全体ドキュメント（本リポジトリ）。旧コードのアーカイブも含む。 |
| **parashare-hardware** | Raspberry Pi 貸出端末。NFC / RFID 読み取り、`django_parashare` 端末アプリ、タッチ UI、サーボ電子錠制御。 |
| **parashare-backend** | FastAPI + PostgreSQL の API 本体。学生認証・貸出・返却・スタンド管理。 |
| **parashare-mobile-app** | モバイルアプリ（Expo / React Native）。利用者向け。 |
| **parashare-homepage** | プロジェクト紹介ホームページ。 |

> NFC 読み取り処理と Django 端末アプリは、本リポジトリ（`NFC/`、`RFID/`、`django_parashare/`）から **parashare-hardware** へ移行されています。API 本体（`backend/`、`client_test/`）は **parashare-backend** へ移行済みで、本リポジトリ内のコピーは旧版アーカイブです。

## 本リポジトリ（parashare）のディレクトリ構成

```
parashare/
├── docs/                  ← プロジェクトドキュメント（本ディレクトリ）
│   ├── README.md          … ドキュメント索引
│   ├── overview.md        … プロジェクト概要（本ファイル）
│   ├── architecture.md    … システム全体構成と処理フロー
│   └── state-transitions.md … 状態遷移（メインドキュメント）
│
├── NFC/                   ← NFC 読み取り検証コード（nfcpy）。学籍番号抽出ロジック。
│   ├── main.py            … タグから学籍番号を抽出する基本実装
│   ├── make_masterkey.py  … FeliCa マスターキー生成
│   └── read_suica/        … Suica 読み取り検証
│
├── RFID/                  ← RFID 読み取り検証コード（シリアル通信）
│
├── django_parashare/      ← Raspberry Pi 貸出端末アプリ（Django）
│   ├── parashare_app/
│   │   ├── views.py            … 画面 0〜9 のルーティング
│   │   ├── nfc_reader.py       … NFC 読み取り API（学籍番号取得）
│   │   ├── rfid_reader.py      … RFID 読み取り API（傘タグ）
│   │   ├── servo_controller_simple.py … サーボ電子錠の開閉 API
│   │   ├── sendserver.py       … バックエンド API への中継
│   │   └── urls.py             … URL 定義
│   └── templates/         … 端末 UI（0.html〜9.html）
│
├── backend/               ← API 本体の旧コピー（FastAPI、確認用）
│   ├── app/
│   │   ├── main.py            … FastAPI エントリポイント
│   │   ├── db/db_models.py    … SQLAlchemy モデル
│   │   ├── routes/device.py   … 端末向けエンドポイント
│   │   └── schemas/api_schemas.py … Pydantic スキーマ
│   └── sql/database.sql       … DB スキーマ（DDL）
│
└── client_test/           ← API クライアント検証コードの旧コピー
```

## 関連ドキュメント

- [architecture.md](architecture.md) — システム全体構成と貸出 / 返却の処理フロー
- [state-transitions.md](state-transitions.md) — 4種類の状態遷移（メインドキュメント）
</content>
</invoke>
