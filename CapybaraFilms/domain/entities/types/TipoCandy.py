from enum import Enum

# Definimos el enum TipoCandy
class TipoCandy(Enum):
    CHICO = ("Combo Chico", 2000)
    MEDIANO = ("Combo Mediano", 4000)
    GRANDE = ("Combo Grande", 5000)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio