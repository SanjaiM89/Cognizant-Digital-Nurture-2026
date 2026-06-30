from flask import Flask
from config import config
from courses.routes import courses_bp
from courses.models import db
def create_app():
    app = Flask(__name__)
    
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(courses_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run()