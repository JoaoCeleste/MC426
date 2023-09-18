import unittest
from database.database import db
from database.models import User, Ingredient, IngredientInformation, Recipe, RecipeIngredient, RecipeInstruction
from app import create_app


class DatabaseIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update({
            "TESTING": True,
        })
        self.session = db.session

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        with self.app.app_context():
            user = User(username="tiago", password="teste")
            self.session.add(user)
            self.session.commit()
            self.assertIsNotNone(user.id)

    def test_read_user(self):
        with self.app.app_context():
            user = User(username="tiago", password="teste")
            self.session.add(user)
            self.session.commit()
            retrieved_user = self.session.query(User).filter_by(id=user.id).first()
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(user.id, retrieved_user.id)

    def test_delete_user(self):
        with self.app.app_context():
            user = User(username="tiago", password="teste")
            self.session.add(user)
            self.session.commit()
            user_id = user.id

            self.session.delete(user)
            self.session.commit()

            deleted_user = self.session.query(User).filter_by(id=user_id).first()
            self.assertIsNone(deleted_user)

    def test_find_ingredient_information(self):
        with self.app.app_context():
            ingredient = Ingredient(name='Chicken')
            self.session.add(ingredient)
            self.session.commit()

            info = IngredientInformation(ingredient_id=ingredient.id, calories=200,
                                         proteins=20, fats=10, carbohydrates=0)
            self.session.add(info)
            self.session.commit()

            macronutrients = self.session.query(IngredientInformation).filter_by(ingredient_id=ingredient.id).first()
            self.assertIsNotNone(macronutrients)
            self.assertEqual(info.id, macronutrients.id)
            self.assertEqual(macronutrients.calories, 200)
            self.assertEqual(macronutrients.proteins, 20)
            self.assertEqual(macronutrients.fats, 10)
            self.assertEqual(macronutrients.carbohydrates, 0)


if __name__ == '__main__':
    unittest.main()
