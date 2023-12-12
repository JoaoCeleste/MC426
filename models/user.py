from models.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user_'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    admin = db.Column(db.Integer, default=0)

    @property
    def is_admin(self):
        return self.admin