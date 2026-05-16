from app.extensions import db


class LessonPlan(db.Model):
    __tablename__ = "lesson_plans"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)

    objective = db.Column(db.Text, nullable=False)

    summary = db.Column(db.Text, nullable=False)

    subject = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text)

    support_resources = db.Column(db.Text)

    tags = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )