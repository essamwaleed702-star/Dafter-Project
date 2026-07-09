from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker  

DATABASE_URL = "sqlite:///./User.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False ,
    autocommit=False ,
    bind = engine
)



def get_db():
    session = SessionLocal()
    try:
        yield session 
    finally:
        session.close()
        