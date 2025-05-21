# Importación de Enum
from enum import Enum

class FormatoPelicula(Enum):
    # Definimos los dos formatos como miembros del enum
    # Formato 2D sin costo adicional.
    DOS_D = ("2D", 0)
    # Formato 3D con costo adicional de $1000
    TRES_D = ("3D", 1000)
    
    # Método inicializador del tipo de pelicula y el precio extra
    def __init__(self, tipo, precio_extra):
        self._tipo = tipo
        self._precio_extra = precio_extra
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def precio_extra(self):
        return self._precio_extra
    
    def get_precio_extra(self):
        return self._precio_extra
    
    def get_tipo(self):
        """Devuelve la representación como '2D' o '3D'."""
        return self._tipo
    