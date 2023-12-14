import unittest
from models.database import db
from models.user import User
from app import create_app


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Configuração de teste
        self.app = create_app('TESTING')
        self.session = db.session
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Adicione um usuário de teste à base de dados
            test_user = User(username="testuser", password="testpassword")
            test_user_2 = User(username="a", password="a")
            test_user_3 = User(username="a"*12, password="a"*12)
            db.session.add_all([test_user, test_user_2, test_user_3])
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

    #Testes de Particionamento em Classes de Equivalencia

    def test_login_min_password_length(self):
        # Testa login com senha de tamanho minimo
        response = self.client.post("/login", data={"username": "a", "password": "a"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_correct_password_length(self):
        # Testa login com senha de tamanho medio
        response = self.client.post("/login", data={"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_max_password_length(self):
        # Testa login com senha de tamanho maximo
        response = self.client.post("/login", data={"username": "a" * 12, "password": "a" * 12})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_min_username_length(self):
        # Testa login com username de tamanho minimo
        response = self.client.post("/login", data={"username": "a", "password": "a"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_correct_username_length(self):
        # Testa login com username de tamanho medio
        response = self.client.post("/login", data={"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    def test_login_max_username_length(self):
        # Testa login com username de tamanho maximo
        response = self.client.post("/login", data={"username": "a" * 12, "password": "a" * 12})
        self.assertEqual(response.status_code, 302)  # Deve redirecionar após login bem-sucedido

    #Testes de Analise de Valor Limite
    
    def test_login_below_min_password_length(self):
        # Testa login com senha abaixo do tamanho minimo
        response = self.client.post("/login", data={"username": "testuser", "password": ""})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login

    def test_login_above_max_password_length(self):
        # Testa login com senha acima do tamanho maximo
        response = self.client.post("/login", data={"username": "testuser", "password": "a" * 13})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login

    def test_login_below_min_username_length(self):
        # Testa login com senha abaixo do tamanho minimo
        response = self.client.post("/login", data={"username": "", "password": "testpassword"})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login

    def test_login_above_max_username_length(self):
        # Testa login com senha acima do tamanho maximo
        response = self.client.post("/login", data={"username": "a" * 13, "password": "testpassword"})
        self.assertEqual(response.status_code, 200)  # Deve permanecer na página de login
    

if __name__ == "__main__":
    unittest.main()
