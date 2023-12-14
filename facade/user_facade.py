from models.database import db
from models.user import User
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user
from forms.user_register_form import UserForm
from forms.recipe_search_form import RecipeSearchByIngredientsForm, RecipeSearchByNameForm


class UserFacade:
    def register(self):
        """
        Register a new user.

        Returns:
            flask.Response: A Flask response, either a redirect to the login page or a rendered sign-up template.
        """
        if request.method == "POST":
            user = User(username=request.form.get("username"),
                        password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("routes.login"))
        return render_template("sign_up.html", form=UserForm())

    def login(self):
        """
        Log in a user.

        Returns:
            flask.Response: A Flask response, either a redirect to the home page or a rendered login template with an error message.
        """
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
        """
        Log out the current user.

        Returns:
            flask.Response: A Flask response, a redirect to the home page.
        """

        logout_user()
        return redirect(url_for("routes.home"))
    
    def current_user(self):
        """
        Returns the current_user.

        Returns:
            current_user (User): The model of the User currently logged in.
        """
        return current_user

    def home(self):
        """
        Render the home page.

        Returns:
            flask.Response: A Flask response, a rendered home page template with recipe search forms.
        """
        return render_template("index.html", ingredientsForm=RecipeSearchByIngredientsForm(), recipeForm=RecipeSearchByNameForm())

    def is_admin(self):
        """
        Check if the user is an admin.

        Returns:
            bool: True if the current user is an admin and authenticated, False otherwise.
        """
        return current_user.is_authenticated and current_user.is_admin
    
    def is_authenticated(self):
        """
        Check if the user is authenticated.

        Returns:
            bool: True if the current user is authenticated, False otherwise.
        """
        return current_user.is_authenticated
