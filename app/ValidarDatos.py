import re
from app.pruebas_assert.Nombre import Nombre
from app.pruebas_assert.Genero import Genero
from app.pruebas_assert.Documento import Documento
from app.pruebas_assert.Direccion import Direccion
from app.pruebas_assert.Celular import Celular
from app.pruebas_assert.Correo import Correo
from app.pruebas_assert.GrupoSanguineo import GrupoSanguineo

class ValidarDatos:
    @staticmethod
    def validar_nombre(nombre):
        return Nombre(nombre)

    @staticmethod
    def validar_apellido(apellido):
        return Nombre(apellido)

    @staticmethod
    def validar_usuario(usuario):
        assert len(usuario) >= 4, "El usuario debe tener al menos 4 caracteres"
        return usuario

    @staticmethod
    def validar_password(password):
        assert len(password) >= 6, "La contraseña debe tener al menos 6 caracteres"
        assert re.search(r"[A-Z]", password), "La contraseña debe tener al menos una letra mayúscula"
        assert re.search(r"[0-9]", password), "La contraseña debe tener al menos un número"
        return password

    @staticmethod
    def validar_correo(correo):
        return Correo(correo)

    @staticmethod
    def validar_celular(celular):
        return Celular(celular)

    @staticmethod
    def validar_direccion(direccion):
        return Direccion(direccion)

    @staticmethod
    def validar_documento(documento):
        return Documento(documento)

    @staticmethod
    def validar_genero(genero):
        return Genero(genero)

    @staticmethod
    def validar_grupo_sanguineo(grupo):
        return GrupoSanguineo(grupo)
