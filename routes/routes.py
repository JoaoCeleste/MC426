from flask import Blueprint
from controllers.user_controller import register, login, logout, home, config
from controllers.recipe_controller import new as recipe_new, create as recipe_create, search as recipe_search, index as recipe_index, show as recipe_show, bookmark, bookmark_index as bookmarks
from controllers.ingredient_controller import index as ingredient_index, new as ingredient_new, create as ingredient_create, show as ingredients_show
from controllers.comment_controller import create as comment_create

routes = Blueprint('routes', __name__)

routes.route('/register', methods=["GET", "POST"])(register)
routes.route("/login", methods=["GET", "POST"])(login)
routes.route("/config", methods=["GET", "POST"])(config)
routes.route("/logout")(logout)
routes.route("/")(home)

routes.route("/ingredients", methods=["GET"])(ingredient_index)
routes.route("/ingredients/<id>", methods=["GET"], endpoint='ingredients_show')(ingredients_show)
routes.route("/ingredients/new", methods=["GET"], endpoint='ingredients_new')(ingredient_new)
routes.route("/ingredients", methods=["POST"], endpoint='ingredients_create')(ingredient_create)

routes.route("/recipes", methods=["GET"], endpoint='recipe_index')(recipe_index)
routes.route("/recipe/<id>", methods=["GET"], endpoint='recipe_show')(recipe_show)
routes.route("/recipe/new", methods=["GET"], endpoint='recipe_new')(recipe_new)
routes.route("/recipe", methods=["POST"], endpoint='recipe_create')(recipe_create)
routes.route("/search", methods=["GET"], endpoint='recipe_search')(recipe_search)

routes.route("/recipe/<id>/comment", methods=["POST"], endpoint='comment_create')(comment_create)

routes.route("/bookmark/<id>", methods=["POST"], endpoint='bookmark')(bookmark)
routes.route("/bookmarks", methods=["GET"], endpoint='bookmarks')(bookmarks)