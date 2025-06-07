from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = {"schema": "jobs_schema"}  # points to your existing schema/table

    job_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default="queued", nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
