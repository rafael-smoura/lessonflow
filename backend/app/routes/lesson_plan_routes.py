from flask import Blueprint, request, jsonify


from app.services.lesson_plan_service import (
    create_lesson_plan,
    get_all_lesson_plans
)


lesson_plan_bp = Blueprint(
    "lesson_plan",
    __name__
)


@lesson_plan_bp.route("/lesson-plans", methods=["POST"])
def create_plan():
    data = request.get_json()

    lesson_plan = create_lesson_plan(data)

    return jsonify({
        "message": "Lesson plan created successfully",
        "id": lesson_plan.id
    }), 201


@lesson_plan_bp.route("/lesson-plans", methods=["GET"])
def get_lesson_plans():

    lesson_plans = get_all_lesson_plans()

    results = []

    for lesson_plan in lesson_plans:
        results.append({
            "id": lesson_plan.id,
            "title": lesson_plan.title,
            "objective": lesson_plan.objective,
            "summary": lesson_plan.summary,
            "subject": lesson_plan.subject
        })

    return jsonify(results), 200