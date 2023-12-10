from models.database import db
from models.ingredient import Ingredient
from flask import jsonify, request
from forms.recipe_register_form import RecipeForm
import sys

def index():
    ingredients = Ingredient.query.all()
    names = [ingredient.name for ingredient in ingredients]
    return jsonify({'suggestions': names})