import unittest
from app.ValidarDatos import ValidarDatos

class TestCaseRegistro(unittest.TestCase):
    def setUp(self):
        self.validador = ValidarDatos

#correo
    def test_validar_correo(self):
    #correo valido
        resultado = False
        try:
            self.validador.validar_correo("usuario@correo.com")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_correo_invalido(self):
    #correo invalido
        resultado = True
        try:
            self.validador.validar_correo("usuario-correo.com")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

#celular
    def test_validar_celular(self):
    #celular valido
        resultado = False
        try:
            self.validador.validar_celular("3001234567")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_celular_invalido(self):
    #celular invalido
        resultado = True
        try:
            self.validador.validar_celular("30A123456")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

#Nombre
    def test_validar_nombre(self):
   #nombre valido
        resultado = False
        try:
            self.validador.validar_nombre("Carlos")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_nombre_invalido(self):
    #nombre invalido
        resultado = True
        try:
            self.validador.validar_nombre("C4rlos")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)

#Dirección
    def test_validar_direccion(self):
    #direccion valida
        resultado = False
        try:
            self.validador.validar_direccion("Calle 10 #20-30 El Poblado")
            resultado = True
        except AssertionError:
            resultado = False
        self.assertTrue(resultado)

    def test_direccion_invalida(self):
    #direccion invalida
        resultado = True
        try:
            self.validador.validar_direccion("Calle @@ 20")
        except AssertionError:
            resultado = False
        self.assertFalse(resultado)