from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from uuid import UUID
from datetime import datetime

# 共通レスポンス（成功時）
class CommonResponse(BaseModel):
    status: int = Field(..., example=200)
    message: str = Field(..., example="成功")
    data: Optional[dict] = None  # 実際の中身はresponse_modelで上書き

# エラーレスポンス（詳細つき）
class ErrorResponse(BaseModel):
    status: int = Field(..., example=400)
    error_code: str = Field(..., example="points_negative")
    message: str = Field(..., example="ポイントが不足しています")

# 学生証リクエスト
class StudentAuthRequest(BaseModel):
    card_id: str = Field(..., description="スタンドで読み取ったNFCカードID", example="04A224B63C1E80")

# 学生認証レスポンス
class StudentAuthData(BaseModel):
    valid: bool = Field(..., description="カードIDが有効か", example=True)
    student_id: Optional[str] = Field(..., description="UUID形式の学生ID", example="c7fb8b5e-3d03-4b2e-9e31-de2b1e6f2e7a")

# ポイント情報
class PointData(BaseModel):
    points: int = Field(..., example=350)

# 傘の貸出リクエスト
class RentRequest(BaseModel):
    stand_id: str = Field(..., example="ST01")
    student_id: str = Field(..., example="c7fb8b5e-3d03-4b2e-9e31-de2b1e6f2e7a")

# 返却リクエスト
class ReturnRequest(BaseModel):
    stand_id: str = Field(..., example="ST02")

# 鍵操作リクエスト
class LockLogRequest(BaseModel):
    stand_id: str
    lock_id: str
    status: Literal["opened", "closed"]
    timestamp: datetime = Field(..., example="2025-07-15T01:23:45+09:00")

# スタンドの状態
class StandStatusData(BaseModel):
    stand_id: str
    location: str
    capacity: int
    available: int

# 自分情報（ポイント含む）
class MeData(BaseModel):
    student_id: str
    points: int

# 現在の貸出状況
class RentalStatusData(BaseModel):
    active: bool
    borrowed_at: Optional[datetime]
    due_at: Optional[datetime]
    stand_id: Optional[str]

# 過去の貸出履歴アイテム
class RentalHistoryItem(BaseModel):
    parasol_id: str
    rent_stand_from: str
    return_stand_to: Optional[str]
    rented_at: datetime
    returned_at: Optional[datetime]

# 貸出履歴一覧
class RentalHistoryData(BaseModel):
    __root__: List[RentalHistoryItem]

# 鍵開閉操作
class LockOperationRequest(BaseModel):
    action: Literal["open", "close"]

# ポイント操作
class PointOperationRequest(BaseModel):
    delta: int = Field(..., description="正の値で加算、負の値で減算")
    reason: Optional[str] = Field(None, description="理由（任意）")
