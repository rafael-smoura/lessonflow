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

from app.ai.lesson_plan_ai import (
    generate_lesson_plan_recommendations
)

lesson_plan_bp = Blueprint(
    "lesson_plan",
    __name__
)

lesson_plan_schema = LessonPlanSchema()
lesson_plans_schema = LessonPlanSchema(many=True)


@lesson_plan_bp.route("/lesson-plans", methods=["POST"])
def create_plan():
    data = request.get_json()

    try:
        validated_data = lesson_plan_schema.load(data)
    except ValidationError as error:
        return jsonify({
            "errors": error.messages
        }), 400

    ai_data = generate_lesson_plan_recommendations(
        validated_data["title"],
        validated_data["discipline"],
        validated_data["summary"]
    )

    validated_data["contents"] = validated_data.get("contents") or ai_data.get("contents", "")
    validated_data["support_resources"] = validated_data.get("support_resources") or ai_data.get("support_resources", "")
    validated_data["tags"] = validated_data.get("tags") or ai_data.get("tags", "")

    lesson_plan = create_lesson_plan(validated_data)

    return jsonify({
        "message": "Lesson plan created successfully",
        "data": lesson_plan_schema.dump(lesson_plan)
    }), 201


@lesson_plan_bp.route("/lesson-plans", methods=["GET"])
def get_lesson_plans():
    # Parâmetros dinâmicos de filtragem e busca [cite: 19, 20]
    discipline = request.args.get("discipline")
    tag = request.args.get("tag")
    planned_date = request.args.get("planned_date")
    search = request.args.get("search")

    # Parâmetros dinâmicos de ordenação [cite: 21]
    sort_by = request.args.get("sort_by", "created_at") 
    order = request.args.get("order", "desc")           

    # Parâmetros de paginação [cite: 10]
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    # Executa a busca estruturada
    lesson_plans = get_all_lesson_plans(
        discipline=discipline,
        tag=tag,
        planned_date=planned_date,
        search=search,
        sort_by=sort_by,
        order=order,
        page=page,
        per_page=per_page
    )

    return jsonify({
        "page": lesson_plans.page,
        "per_page": lesson_plans.per_page,
        "total": lesson_plans.total,
        "pages": lesson_plans.pages,
        "data": lesson_plans_schema.dump(lesson_plans.items)
    }), 200


@lesson_plan_bp.route("/lesson-plans/<int:lesson_plan_id>", methods=["GET"])
def get_lesson_plan(lesson_plan_id):
    lesson_plan = get_lesson_plan_by_id(lesson_plan_id)

    if lesson_plan is None:
        return jsonify({
            "message": "Lesson plan not found"
        }), 404

    return jsonify(
        lesson_plan_schema.dump(lesson_plan)
    ), 200


@lesson_plan_bp.route("/lesson-plans/<int:lesson_plan_id>", methods=["PUT"])
def update_lesson_plan_route(lesson_plan_id):
    data = request.get_json()

    try:
        validated_data = lesson_plan_schema.load(
            data,
            partial=True
        )
    except ValidationError as error:
        return jsonify({
            "errors": error.messages
        }), 400

    lesson_plan = update_lesson_plan(
        lesson_plan_id,
        validated_data
    )

    if lesson_plan is None:
        return jsonify({
            "message": "Lesson plan not found"
        }), 404

    return jsonify({
        "message": "Lesson plan updated successfully",
        "data": lesson_plan_schema.dump(lesson_plan)
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


@lesson_plan_bp.route("/lesson-plans/ai-recommendations", methods=["POST"])
def generate_ai_recommendations():
    data = request.get_json()

    title = data.get("title")
    discipline = data.get("discipline")
    summary = data.get("summary")

    if not title or not discipline or not summary:
        return jsonify({
            "message": "title, discipline and summary are required"
        }), 400

    try:
        recommendations = generate_lesson_plan_recommendations(
            title,
            discipline,
            summary
        )

        return jsonify({
            "message": "AI recommendations generated successfully",
            "data": recommendations
        }), 200

    except Exception as error:
        return jsonify({
            "message": "AI generation failed",
            "error": str(error)
        }), 500

