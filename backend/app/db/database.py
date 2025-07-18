from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from typing import AsyncGenerator
import os

load_dotenv()

# 環境変数から接続情報を取得
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy エンジンとセッションのセットアップ
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Base クラス（モデル定義で使う）
Base = declarative_base()

# セッション取得
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
