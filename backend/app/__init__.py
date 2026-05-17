from flask import Flask

from flask_cors import CORS
from app.extensions.extensions import db
from app.routes.main_routes import main_bp
from app.routes.auth_routes import auth_bp
from app.models.lesson_plan import LessonPlan
from app.routes.lesson_plan_routes import lesson_plan_bp

from app.config.config import Config

from app.models.user import User

def create_app():
    app = Flask(__name__)

    # 2. Habilita o CORS para permitir acessos vindos do frontend
    CORS(app)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(lesson_plan_bp)
    
    
    return app
