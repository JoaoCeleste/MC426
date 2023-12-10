from flask import Blueprint
from controllers.user_controller import register, login, logout, home
from controllers.recipe_controller import create
from controllers.ingredient_controller import index

routes = Blueprint('routes', __name__)

routes.route('/register', methods=["GET", "POST"])(register)
routes.route("/login", methods=["GET", "POST"])(login)
routes.route("/logout")(logout)
routes.route("/")(home)

routes.route("/ingredients", methods=["GET"])(index)

routes.route("/recipe/create", methods=["GET", "POST"])(create)