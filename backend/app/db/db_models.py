import uuid
import enum
from sqlalchemy import (
    Column, String, TIMESTAMP, ForeignKey, Enum, func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ENUM: Parasol Status ---------------------------------
class ParasolStatus(str, enum.Enum):
    available   = "available"
    rented      = "rented"
    maintenance = "maintenance"
    lost        = "lost"

# Students ---------------------------------------------
class Students(Base):
    __tablename__ = "students"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(String(16), unique=True, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

# Parasol ----------------------------------------------
class Parasol(Base):
    __tablename__ = "parasol"

    id       = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rfid_id  = Column(String(32), unique=True, nullable=False)
    status   = Column(
        Enum(
            ParasolStatus,
            name="parasol_status",   # 既存 TYPE 名と合わせる
            create_type=False        # 既に存在する ENUM を再作成しない
        ),
        nullable=False,
    )
    added_at   = Column(TIMESTAMP(timezone=True), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

# ParaStand --------------------------------------------
class ParaStand(Base):
    __tablename__ = "para_stand"

    id       = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version  = Column(String(16), nullable=False)
    location = Column(String(64), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

# RentalHistory ----------------------------------------
class RentalHistory(Base):
    __tablename__ = "rental_history"

    id                = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    students_id       = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)

    rent_parasol_id   = Column(UUID(as_uuid=True), ForeignKey("parasol.id"), nullable=False)
    return_parasol_id = Column(UUID(as_uuid=True), ForeignKey("parasol.id"), nullable=True)

    rent_stand_from   = Column(UUID(as_uuid=True), ForeignKey("para_stand.id"), nullable=False)
    return_stand_to   = Column(UUID(as_uuid=True), ForeignKey("para_stand.id"), nullable=True)

    rented_at   = Column(TIMESTAMP(timezone=True), nullable=False)
    due_at      = Column(TIMESTAMP(timezone=True), nullable=False)
    returned_at = Column(TIMESTAMP(timezone=True), nullable=True)

    created_at  = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at  = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )
