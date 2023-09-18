import unittest
from database.database import db
from database.models import User
from app import create_app


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Configuração de teste
        self.app = create_app()
        self.app.config.update({
            "TESTING": True,
        })
        self.session = db.session
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Adicione um usuário de teste à base de dados
            test_user = User(username="testuser", password="testpassword")
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Limpeza após os testes
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_correct_credentials(self):
        # Testa login com credenciais corretas
        response = self.client.post("/login", data={"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_incorrect_credentials(self):
        # Testa login com credenciais incorretas
        response = self.client.post("/login", data={"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login


if __name__ == "__main__":
    unittest.main()
