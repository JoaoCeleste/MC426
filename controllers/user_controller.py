from models.database import db
from models.user import User
from forms.user_register_form import UserForm
from forms.recipe_search_form import RecipeSearchByIngredientsForm, RecipeSearchByNameForm
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user


def register():
    if request.method == "POST":
        user = User(username=request.form.get("username"),
                    password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("routes.login"))
    return render_template("sign_up.html", form=UserForm())


def login():
    form=UserForm()
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user is not None and user.password == password:
            login_user(user)
            return redirect(url_for("routes.home"))
        else:
            error = "Nome de usuário ou senha incorretos. Tente novamente."
    return render_template("login.html", error=error, form=form)


def logout():
    logout_user()
    return redirect(url_for("routes.home"))


def home():
    return render_template("index.html", ingredientsForm=RecipeSearchByIngredientsForm(), recipeForm=RecipeSearchByNameForm())
