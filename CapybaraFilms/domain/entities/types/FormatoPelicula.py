from enum import Enum

# Excepción personalizada
class ReservaException(Exception):
    """Excepción personalizada para errores en reservas."""
    pass

class FormatoPelicula(Enum):
    DOS_D = ("2D", 0)          # Formato 2D sin costo adicional
    TRES_D = ("3D", 1000)      # Formato 3D con costo adicional

    def __init__(self, tipo, precio_extra):
        self._tipo = tipo
        self._precio_extra = precio_extra

    @property
    def tipo(self):
        try:
            return self._tipo
        except AttributeError:
            raise ReservaException("El tipo del formato de película no está definido correctamente.")

    @property
    def precio_extra(self):
        try:
            return self._precio_extra
        except AttributeError:
            raise ReservaException("El precio extra del formato de película no está definido correctamente.")

    def get_precio_extra(self):
        try:
            return self._precio_extra
        except AttributeError:
            raise ReservaException("No se pudo obtener el precio extra del formato de película.")

    def get_tipo(self):
        """Devuelve la representación como '2D' o '3D'."""
        try:
            return self._tipo
        except AttributeError:
            raise ReservaException("No se pudo obtener el tipo del formato de película.")
