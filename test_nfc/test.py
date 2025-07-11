import nfc
import re
import time

def extract_student_id(tag_data):
    pattern = re.compile(r"[A-Za-z]?\d{6,10}")  # 6～10桁の学籍番号のパターン
    for line in tag_data:
        match = pattern.search(line)
        if match:
            return match.group()
    return "学籍番号が見つかりません"

def on_connect(tag):
    try:
        tag_data = tag.dump()
        student_id = extract_student_id(tag_data)
        print("学籍番号:", student_id)
    except Exception as e:
        print("タグ読み取りエラー:", e)
    return False  # タグ検出後に終了

if __name__ == "__main__":
    with nfc.ContactlessFrontend("usb") as clf:
        print("NFCタグをかざしてください...")
        clf.connect(rdwr={"on-connect": on_connect})
        print("読み取りが完了しました。")