from app.models.collector_status import SessionLocal, CollectorStatus
import datetime

def mock_sync(name, url):
    db = SessionLocal()
    status = db.query(CollectorStatus).filter(CollectorStatus.name == name).first()
    if not status:
        status = CollectorStatus(name=name, source_url=url)
        db.add(status)
    status.last_synced_at = datetime.datetime.utcnow()
    status.available_to_chat = True
    status.status = "Success"
    db.commit()
    db.close()

if __name__ == "__main__":
    mock_sync("UN Data", "https://data.un.org/")
    mock_sync("UK Gov Data", "https://data.gov.uk/api/action/package_search")
    mock_sync("UK Trade Tariff", "https://www.trade-tariff.service.gov.uk/api/v2/sections")
    print("Collectors synced.")