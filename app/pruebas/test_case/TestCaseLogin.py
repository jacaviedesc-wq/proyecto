import unittest
from app.ValidarDatos import ValidarDatos

class TestCaseLogin(unittest.TestCase):
    def setUp(self):
        self.validador = ValidarDatos

    def test_validar_usuario(self):
    #usuario válido
        resultado = False
        try:
            self.validador.validar_usuario("carlos123")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_usuario_invalido(self):
    #usuario invalido
        resultado = True
        try:
            self.validador.validar_usuario("abc")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

    def test_contrasenna_valida(self):
    #contraseña válida
        resultado = False
        try:
            self.validador.validar_contrasenna("Abc123")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_contrasenna_mayusculas(self):
    #contraseña invaldia
        resultado = True
        try:
            self.validador.validar_contrasenna("abcdef")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

    def test_contrasenna_numeros(self):
    #contraseña invalida
        resultado = True
        try:
            self.validador.validar_contrasenna("Abcdef")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

    def test_contrasenna_corta(self):
    #contraseña invalida
        resultado = True
        try:
            self.validador.validar_contrasenna("Ab1")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)