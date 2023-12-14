from models.database import db
from models.user import User
from forms.user_register_form import UserForm
from forms.recipe_search_form import RecipeSearchByIngredientsForm, RecipeSearchByNameForm
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user
from facade.user_facade import UserFacade  


user_facade = UserFacade()

def register():
    return user_facade.register()

def login():
    return user_facade.login()

def logout():
    return user_facade.logout()

def home():
    return user_facade.home()

def config():
    current_user = user_facade.current_user()
    form = UserForm()
    if request.method == "POST":
        # Get form data
        new_username = request.form.get("username")
        new_password = request.form.get("password")
        # Update user information in the database
        current_user.username = new_username
        current_user.password = new_password
        db.session.commit()

        print(f"User with ID {current_user.id} updated successfully.")

    return render_template("config.html", form=form)

