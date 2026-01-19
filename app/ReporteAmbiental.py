class ReporteAmbiental:
    def __init__(self, usuario, descripcion, ubicacion, foto=None):
        self.usuario = usuario
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.foto = foto

    def __str__(self):
        return f"Reporte de {self.usuario.nombre} en {self.ubicacion}: {self.descripcion}"