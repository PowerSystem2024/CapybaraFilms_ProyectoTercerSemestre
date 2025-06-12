from enum import Enum

# Definimos el enum TipoCandy
class TipoCandy(Enum):

    CHICO = ("Combo Chico", 5000)
    MEDIANO = ("Combo Mediano", 8000)
    GRANDE = ("Combo Grande", 10000)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio