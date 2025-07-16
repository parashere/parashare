
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from sqlalchemy import text
from dotenv import load_dotenv
from app.db.database import engine
from app.routes import device
from app.schemas.api_schemas import ErrorResponse


# .env ファイルから環境変数を読み込む
load_dotenv()


app = FastAPI(
    title="Parashare 傘シェアAPI",
    version="1.0.0"
)


app.include_router(device.router)


# テスト用エンドポイント
@app.get("/")
async def root():
    return {"message": "Parashare API is running"}


# 起動時にDB接続をテスト
@app.on_event("startup")
async def startup_event():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1;"))
        print("起動時DB接続に成功")
    except Exception as e:
        print("起動時DB接続に失敗:", e)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder(ErrorResponse(
            status=400,
            error_code="invalid_request",
            message="不正なリクエストです"
        )),
    )