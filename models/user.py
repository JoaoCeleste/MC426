from models.database import db
from flask_login import UserMixin


user_recipe = db.Table('user_recipe',
                       db.Column('user_id', db.Integer, db.ForeignKey('user_.id')),
                       db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')))

class User(db.Model, UserMixin):
    __tablename__ = 'user_'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    recipes = db.relationship('Recipe', secondary=user_recipe, backref='users')
