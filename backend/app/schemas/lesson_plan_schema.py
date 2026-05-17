from marshmallow import Schema, fields


class LessonPlanSchema(Schema):

    title = fields.String(required=True)

    objective = fields.String(required=True)

    summary = fields.String(required=True)

    planned_date = fields.Date(required=True)

    discipline = fields.String(required=True)

    contents = fields.String(required=True)

    support_resources = fields.String(required=False)

    tags = fields.String(required=False)