from fastapi import APIRouter, Path, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.db.database import get_async_session
from app.db.db_models import Students,ParaStand, Parasol, RentalHistory
from app.schemas.api_schemas import StudentAuthRequest, CommonResponse, StudentAuthData, ErrorResponse
from fastapi.responses import JSONResponse
from uuid import UUID

router = APIRouter()

@router.post("/students/{student_id}/auth", response_model=CommonResponse)
async def auth_or_register_student(
    student_id: str = Path(..., description="学籍番号"),
    request: StudentAuthRequest = ...,
    session: AsyncSession = Depends(get_async_session)
):
    # 学生情報を検索
    query = select(Students).where(Students.student_id == student_id)
    result = await session.execute(query)
    student = result.scalar_one_or_none()

    if student is None:
        # 見つからない場合、登録
        new_student = Students(student_id=student_id)
        session.add(new_student)
        await session.commit()
        await session.refresh(new_student)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=CommonResponse(
                status=201,
                message="New Registration Successful",
                data=StudentAuthData(valid=True, student_id=new_student.student_id).dict()
            ).dict()
        )

    # 見つかった場合、認証成功
    return CommonResponse(
        status=200,
        message="Authentication Successful",
        data=StudentAuthData(valid=True, student_id=student.student_id).dict()
    )

@router.get("/stands")
async def get_stand_list(session: AsyncSession = Depends(get_async_session)):
    # 全スタンド取得
    result = await session.execute(select(ParaStand))
    stands = result.scalars().all()

    stand_list = []
    for stand in stands:
        # このスタンドに現在置かれている傘の数（＝まだ返却されていないレンタル履歴の傘を除いた数）
        subquery = select(func.count()).select_from(RentalHistory).where(
            (RentalHistory.return_stand_to == stand.id)
        )
        result = await session.execute(subquery)
        available_count = result.scalar()

        stand_list.append({
            "standId": str(stand.id),
            "name": stand.location,
            "available": available_count,
        })

    return JSONResponse(status_code=200, content={"status": 200, "data": stand_list})