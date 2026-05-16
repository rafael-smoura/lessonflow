from app.extensions.extensions import db
from app.models.lesson_plan import LessonPlan


def create_lesson_plan(data):
    lesson_plan = LessonPlan(
        title=data["title"],
        objective=data["objective"],
        summary=data["summary"],
        subject=data["subject"]
    )

    db.session.add(lesson_plan)

    db.session.commit()

    return lesson_plan

def get_all_lesson_plans():
    return LessonPlan.query.all()