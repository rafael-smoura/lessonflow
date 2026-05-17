from datetime import datetime

from app.extensions.extensions import db
from app.models.lesson_plan import LessonPlan


def create_lesson_plan(data):

    lesson_plan = LessonPlan(
        title=data["title"],
        objective=data["objective"],
        summary=data["summary"],
        planned_date=data["planned_date"],
        discipline=data["discipline"],
        contents=data["contents"],
        support_resources=data["support_resources"],
        tags=data["tags"]
    )

    db.session.add(lesson_plan)

    db.session.commit()

    return lesson_plan


def get_all_lesson_plans(
    discipline=None,
    search=None,
    page=1,
    per_page=5
):

    query = LessonPlan.query

    if discipline:

        query = query.filter_by(
            discipline=discipline
        )

    if search:

        query = query.filter(
            LessonPlan.title.ilike(f"%{search}%")
        )

    paginated_lesson_plans = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return paginated_lesson_plans


def get_lesson_plan_by_id(lesson_plan_id):
    return LessonPlan.query.get(lesson_plan_id)


def update_lesson_plan(lesson_plan_id, data):

    lesson_plan = LessonPlan.query.get(lesson_plan_id)

    if lesson_plan is None:
        return None

    lesson_plan.title = data["title"]

    lesson_plan.objective = data["objective"]

    lesson_plan.summary = data["summary"]

    lesson_plan.planned_date = datetime.strptime(
        data["planned_date"],
        "%Y-%m-%d"
    ).date()

    lesson_plan.discipline = data["discipline"]

    lesson_plan.contents = data["contents"]

    lesson_plan.support_resources = data["support_resources"]

    lesson_plan.tags = data["tags"]

    db.session.commit()

    return lesson_plan


def delete_lesson_plan(lesson_plan_id):

    lesson_plan = LessonPlan.query.get(lesson_plan_id)

    if lesson_plan is None:
        return None

    db.session.delete(lesson_plan)

    db.session.commit()

    return lesson_plan