from fastapi import APIRouter, Depends, HTTPException
from app.model.job_response import JobListResponse, JobResponse
from app.model.job_request import JobCreateRequest
from datetime import datetime
from app.db.models import Job
from app.db.deps import get_db
from sqlalchemy.orm import Session
from app.core.logger import logger

# This module defines the API routes for the job queue system.
# It includes endpoints for job management, such as retrieving all jobs.    

router = APIRouter()

@router.get("/")
async def root():
    """
    Root endpoint for the Job Queue System API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the Job Queue System API!"}


@router.get("/jobs", response_model=JobListResponse)
async def get_all_jobs(
    skip: int = 0,
    limit: int = 100,   # Pagination parameters for job retrieval
    status: str = None,  # Optional filter for job status
    name: str = None,  # Optional filter for job name
    db: Session=Depends(get_db)
    ):
    """
    Args:
        skip (int): Number of jobs to skip for pagination.
        limit (int): Maximum number of jobs to return.
        status (str): Optional filter to retrieve jobs by status.
        name (str): Optional filter to retrieve jobs by name.
        db (Session): The database session dependency.
    Returns:
        List[JobResponse]: A list of job details.
    """
    if status:
        query = db.query(Job).filter(Job.status == status)
    elif name:
        query = db.query(Job).filter(Job.name == name)
    else:
        query = db.query(Job)
    jobs = query.offset(skip).limit(limit).all()
    total = query.count()  # Get the total count of jobs matching the query
    
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    # Convert the list of Job ORM objects to JobResponse Pydantic models

    return JobListResponse(
        total=total,
        jobs=[JobResponse(
            job_id=job.job_id,
            name=job.name,
            status=job.status,
            created_at=job.created_at,
            updated_at=job.updated_at
        ) for job in jobs]
    ) 


@router.get("/jobs/{job_id}")
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a job by its ID.
    Args:
        job_id (int): The ID of the job to retrieve.
        db (Session): The database session dependency.
    Returns:
        dict: A dictionary containing job details.
    Raises:
        HTTPException: If the job with the specified ID does not exist.
    """
    job = db.query(Job).filter(Job.job_id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobResponse(
        job_id=job.job_id,
        name=job.name,
        status=job.status,
        created_at=job.created_at,
        updated_at=job.updated_at
    )

@router.post("/jobs", response_model=JobResponse)
def create_job(job_data: JobCreateRequest, db: Session = Depends(get_db)):
    logger.info(f"Creating job with name: {job_data.name} and status: {job_data.status}")
    job = Job(
        name=job_data.name,
        status=job_data.status
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    logger.info(f"Job created with ID: {job.job_id}")
    return job


@router.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job_data: JobCreateRequest, db: Session = Depends(get_db)):
    """
    Endpoint to update a job by its ID.
    Args:
        job_id (int): The ID of the job to update.
        job_data (JobCreateRequest): The data to update the job with.
        db (Session): The database session dependency.
    Returns:
        JobResponse: The updated job details.
    Raises:
        HTTPException: If the job with the specified ID does not exist.
    """
    logger.info(f"Updating job with ID: {job_id}")
    job = db.query(Job).filter(Job.job_id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job_data.name is not None:
        job.name = job_data.name
    if job_data.status is not None:
        job.status = job_data.status
    
    db.commit()
    db.refresh(job)
    logger.info(f"Job with ID: {job_id} updated successfully")
    return job

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a job by its ID.
    Args:
        job_id (int): The ID of the job to delete.
        db (Session): The database session dependency.
    Returns:
        dict: A confirmation message.
    Raises:
        HTTPException: If the job with the specified ID does not exist.
    """
    job = db.query(Job).filter(Job.job_id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}