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
    tag=None,
    planned_date=None,
    search=None,
    sort_by="created_at",
    order="desc",
    page=1,
    per_page=5
):
    query = LessonPlan.query

    if discipline:
        query = query.filter_by(discipline=discipline)

    if tag:
        query = query.filter(LessonPlan.tags.ilike(f"%{tag}%"))

    if planned_date:
        query = query.filter(LessonPlan.planned_date == planned_date)

    if search:
        query = query.filter(LessonPlan.title.ilike(f"%{search}%"))

    if sort_by == "title":
        sort_column = LessonPlan.title
    else:
        sort_column = LessonPlan.created_at

    if order == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())


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

    lesson_plan.title = data.get("title", lesson_plan.title)
    lesson_plan.objective = data.get("objective", lesson_plan.objective)
    lesson_plan.summary = data.get("summary", lesson_plan.summary)
    
    lesson_plan.planned_date = data.get("planned_date", lesson_plan.planned_date)
    
    lesson_plan.discipline = data.get("discipline", lesson_plan.discipline)
    lesson_plan.contents = data.get("contents", lesson_plan.contents)
    lesson_plan.support_resources = data.get("support_resources", lesson_plan.support_resources)
    lesson_plan.tags = data.get("tags", lesson_plan.tags)

    db.session.commit()
    return lesson_plan


def delete_lesson_plan(lesson_plan_id):
    lesson_plan = LessonPlan.query.get(lesson_plan_id)

    if lesson_plan is None:
        return None

    db.session.delete(lesson_plan)
    db.session.commit()
    return lesson_plan