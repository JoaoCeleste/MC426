from models.database import db
from models.ingredient import Ingredient
from flask import jsonify, request
from forms.recipe_register_form import RecipeForm
from flask_login import current_user

def index():
    if not current_user.is_authenticated or not current_user.is_admin:
        return abort(403)
    ingredients = Ingredient.query.all()
    names = [ingredient.name for ingredient in ingredients]
    return jsonify({'suggestions': names})