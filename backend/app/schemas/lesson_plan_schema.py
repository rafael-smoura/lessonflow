from marshmallow import Schema, fields


class LessonPlanSchema(Schema):

    id = fields.Int(dump_only=True)

    title = fields.Str(required=True)

    objective = fields.Str(required=True)

    summary = fields.Str(required=True)

    planned_date = fields.Date(required=True)

    discipline = fields.Str(required=True)

    contents = fields.Str(required=False)

    support_resources = fields.Str(required=False)

    tags = fields.Str(required=False)

    created_at = fields.DateTime(dump_only=True)