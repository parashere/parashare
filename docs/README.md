# Parashare ドキュメント

中京大学 学内傘シェアリングシステム **Parashare** のプロジェクトドキュメントです。

NFC（学生証 / スマホ）認証と RFID（傘タグ）を用いて、傘の貸出・返却を自動化するシステムです。

## ドキュメント一覧

| ファイル | 内容 |
|---------|------|
| [overview.md](overview.md) | プロジェクト概要・技術スタック・ディレクトリ構成 |
| [architecture.md](architecture.md) | システム構成（Django / FastAPI / ハードウェア）と全体の処理フロー |
| [state-transitions.md](state-transitions.md) | **状態遷移**（傘・学生・UI画面・ゲート）★メイン |
| api.md | FastAPI バックエンドの API 仕様（作成予定） |
| data-model.md | データベーススキーマ・ORM モデル（作成予定） |

## 一言まとめ

このシステムには大きく **4種類の状態** が存在します。

1. **傘の状態** … `available / rented / maintenance / lost`（DB の `parasol.status`）
2. **学生の貸出状態** … `rent / return`（`rental_history.returned_at` から動的に判定）
3. **UI画面の状態** … `0.html`〜`9.html` の10画面（端末タッチパネルの遷移）
4. **ゲートの状態** … `open / closed`（サーボモーター）

詳細は [state-transitions.md](state-transitions.md) を参照してください。
