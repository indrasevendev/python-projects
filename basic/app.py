from flask import Flask
from .config import Config
from .database import db
from .routes.task_routes import task_bp
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .routes.auth_routes import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_bp)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(debug=True)
