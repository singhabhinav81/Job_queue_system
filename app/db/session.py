from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.core.config import get_database_url

# Create a SQLAlchemy engine
engine = create_engine(get_database_url(), echo=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Create a configured "Session" class
