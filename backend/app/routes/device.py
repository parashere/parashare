from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_async_session
from app.db.db_models import Students
from app.schemas.api_schemas import StudentAuthRequest, CommonResponse, StudentAuthData, ErrorResponse

router = APIRouter()

@router.post("/students/{student_id}/auth", response_model=CommonResponse)
async def register_or_auth_student(
    student_id: str = Path(..., description="学籍番号"),
    request: StudentAuthRequest = ...,
    session: AsyncSession = Depends(get_async_session)
):
    # 学籍番号がすでに登録されているか確認
    query = select(Students).where(Students.student_id == student_id)
    result = await session.execute(query)
    student = result.scalar_one_or_none()

    # 学籍番号が存在しない場合 → 新規登録
    if student is None:
        new_student = Students(
            student_id=student_id,
            card_id=request.card_id
        )
        session.add(new_student)
        await session.commit()
        await session.refresh(new_student)

        return CommonResponse(
            message="新しい学生情報を登録しました",
            data=StudentAuthData(student_id=new_student.student_id)
        )

    # 学籍番号とカードIDが一致している → 認証成功
    return CommonResponse(
        message="認証成功",
        data=StudentAuthData(student_id=student.student_id)
    )

