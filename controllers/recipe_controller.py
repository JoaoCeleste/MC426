from models.recipe import Recipe
from flask import render_template, request, url_for, redirect
from forms.recipe_register_form import RecipeForm

def create():
    return render_template("recipe_register.html", form=RecipeForm())