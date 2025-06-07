# This script tests the database connection by creating a session and executing a simple query.
# If the connection is successful, it prints a success message; otherwise, it prints the error.
# Ensure the session is closed after the test to avoid connection leaks.
# This script is intended to be run directly to test the database connection.                   

from app.db.session import SessionLocal
from sqlalchemy import text


def test_database_connection():
    """Test the database connection."""
    try:
        # Attempt to create a session
        db = SessionLocal()
        # Execute a simple query to check the connection
        db.execute(text("SELECT * from jobs_schema.jobs LIMIT 1"))
        db.commit()
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        db.close()  # Ensure the session is closed after the test


if __name__ == "__main__":
    test_database_connection()