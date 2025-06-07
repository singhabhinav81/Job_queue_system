from app.db.session import SessionLocal
from sqlalchemy.orm import Session


def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use
# This function is used as a dependency in FastAPI routes to provide a database session.
# It ensures that the session is properly closed after the request is processed.
# This helps to prevent connection leaks and ensures that the database session is managed correctly.
# The `get_db` function is typically used in FastAPI route handlers to provide a database session.
# It uses the `SessionLocal` from the session module to create a new session.   