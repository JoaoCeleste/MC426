import unittest
from models.database import db
from models.ingredient import Ingredient, IngredientInformation
from models.recipe import Recipe, RecipeIngredient
from models.user import User
from app import create_app
from services.recipe_logic import calculate_macronutrients_for_recipe


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TESTING')
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
            ingredient.recipes.append(RecipeIngredient(recipe=recipe,quantity=1))
            self.session.add(ingredient)
            self.session.commit()  

            ingredient_info = IngredientInformation(
                ingredient_id=ingredient.id, calories=100, proteins=10, fats=5, carbohydrates=15
            )
            self.session.add(ingredient_info)
            self.session.commit()

            macronutrients = calculate_macronutrients_for_recipe(recipe.id)
            self.assertEqual(macronutrients["total_calories"], 100)
            self.assertEqual(macronutrients["total_proteins"], 10)
            self.assertEqual(macronutrients["total_fats"], 5)
            self.assertEqual(macronutrients["total_carbohydrates"], 15)


    # Testes de Classes de Equivalencia

    def test_min_macronutrients_amount(self):
        with self.app.app_context():
            recipe = Recipe(name="Min Recipe", instruction="Placeholder")
            self.session.add(recipe)
            self.session.commit()

            ingredient = Ingredient(name="Min Ingredient")
            ingredient.recipes.append(RecipeIngredient(recipe=recipe, quantity=1))
            self.session.add(ingredient)
            self.session.commit()

          
            min_calories = 1
            min_proteins = 1
            min_fats = 1
            min_carbohydrates = 1

            ingredient_info = IngredientInformation(
                ingredient_id=ingredient.id, calories=min_calories, proteins=min_proteins, 
                fats=min_fats, carbohydrates=min_carbohydrates
            )
            self.session.add(ingredient_info)
            self.session.commit()

            macronutrients = calculate_macronutrients_for_recipe(recipe.id)

           
            self.assertGreaterEqual(macronutrients["total_calories"], min_calories)
            self.assertGreaterEqual(macronutrients["total_proteins"], min_proteins)
            self.assertGreaterEqual(macronutrients["total_fats"], min_fats)
            self.assertGreaterEqual(macronutrients["total_carbohydrates"], min_carbohydrates)


def test_correct_macronutrients_amount(self):
    with self.app.app_context():
        mid_calories = 100
        mid_proteins = 10
        mid_fats = 5
        mid_carbohydrates = 15

        recipe = Recipe(name="Mid Recipe", instruction="Placeholder")
        self.session.add(recipe)
        self.session.commit()

        ingredient = Ingredient(name="Mid Ingredient")
        ingredient.recipes.append(RecipeIngredient(recipe=recipe, quantity=1))
        self.session.add(ingredient)
        self.session.commit()

        ingredient_info = IngredientInformation(
            ingredient_id=ingredient.id, calories=mid_calories, proteins=mid_proteins, 
            fats=mid_fats, carbohydrates=mid_carbohydrates
        )
        self.session.add(ingredient_info)
        self.session.commit()

        macronutrients = calculate_macronutrients_for_recipe(recipe.id)

        self.assertEqual(macronutrients["total_calories"], mid_calories)
        self.assertEqual(macronutrients["total_proteins"], mid_proteins)
        self.assertEqual(macronutrients["total_fats"], mid_fats)
        self.assertEqual(macronutrients["total_carbohydrates"], mid_carbohydrates)


def test_max_macronutrients_amount(self):
    with self.app.app_context():
        recipe = Recipe(name="Max Recipe", instruction="Placeholder")
        self.session.add(recipe)
        self.session.commit()

        ingredient = Ingredient(name="Max Ingredient")
        ingredient.recipes.append(RecipeIngredient(recipe=recipe, quantity=1))
        self.session.add(ingredient)
        self.session.commit()

        
        max_calories = 1000
        max_proteins = 100
        max_fats = 50
        max_carbohydrates = 150

        ingredient_info = IngredientInformation(
            ingredient_id=ingredient.id, calories=max_calories, proteins=max_proteins, 
            fats=max_fats, carbohydrates=max_carbohydrates
        )
        self.session.add(ingredient_info)
        self.session.commit()

        macronutrients = calculate_macronutrients_for_recipe(recipe.id)

        
        self.assertLessEqual(macronutrients["total_calories"], max_calories)
        self.assertLessEqual(macronutrients["total_proteins"], max_proteins)
        self.assertLessEqual(macronutrients["total_fats"], max_fats)
        self.assertLessEqual(macronutrients["total_carbohydrates"], max_carbohydrates)
   

    # Testes de Analise do Valor Limite
        
    def test_below_min_macronutrients_amount(self):
        with self.app.app_context():
            recipe = Recipe(name="Below Min Recipe", instruction="Placeholder")
            self.session.add(recipe)
            self.session.commit()

            ingredient = Ingredient(name="Below Min Ingredient")
            ingredient.recipes.append(RecipeIngredient(recipe=recipe, quantity=1))
            self.session.add(ingredient)
            self.session.commit()

            
            min_calories = 50
            min_proteins = 5
            min_fats = 2
            min_carbohydrates = 8

            ingredient_info = IngredientInformation(
                ingredient_id=ingredient.id, calories=min_calories - 1, proteins=min_proteins - 1, 
                fats=min_fats - 1, carbohydrates=min_carbohydrates - 1
            )
            self.session.add(ingredient_info)
            self.session.commit()

            macronutrients = calculate_macronutrients_for_recipe(recipe.id)

            
            self.assertLess(macronutrients["total_calories"], min_calories)
            self.assertLess(macronutrients["total_proteins"], min_proteins)
            self.assertLess(macronutrients["total_fats"], min_fats)
            self.assertLess(macronutrients["total_carbohydrates"], min_carbohydrates)


    def test_above_max_macronutrients_amount(self):
        with self.app.app_context():
            recipe = Recipe(name="Above Max Recipe", instruction="Placeholder")
            self.session.add(recipe)
            self.session.commit()

            ingredient = Ingredient(name="Above Max Ingredient")
            ingredient.recipes.append(RecipeIngredient(recipe=recipe, quantity=1))
            self.session.add(ingredient)
            self.session.commit()

            
            max_calories = 200
            max_proteins = 20
            max_fats = 10
            max_carbohydrates = 30

            ingredient_info = IngredientInformation(
                ingredient_id=ingredient.id, calories=max_calories + 1, proteins=max_proteins + 1, 
                fats=max_fats + 1, carbohydrates=max_carbohydrates + 1
            )
            self.session.add(ingredient_info)
            self.session.commit()

            macronutrients = calculate_macronutrients_for_recipe(recipe.id)

            # Use assertGreater or assertGreaterEqual to check if the values are above the maximum
            self.assertGreater(macronutrients["total_calories"], max_calories)
            self.assertGreater(macronutrients["total_proteins"], max_proteins)
            self.assertGreater(macronutrients["total_fats"], max_fats)
            self.assertGreater(macronutrients["total_carbohydrates"], max_carbohydrates)
