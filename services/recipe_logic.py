from models.recipe import Recipe
from models.ingredient import IngredientInformation


def calculate_macronutrients_for_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return None

    ingredients = recipe.ingredients

    total_calories = 0
    total_proteins = 0
    total_fats = 0
    total_carbohydrates = 0

    for ingredient in ingredients:
        ingredient_id = ingredient.ingredient_id
        quantity = ingredient.quantity

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
