from flask import Flask
from database import db
from models import User
from os import environ

def create_app():
    app = Flask(__name__)

    db_name = environ.get('POSTGRES_DB')
    db_user = environ.get('POSTGRES_USER')
    db_password = environ.get('POSTGRES_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"

    db.init_app(app)

    from routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)