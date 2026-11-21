

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from izutsu.config import DATABASE_URL, initialize_directories


initialize_directories()

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)


@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_session():
    """Return a new database session."""

    return SessionLocal()
