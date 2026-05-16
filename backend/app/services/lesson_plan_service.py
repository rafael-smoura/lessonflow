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

def get_lesson_plan_by_id(lesson_plan_id):
    return LessonPlan.query.get(lesson_plan_id)

def update_lesson_plan(lesson_plan_id, data):

    lesson_plan = LessonPlan.query.get(lesson_plan_id)

    if lesson_plan is None:
        return None

    lesson_plan.title = data["title"]
    lesson_plan.objective = data["objective"]
    lesson_plan.summary = data["summary"]
    lesson_plan.subject = data["subject"]

    db.session.commit()

    return lesson_plan

def delete_lesson_plan(lesson_plan_id):

    lesson_plan = LessonPlan.query.get(lesson_plan_id)

    if lesson_plan is None:
        return None

    db.session.delete(lesson_plan)

    db.session.commit()

    return lesson_plan
