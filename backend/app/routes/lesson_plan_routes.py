from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.schemas.lesson_plan_schema import LessonPlanSchema


from app.services.lesson_plan_service import (
    create_lesson_plan,
    get_all_lesson_plans,
    get_lesson_plan_by_id,
    update_lesson_plan,
    delete_lesson_plan
)


lesson_plan_bp = Blueprint(
    "lesson_plan",
    __name__
)

lesson_plan_schema = LessonPlanSchema()

@lesson_plan_bp.route("/lesson-plans", methods=["POST"])
def create_plan():

    data = request.get_json()

    try:

        validated_data = lesson_plan_schema.load(data)

    except ValidationError as error:

        return jsonify({
            "errors": error.messages
        }), 400

    lesson_plan = create_lesson_plan(validated_data)

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
            "planned_date": lesson_plan.planned_date.strftime("%Y-%m-%d"),
            "discipline": lesson_plan.discipline,
            "contents": lesson_plan.contents,
            "support_resources": lesson_plan.support_resources,
            "tags": lesson_plan.tags,
            "created_at": lesson_plan.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        })

    return jsonify(results), 200


@lesson_plan_bp.route("/lesson-plans/<int:lesson_plan_id>", methods=["GET"])
def get_lesson_plan(lesson_plan_id):

    lesson_plan = get_lesson_plan_by_id(lesson_plan_id)

    if lesson_plan is None:

        return jsonify({
            "message": "Lesson plan not found"
        }), 404

    return jsonify({
        "id": lesson_plan.id,
        "title": lesson_plan.title,
        "objective": lesson_plan.objective,
        "summary": lesson_plan.summary,
        "planned_date": lesson_plan.planned_date.strftime("%Y-%m-%d"),
        "discipline": lesson_plan.discipline,
        "contents": lesson_plan.contents,
        "support_resources": lesson_plan.support_resources,
        "tags": lesson_plan.tags,
        "created_at": lesson_plan.created_at.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }), 200


@lesson_plan_bp.route("/lesson-plans/<int:lesson_plan_id>", methods=["PUT"])
def update_lesson_plan_route(lesson_plan_id):

    data = request.get_json()

    lesson_plan = update_lesson_plan(
        lesson_plan_id,
        data
    )

    if lesson_plan is None:

        return jsonify({
            "message": "Lesson plan not found"
        }), 404

    return jsonify({
        "message": "Lesson plan updated successfully"
    }), 200


@lesson_plan_bp.route("/lesson-plans/<int:lesson_plan_id>", methods=["DELETE"])
def delete_lesson_plan_route(lesson_plan_id):

    lesson_plan = delete_lesson_plan(lesson_plan_id)

    if lesson_plan is None:

        return jsonify({
            "message": "Lesson plan not found"
        }), 404

    return jsonify({
        "message": "Lesson plan deleted successfully"
    }), 200