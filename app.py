from flask import Flask
from models.database import db
from models.user import User
from os import environ
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect


def create_app(env='DEVELOPMENT'):
    """
    Create and configure the Flask application.

    This function initializes the Flask app, sets up configurations based on the environment,
    initializes the database, sets up user authentication, registers blueprints for routes,
    and configures additional extensions like migration and CSRF protection.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__, template_folder='views')

    if env == 'DEVELOPMENT':
        app.config.from_object('config.development')
    elif env == 'TESTING':
        app.config.from_object('config.testing')
    try:
        db.init_app(app)

        login_manager = LoginManager()
        login_manager.init_app(app)

        @login_manager.user_loader
        def loader_user(user_id):
            return User.query.get(user_id)

        from routes.routes import routes
        app.register_blueprint(routes)

        import models
        with app.app_context():
            db.create_all()

        migrate = Migrate(app, db)
        bootstrap = Bootstrap5(app)
        if not env == 'TESTING':
            csrf = CSRFProtect(app)

        return app
    except Exception as e:
        print(f"Error creating the app: {e}")


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
