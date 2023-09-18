from database.database import db
from database.models import User
from flask import render_template, request, url_for, redirect, Blueprint
from flask_login import login_user, logout_user

routes = Blueprint('routes', __name__)


@routes.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(username=request.form.get("username"),
                    password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("routes.login"))
    return render_template("sign_up.html")


@routes.route("/login", methods=["GET", "POST"])
def login():
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
    return render_template("login.html", error=error)


@routes.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("routes.home"))


@routes.route("/")
def home():
    return render_template("home.html")
