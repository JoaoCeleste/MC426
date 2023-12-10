from models.recipe import Recipe, RecipeIngredient
from models.ingredient import Ingredient
from flask import render_template, request, url_for, redirect
from forms.recipe_register_form import RecipeForm
from models.database import db

def new():
    return render_template("recipe_register.html", form=RecipeForm())

def create():
    form = RecipeForm(request.form)

    if form.validate_on_submit():
        recipe = Recipe(name=form.name.data, instruction=form.instruction.data)
        db.session.add(recipe)
        db.session.flush()

        for ingredient_data in form.ingredients.data:
            name = ingredient_data['ingredient_name']
            quantity = ingredient_data['quantity']

            ingredient = Ingredient.query.filter(Ingredient.name == name).first()
            if ingredient:
                recipe_ingredient = RecipeIngredient(
                    recipe_id = recipe.id,
                    ingredient_id = ingredient.id,
                    quantity = quantity)
                db.session.add(recipe_ingredient)

        db.session.commit()

        return redirect(url_for('routes.recipe_new'))
    print(form.errors)
    return render_template("recipe_register.html", form = form)