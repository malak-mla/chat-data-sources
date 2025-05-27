from sqlalchemy import create_engine, Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///./collectors.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class CollectorStatus(Base):
    __tablename__ = "collector_status"
    name = Column(String, primary_key=True, index=True)
    source_url = Column(String)
    available_to_chat = Column(Boolean, default=False)
    last_synced_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="Unknown")

Base.metadata.create_all(bind=engine)

def get_all_statuses():
    db = SessionLocal()
    statuses = db.query(CollectorStatus).all()
    db.close()
    return [s.__dict__ for s in statuses]