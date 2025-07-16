from fastapi import APIRouter, Path, Depends,status,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from app.db.database import get_async_session
from app.db.db_models import Students,ParaStand, Parasol, RentalHistory, Parasol, RentalHistory, ParaStand, ParasolStatus
from app.schemas.api_schemas import StudentAuthRequest, CommonResponse, StudentAuthData,RentRequest, ErrorResponse
from fastapi.responses import JSONResponse
from uuid import UUID
from datetime import datetime, timedelta

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

@router.get("/stands/list")
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

@router.post("/parasols/{rfid}/rent")
async def rent_parasol(
    rfid: str = Path(..., description="RFIDタグのID"),
    body: RentRequest = ...,
    session: AsyncSession = Depends(get_async_session)
):
    # 傘が存在して貸出可能か？
    result = await session.execute(
        select(Parasol).where(and_(
            Parasol.rfid_id == rfid,
            Parasol.status == ParasolStatus.available
        ))
    )
    parasol = result.scalar_one_or_none()
    if parasol is None:
        raise HTTPException(status_code=401, detail="貸出可能な傘が見つかりません")

    # 学生確認
    result = await session.execute(
        select(Students).where(Students.student_id == body.studentId)
    )
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=402, detail="学生が見つかりません")

    # すでに傘を借りているか？
    result = await session.execute(
        select(RentalHistory).where(and_(
            RentalHistory.students_id == student.id,
            RentalHistory.returned_at.is_(None)
        ))
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=403, detail="すでに傘を借りています")

    # スタンド確認
    result = await session.execute(
        select(ParaStand).where(ParaStand.id == UUID(body.standId))
    )
    stand = result.scalar_one_or_none()
    if stand is None:
        raise HTTPException(status_code=404, detail="スタンドが見つかりません")

    # ポイント制御（ここではスキップ）

    # 貸出処理
    now = datetime.now()
    due = now + timedelta(days=2)

    rental = RentalHistory(
        id=uuid4(),
        students_id=student.id,
        parasol_id=parasol.id,
        rent_stand_from=stand.id,
        rented_at=now,
        due_at=due
    )
    session.add(rental)

    # 傘の状態を "rented" に更新
    parasol.status = ParasolStatus.rented

    await session.commit()

    # borrowingId を生成（任意のルール、ここではタイムスタンプ）
    borrowing_id = f"BRW_{now.strftime('%Y%m%d%H%M%S')}"

    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
            "status": 202,
            "message": "borrowed",
            "data": {
                "borrowingId": borrowing_id,
                "due": due.strftime("%Y-%m-%dT%H:%M:%S")
            }
        }
    )