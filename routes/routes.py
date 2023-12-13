from flask import Blueprint
from controllers.user_controller import register, login, logout, home
from controllers.recipe_controller import new as recipe_new, create as recipe_create, search as recipe_search, index as recipe_index
from controllers.ingredient_controller import index

routes = Blueprint('routes', __name__)

routes.route('/register', methods=["GET", "POST"])(register)
routes.route("/login", methods=["GET", "POST"])(login)
routes.route("/logout")(logout)
routes.route("/")(home)

routes.route("/ingredients", methods=["GET"])(index)

routes.route("/recipes", methods=["GET"], endpoint='recipe_index')(recipe_index)
routes.route("/recipe/new", methods=["GET"], endpoint='recipe_new')(recipe_new)
routes.route("/recipe", methods=["POST"], endpoint='recipe_create')(recipe_create)
routes.route("/search", methods=["GET"], endpoint='recipe_search')(recipe_search)