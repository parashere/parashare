from fastapi import APIRouter, Path, Depends,status,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc
from app.db.database import get_async_session
from app.db.db_models import Students,ParaStand, Parasol, RentalHistory, Parasol, RentalHistory, ParaStand, ParasolStatus
from app.schemas.api_schemas import StudentAuthRequest, CommonResponse, StudentAuthData, RentRequest, ErrorResponse, RentAvailabilityData, ReturnRequest, LockLogRequest, StandStatusData, MeData
from fastapi.responses import JSONResponse
from uuid import UUID,uuid4
from datetime import datetime, timedelta
from fastapi.logger import logger

router = APIRouter()

@router.post("/students/{student_id}/auth", response_model=CommonResponse)
async def auth_or_register_student(
    student_id: str = Path(..., description="学籍番号"),
    #request: StudentAuthRequest = ...,
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
    
@router.post("/students/{student_id}", response_model=CommonResponse)
async def check_student_can_rent(
    student_id: str = Path(..., description="学籍番号"),
    session: AsyncSession = Depends(get_async_session),
):
    # 1) 学生情報を取得（student_id → UUID）
    res_student = await session.execute(
        select(Students).where(Students.student_id == student_id)
    )
    student = res_student.scalar_one_or_none()
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    # 2) 最新のレンタル履歴を 1 件だけ取得
    res_history = await session.execute(
        select(RentalHistory)
        .where(RentalHistory.students_id == student.id)
        .order_by(desc(RentalHistory.rented_at))
        .limit(1)
    )
    latest = res_history.scalar_one_or_none()
    
    # 3) 履歴が無い、または返却済みなら OK
    if latest is None or latest.returned_at is not None:
        
        availability = RentAvailabilityData(student_id=student_id, can_rent=True)
        
        return CommonResponse(
            status=200,
            message="Can Rent",
            data=availability.model_dump()
        )

    availability = RentAvailabilityData(student_id=student_id, can_rent=False)
    # 4) 返却されていない ⇒ 現在レンタル中なので No
    return CommonResponse(
        
        status=422,
        message="Cannot Rent",
        data=availability.model_dump()
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
    body: RentRequest,
    rfid: str = Path(..., description="RFIDタグ"),
    session: AsyncSession = Depends(get_async_session)
):
    #logger.info(f"受け取ったbody: {body}")
    parasol = await session.execute(
        select(Parasol).where(
            Parasol.rfid_id == rfid,
            Parasol.status == ParasolStatus.available
        )
    )
    parasol = parasol.scalar_one_or_none()
    if not parasol:
        raise HTTPException(status_code=400, detail="unavailable parasol")
    # 学籍番号からUUIDを検索
    result = await session.execute(
        select(Students).where(Students.student_id == body.student_id)
    )
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=401, detail="student not found")

    stand = await session.get(ParaStand, body.stand_id)
    if not stand:
        raise HTTPException(status_code=402, detail="stand not found")

    now = datetime.now()
    due = now + timedelta(days=2)

    rental = RentalHistory(
        id=uuid4(),
        students_id=student.id,
        rent_parasol_id=parasol.id,
        rent_stand_from=stand.id,
        rented_at=now,
        due_at=due
    )
    parasol.status = ParasolStatus.rented

    session.add(rental)
    await session.commit()

    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "message": "Successful umbrella rental",
            "data": {
                "due": due.isoformat()
            }
        }
    )

@router.post("/parasols/{rfid}/return")
async def return_parasol(
    body: ReturnRequest,
    rfid: str = Path(..., description="RFIDタグ"),
    session: AsyncSession = Depends(get_async_session)
):
    # 該当する傘の取得
    result = await session.execute(
        select(Parasol).where(Parasol.rfid_id == rfid)
    )
    parasol = result.scalar_one_or_none()
    if not parasol:
        raise HTTPException(status_code=404, detail="傘が見つかりません")

    # 現在の貸出履歴を取得（返却されていないもの）
    result = await session.execute(
        select(RentalHistory)
        .where(
            RentalHistory.rent_parasol_id == parasol.id,
            RentalHistory.returned_at.is_(None)
        )
        .order_by(RentalHistory.rented_at.desc())  # 念のため最新を優先
        .limit(1)
    )
    rental = result.scalar_one_or_none()
    if not rental:
        raise HTTPException(status_code=404, detail="返却対象の履歴が見つかりません")

    # スタンド確認
    stand = await session.get(ParaStand, body.return_stand_to)
    if not stand:
        raise HTTPException(status_code=404, detail="返却スタンドが見つかりません")

    # 更新処理
    rental.return_stand_to = stand.id
    rental.return_parasol_id = parasol.id
    rental.returned_at = datetime.now()

    parasol.status = ParasolStatus.available

    await session.commit()

    return {"status": "returned", "returned_at": rental.returned_at.isoformat()}
