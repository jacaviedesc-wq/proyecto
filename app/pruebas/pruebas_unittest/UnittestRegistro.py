import unittest
from unittest.mock import MagicMock
from app import app, db

class TestRegistro(unittest.TestCase):
    #Pruebas unitarias para la funcionalidad de registro
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Simular conexión BD
        self.mock_cursor = MagicMock()
        db.get_cursor = MagicMock(return_value=self.mock_cursor)
        db.mysql = MagicMock()
        db.mysql.connection.commit = MagicMock()

    def test_registro_exitoso(self):
    #datos válidos
        response = self.app.post("/registro", data={
            "username": "usuarioNuevo",
            "email": "nuevo@example.com",
            "password": "Abc123"
        }, follow_redirects=True)

        self.mock_cursor.execute.assert_called_once()
        self.assertIn(b"Usuario registrado", response.data)

    def test_registro_campos_vacios(self):
    #Faltan datos
        response = self.app.post("/registro", data={
            "username": "",
            "email": "",
            "password": ""
        }, follow_redirects=True)

        self.assertNotIn(b"Usuario registrado", response.data)