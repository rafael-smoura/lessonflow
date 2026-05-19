import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from app.extensions.extensions import db
from app.routes.auth_routes import auth_bp
from app.models.lesson_plan import LessonPlan
from app.routes.lesson_plan_routes import lesson_plan_bp
from app.config.config import Config
from app.models.user import User

def create_app():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'frontend'),
        static_folder=os.path.join(base_dir, 'frontend'),
        static_url_path=''
    )

    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    
    @app.route('/')
    def serve_frontend():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/api/health')
    def health_check():
        return jsonify({
            "status": "healthy", 
            "message": "LessonFlow API is running successfully"
        }), 200

    app.register_blueprint(auth_bp)
    app.register_blueprint(lesson_plan_bp)
    
    return app