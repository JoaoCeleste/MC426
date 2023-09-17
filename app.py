from flask import Flask
from database.database import db
from database.models import User
from os import environ
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)

    db_name = environ.get('POSTGRES_DB')
    db_user = environ.get('POSTGRES_USER')
    db_password = environ.get('POSTGRES_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"
    app.config["SECRET_KEY"] = "abc"

    db.init_app(app)
	
    login_manager = LoginManager()
    login_manager.init_app(app)
	
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(user_id)

    from routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)