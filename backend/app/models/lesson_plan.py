from datetime import datetime

from app.extensions.extensions import db


class LessonPlan(db.Model):

    __tablename__ = "lesson_plans"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    objective = db.Column(db.Text, nullable=False)

    summary = db.Column(db.Text, nullable=False)

    planned_date = db.Column(db.Date, nullable=False)

    discipline = db.Column(db.String(100), nullable=False)

    contents = db.Column(db.Text, nullable=False)

    support_resources = db.Column(db.Text, nullable=True)

    tags = db.Column(db.String(200), nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )