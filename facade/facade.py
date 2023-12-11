from models.database import db
from models.user import User
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

db = SQLAlchemy()

class Facade:
    def register_user(self, username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
    
    def login_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user is not None and user.password == password:
            login_user(user)
            return True
        return False
    
    def logout_user(self):
        logout_user()
    
    def get_user(self, user_id):
        return User.query.get(user_id)
    
    def get_recipe_by_id(self, recipe_id):
        return Recipe.query.get(recipe_id)
    
    def calculate_macronutrients_for_recipe(self, recipe_id):
        recipe = self.get_recipe_by_id(recipe_id)
        if not recipe:
            return None

        recipe_ingredients = RecipeIngredient.query.filter_by(recipe_id=recipe_id).all()

        total_calories = 0
        total_proteins = 0
        total_fats = 0
        total_carbohydrates = 0

        for recipe_ingredient in recipe_ingredients:
            ingredient_id = recipe_ingredient.ingredient_id
            quantity = recipe_ingredient.quantity

            ingredient_info = IngredientInformation.query.filter_by(ingredient_id=ingredient_id).first()

            if ingredient_info:
                total_calories += ingredient_info.calories * quantity
                total_proteins += ingredient_info.proteins * quantity
                total_fats += ingredient_info.fats * quantity
                total_carbohydrates += ingredient_info.carbohydrates * quantity

        macronutrients = {
            'total_calories': total_calories,
            'total_proteins': total_proteins,
            'total_fats': total_fats,
            'total_carbohydrates': total_carbohydrates
        }

        return macronutrients

routes = Blueprint('routes', __name__)

facade = Facade()

@routes.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        facade.register_user(username, password)
        return redirect(url_for("routes.login"))
    return render_template("sign_up.html")

@routes.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if facade.login_user(username, password):
            return redirect(url_for("routes.home"))
        else:
            error = "Nome de usuário ou senha incorretos. Tente novamente."
    return render_template("login.html", error=error)

@routes.route("/logout")
def logout():
    facade.logout_user()
    return redirect(url_for("routes.home"))

@routes.route("/")
def home():
    return render_template("home.html")

