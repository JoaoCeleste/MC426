from models.database import db


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class IngredientInformation(db.Model):
    __tablename__ = 'ingredient_information'

    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    calories = db.Column(db.Float, nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)

