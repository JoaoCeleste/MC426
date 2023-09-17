from database import db

class User(db.Model):
    __tablename__ = 'user_'

    id = db.Column(db.Integer, primary_key = True)


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key = True)