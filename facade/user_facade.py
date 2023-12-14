from models.database import db
from models.user import User
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user
from forms.user_register_form import UserForm
from forms.recipe_search_form import RecipeSearchByIngredientsForm, RecipeSearchByNameForm

class UserFacade:
    def register(self):
        if request.method == "POST":
            user = User(username=request.form.get("username"),
                        password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("routes.login"))
        return render_template("sign_up.html", form=UserForm())


    def login(self):  
        form = UserForm()
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

    def logout(self):
        logout_user()
        return redirect(url_for("routes.home"))
    
    def current_user(self):
        return current_user

    def home(self):
        return render_template("index.html", ingredientsForm=RecipeSearchByIngredientsForm(), recipeForm=RecipeSearchByNameForm())
    
    def is_authenticated(self):
        return current_user.is_authenticated

    def is_admin(self):
        return current_user.is_authenticated and current_user.is_admin