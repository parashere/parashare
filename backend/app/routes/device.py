from fastapi import APIRouter, Path, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_async_session
from app.db.db_models import Students
from app.schemas.api_schemas import StudentAuthRequest, CommonResponse, StudentAuthData, ErrorResponse
from fastapi.responses import JSONResponse

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

