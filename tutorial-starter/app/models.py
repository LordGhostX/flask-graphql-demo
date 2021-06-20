from datetime import datetime
from app import db
from app.utils import generate_id


class Notes(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.String, primary_key=True, default=generate_id)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    last_updated = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
