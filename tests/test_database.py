import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import db, app
from database.database import User, Ingredient, IngredientInformation, Recipe, RecipeIngredient, RecipeInstruction


class DatabaseIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        with app.app_context():
            db.create_all()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        user = User(id=123, username="tiago", password="teste")
        self.session.add(user)
        self.session.commit()
        self.assertIsNotNone(user.id)

    def test_read_user(self):
        user = User(id=123, username="tiago", password="teste")
        self.session.add(user)
        self.session.commit()
        retrieved_user = self.session.query(User).filter_by(id=user.id).first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(user.id, retrieved_user.id)

    def test_delete_user(self):
        user = User(id=123, username="tiago", password="teste")
        self.session.add(user)
        self.session.commit()
        user_id = user.id

        self.session.delete(user)
        self.session.commit()

        deleted_user = self.session.query(User).filter_by(id=user_id).first()
        self.assertIsNone(deleted_user)

    def test_find_ingredient_information(self):
        ingredient = Ingredient(id=30, name='Chicken')
        self.session.add(ingredient)
        self.session.commit()

        info = IngredientInformation(id=1, ingredient_id=ingredient.id, calories=200,
                                     proteins=20, fats=10, carbohydrates=0)
        self.session.add(info)
        self.session.commit()

        macronutrients = self.session.query(IngredientInformation).filter_by(ingredient_id=ingredient.id).first()
        self.assertIsNotNone(macronutrients)
        self.assertEqual(info.id, macronutrients.id)
        self.assertEqual(macronutrients['calories'], 200)
        self.assertEqual(macronutrients['proteins'], 20)
        self.assertEqual(macronutrients['fats'], 10)
        self.assertEqual(macronutrients['carbohydrates'], 0)


if __name__ == '__main__':
    unittest.main()
