import unittest
from unittest.mock import MagicMock
import bcrypt
from app import app, db

class TestLogin(unittest.TestCase):
#Pruebas unitarias para la funcionalidad de login
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Simular conexión a BD
        self.mock_cursor = MagicMock()
        db.get_cursor = MagicMock(return_value=self.mock_cursor)
        db.mysql = MagicMock()
        db.mysql.connection.commit = MagicMock()

    def test_login(self):
        #usuario y contraseña correctos
        hashed_pw = bcrypt.hashpw("Abc123".encode("utf-8"), bcrypt.gensalt())
        usuario_falso = {"usuario": "juan", "contrasena": hashed_pw.decode("utf-8")}
        self.mock_cursor.fetchone.return_value = usuario_falso

        response = self.app.post("/login", data={
            "user": "juan",
            "password": "Abc123"
        }, follow_redirects=True)

        self.assertIn(b"Bienvenido", response.data)

    def test_login_contrasena(self):
        #contraseña incorrecta
        hashed_pw = bcrypt.hashpw("Correcta1".encode("utf-8"), bcrypt.gensalt())
        usuario_falso = {"usuario": "juan", "contrasena": hashed_pw.decode("utf-8")}
        self.mock_cursor.fetchone.return_value = usuario_falso

        response = self.app.post("/login", data={
            "user": "juan",
            "password": "Mala123"
        }, follow_redirects=True)

        self.assertIn(b"Contrase", response.data)

    def test_usuario_inexistente(self):
        #usuario no existe
        self.mock_cursor.fetchone.return_value = None

        response = self.app.post("/login", data={
            "user": "noexiste",
            "password": "Abc123"
        }, follow_redirects=True)

        self.assertIn(b"Usuario no encontrado", response.data)