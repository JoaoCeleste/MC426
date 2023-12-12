from flask import Blueprint
from controllers.user_controller import register, login, logout, home
from controllers.recipe_controller import new as recipe_new, create as recipe_create, search as recipe_search
from controllers.ingredient_controller import new as ingredient_new, create as ingredient_create

routes = Blueprint('routes', __name__)

routes.route('/register', methods=["GET", "POST"])(register)
routes.route("/login", methods=["GET", "POST"])(login)
routes.route("/logout")(logout)
routes.route("/")(home)

routes.route("/ingredients/new", methods=["GET"], endpoint='ingredients_new')(ingredient_new)
routes.route("/ingredients", methods=["POST"], endpoint='ingredients_create')(ingredient_create)

routes.route("/recipe/new", methods=["GET"], endpoint='recipe_new')(recipe_new)
routes.route("/recipe", methods=["POST"], endpoint='recipe_create')(recipe_create)
routes.route("/search", methods=["GET"], endpoint='recipe_search')(recipe_search)