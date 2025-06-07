from pydantic import BaseModel, Field
from typing import Optional

class JobCreateRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, )
    """Request schema for creating a new job in the job queue system."""
    status: Optional[str] = Field(default="queued")
    """Status of the job, default is 'queued'."""
    
    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "name": "Data Processing Job",
                "status": "queued"
            }
        }


class JobUpdateRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, )
    """Request schema for creating a new job in the job queue system."""
    status: Optional[str]

    class Config:
        """Configuration for the Pydantic model."""
        schema_extra = {
            "example": {
                "name": "Data Processing Job",
                "status": "queued"
            }
        }
