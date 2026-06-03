from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql+psycopg2://postgres:May112002@localhost:5432/sentineliq_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    event_type = Column(String)
    ip_address = Column(String)
    time = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)