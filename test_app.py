import unittest
from flask import Flask
from app import app, db, Users

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Configuração de teste
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.sqlite"
        app.config["TESTING"] = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

            # Adicione um usuário de teste à base de dados
            test_user = Users(username="testuser", password="testpassword")
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Limpeza após os testes
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_correct_credentials(self):
        # Testa login com credenciais corretas
        response = self.app.post("/login", data={"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_incorrect_credentials(self):
        # Testa login com credenciais incorretas
        response = self.app.post("/login", data={"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login

if __name__ == "__main__":
    unittest.main()
