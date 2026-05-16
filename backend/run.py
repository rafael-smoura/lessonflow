import os

from app import create_app
from app.extensions.extensions import db
from app.models.user import User
from app.models.lesson_plan import LessonPlan

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 17001))
    app.run(host="0.0.0.0", debug=True, port=port)