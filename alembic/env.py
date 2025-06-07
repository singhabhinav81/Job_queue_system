# to something like this:
from app.db.base import Base
from app.db.session import engine  # your DB engine
target_metadata = Base.metadata
