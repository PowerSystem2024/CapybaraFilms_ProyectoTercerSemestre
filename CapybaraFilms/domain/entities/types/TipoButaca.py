from enum import Enum

class TipoButaca(Enum):
    COMUN = ("comun", 4000)  # Tipo de butaca común con un precio
    PREMIUM = ("premium", 6500)  # Tipo de butaca premium con un precio más elevado

    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del tipo de butaca
        self.precio = precio  # Precio del tipo de butaca

    def get_nombre(self):
        # Devuelve el nombre del tipo de butaca
        return self.nombre

    def get_precio(self):
        # Devuelve el precio del tipo de butaca
        return self.precio
