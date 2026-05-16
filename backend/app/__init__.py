from flask import Flask

from app.extensions.extensions import db
from app.routes.main_routes import main_bp
from app.routes.auth_routes import auth_bp
from app.models.lesson_plan import LessonPlan

from app.config.config import Config

from app.models.user import User

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    
    return app
