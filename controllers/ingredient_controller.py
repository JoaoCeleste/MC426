from models.database import db
from models.ingredient import Ingredient, IngredientInformation
from flask import jsonify, render_template, request, url_for, redirect, abort
from forms.ingredient_register_form import IngredientForm
from flask_login import current_user
from facade.user_facade import UserFacade

user_facade = UserFacade()

def index():
    ingredients = Ingredient.query.all()
    names = [ingredient.name for ingredient in ingredients]
    return jsonify({'suggestions': names})

def new():
    if not user_facade.is_admin():
        return user_facade.home()
    return render_template("ingredient_register.html", form=IngredientForm())

def create():
    if not user_facade.is_admin():
        return user_facade.home()
    form = IngredientForm(request.form)

    if form.validate_on_submit():
        print(form.ingredient_name.data)
        ingredient = Ingredient(name=form.ingredient_name.data)
        db.session.add(ingredient)
        db.session.flush()
        ingredient_information = IngredientInformation(ingredient_id=ingredient.id, calories=form.calories.data, proteins=form.proteins.data, fats=form.fats.data, carbohydrates=form.carbohydrates.data)
        db.session.add(ingredient_information)
        db.session.flush()
        db.session.commit()

        return redirect(url_for('routes.ingredients_new'))
    print(form.errors)
    return render_template("ingredient_register.html", form = form)
