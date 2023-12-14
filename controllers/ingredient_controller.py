from models.database import db
from models.ingredient import Ingredient, IngredientInformation
from flask import jsonify, render_template, request, url_for, redirect, abort
from forms.ingredient_register_form import IngredientForm
from facade.user_facade import UserFacade

user_facade = UserFacade()

def index():
    ingredients = Ingredient.query.all()
    names = [ingredient.name for ingredient in ingredients]
    return jsonify({'suggestions': names})

  
def show(id):
    ingredient = Ingredient.query.get(id)
    ingredient_information = IngredientInformation.query.filter(IngredientInformation.ingredient_id == id).first()
    recipes_with_ingredient = [assoc.recipe for assoc in ingredient.recipes]
    if ingredient == None:
        return user_facade.home()
    return render_template("ingredient.html", ingredient=ingredient, info=ingredient_information, recipes=recipes_with_ingredient)


def new():
    if not user_facade.is_admin():
        return user_facade.home()
    return render_template("ingredient_register.html", form=IngredientForm())


def create():
    if not user_facade.is_admin():
        return user_facade.home()
    form = IngredientForm(request.form)

    if form.validate_on_submit():
        ingredient = Ingredient(name=form.ingredient_name.data)
        db.session.add(ingredient)
        db.session.flush()
        ingredient_information = IngredientInformation(
            ingredient_id=ingredient.id, calories=form.calories.data, proteins=form.proteins.data, fats=form.fats.data, carbohydrates=form.carbohydrates.data)
        db.session.add(ingredient_information)
        db.session.flush()
        db.session.commit()

        return redirect(url_for('routes.ingredients_new'))
    return render_template("ingredient_register.html", form=form)
