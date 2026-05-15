from flask import Flask

from app.extensions.extensions import db
from app.routes.main_routes import main_bp
from app.config.config import Config

from app.models.user import User

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main_bp)
    
    return app
