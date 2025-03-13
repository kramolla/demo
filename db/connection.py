from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql+psycopg://postgres:123456@localhost:5432/test"
Base = declarative_base()
engine = create_engine(db_url)
session_local = sessionmaker(bind=engine)
session = session_local()