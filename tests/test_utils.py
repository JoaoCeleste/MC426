import unittest
from models.database import db
from models.ingredient import Ingredient, IngredientInformation
from models.recipe import Recipe, RecipeIngredient
from models.user import User
from app import create_app
from services.recipe_logic import calculate_macronutrients_for_recipe


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update({
            "TESTING": True,
        })
        self.session = db.session
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            test_user = User(username="testuser", password="testpassword")
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_calculate_macronutrients_for_recipe(self):
        with self.app.app_context():
            test_user = User(username="testrecipe", password="dummy")
            self.session.add(test_user)
            self.session.commit()

            recipe = Recipe(name="Test Recipe", instruction="Placeholder")
            self.session.add(recipe)
            self.session.commit()

            ingredient = Ingredient(name="Test Ingredient")
            self.session.add(ingredient)
            self.session.commit()  

            ingredient_info = IngredientInformation(
                ingredient_id=ingredient.id, calories=100, proteins=10, fats=5, carbohydrates=15
            )
            self.session.add(ingredient_info)
            self.session.commit()

            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.id, ingredient_id=ingredient.id, quantity=2
            )
            self.session.add(recipe_ingredient)
            self.session.commit()

            macronutrients = calculate_macronutrients_for_recipe(recipe.id)
            self.assertEqual(macronutrients["total_calories"], 200)
            self.assertEqual(macronutrients["total_proteins"], 20)
            self.assertEqual(macronutrients["total_fats"], 10)
            self.assertEqual(macronutrients["total_carbohydrates"], 30)
