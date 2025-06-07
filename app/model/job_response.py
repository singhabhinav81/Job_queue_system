#This defines a response schema called JobResponse.
#FastAPI uses this to format the response body when returning job data.
from pydantic import BaseModel
from datetime import datetime
from typing import List

class JobResponse(BaseModel):
    """Response schema for a job in the job queue system.""" 
    job_id: int
    name: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        """Configuration for the Pydantic model."""
        # Enable ORM mode to allow compatibility with ORM models
        orm_mode = True

class JobListResponse(BaseModel):
    total: int
    jobs: List[JobResponse]