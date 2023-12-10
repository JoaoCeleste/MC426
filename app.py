from flask import Flask
from models.database import db
from models.user import User
from os import environ
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5


def create_app(env='DEVELOPMENT'):
    app = Flask(__name__, template_folder='views')

    if env == 'DEVELOPMENT':
        app.config.from_object('config.development')
    elif env == 'TESTING':
        app.config.from_object('config.testing')

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

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
