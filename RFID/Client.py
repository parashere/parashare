# test_client.py
import unittest
import requests
import json

class TestSimpleApi(unittest.TestCase):

    BASE_URL = "http://192.168.11.41:8000"

    def test_01_get_root(self):
        """ルートパス('/')へのGETリクエストをテスト"""
        response = requests.get(self.BASE_URL + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the simple API!"})

    def test_02_get_items(self):
        """'/items'へのGETリクエストをテスト"""
        response = requests.get(self.BASE_URL + "/items")
        self.assertEqual(response.status_code, 200)
        # サーバー起動時の初期データを検証
        self.assertIn({"id": 1, "name": "item1"}, response.json()['items'])

    def test_03_post_item(self):
        """'/items'へのPOSTリクエストをテスト"""
        new_item = {"id": 3, "name": "item3"}
        response = requests.post(self.BASE_URL + "/items", json=new_item)
        self.assertEqual(response.status_code, 201) # 201 Created
        self.assertEqual(response.json()["message"], "Item created successfully")
        self.assertEqual(response.json()["data"], new_item)

        # データが追加されたことを確認
        get_response = requests.get(self.BASE_URL + "/items")
        self.assertIn(new_item, get_response.json()['items'])

    def test_04_put_item(self):
        """'/items/{id}'へのPUTリクエストをテスト"""
        updated_item = {"id": 1, "name": "updated_item1"}
        response = requests.put(self.BASE_URL + "/items/1", json=updated_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"], updated_item)

        # データが更新されたことを確認
        get_response = requests.get(self.BASE_URL + "/items")
        self.assertIn(updated_item, get_response.json()['items'])
        self.assertNotIn({"id": 1, "name": "item1"}, get_response.json()['items'])
    
    def test_05_delete_item(self):
        """'/items/{id}'へのDELETEリクエストをテスト"""
        item_to_delete = {"id": 2, "name": "item2"}
        response = requests.delete(self.BASE_URL + "/items/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Item 2 deleted successfully")

        # データが削除されたことを確認
        get_response = requests.get(self.BASE_URL + "/items")
        self.assertNotIn(item_to_delete, get_response.json()['items'])

    def test_06_not_found(self):
        """存在しないパスへのリクエストをテスト"""
        response = requests.get(self.BASE_URL + "/non_existent_path")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Not Found"})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)