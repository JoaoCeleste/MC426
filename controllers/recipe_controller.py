from models.recipe import Recipe, RecipeIngredient
from models.ingredient import Ingredient
from flask import render_template, request, url_for, redirect, abort
from forms.recipe_register_form import RecipeForm
from forms.recipe_search_form import RecipeSearchByIngredientsForm, RecipeSearchByNameForm
from models.database import db
from sqlalchemy import or_
from flask_login import current_user



def index():
    recipes = request.args.getlist('recipes')
    recipesOut = []
    for recipe in recipes:
        recipe = Recipe.query.get(recipe)
        if recipe is not None:
            recipesOut.append(recipe)

    return render_template("recipe_index.html", recipes=recipesOut)

def show(id):
    return abort(400)

def new():
    if not current_user.is_authenticated or not current_user.is_admin:
        return abort(403)
    return render_template("recipe_register.html", form=RecipeForm())

def create():
    if not current_user.is_authenticated or not current_user.is_admin:
        return abort(403)
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
    return render_template("recipe_register.html", form = form)

def search():
    recipeForm = RecipeSearchByNameForm(request.args)
    ingredientsForm = RecipeSearchByIngredientsForm(request.args)
    recipes = []
    if recipeForm.name.data:
        names = recipeForm.name.data.split()

        query_conditions = [Recipe.name.ilike(f"%{term}%") for term in names]
        dynamic_query = or_(*query_conditions)

        recipes = Recipe.query.filter(dynamic_query).all()
        if recipes:
            recipes = [Recipe.id for Recipe in Recipe.query.filter(dynamic_query).all()]
        else:
            recipes = []
    elif ingredientsForm.ingredients.data:
        ingredients = ingredientsForm.ingredients.data
        ingredients = [Ingredient.query.filter(Ingredient.name == ingredient).first() for ingredient in ingredients]

        freq = {}
        for ingredient in ingredients:
            if ingredient is None:
                break
            recipes = [Recipe.query.get(recipe_ingredient.recipe_id) for recipe_ingredient in RecipeIngredient.query.filter(RecipeIngredient.ingredient_id == ingredient.id).all()]
            for recipe in recipes:
                if recipe.id in freq:
                    freq[recipe.id] += 1
                else:
                    freq[recipe.id] = 1

        recipes = [key for key, item in sorted(freq.items(), key = lambda x : x[1], reverse=True)]

    return redirect(url_for('routes.recipe_index', recipes=recipes))