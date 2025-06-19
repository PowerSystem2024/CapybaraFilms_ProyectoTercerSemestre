from enum import Enum  # Importamos la clase base Enum para crear enumeraciones

# Definimos el enum TipoCandy que representa los tipos de combos disponibles
class TipoCandy(Enum):

    # Definimos las constantes del enum, cada una con un nombre y un precio
    CHICO = ("Combo Chico = 🍿 Pochoclo chico + 🥤 bebida 500cc", 5000)
    MEDIANO = ("Combo Mediano = 🍿 Pochoclo mediano + 2 🥤 bebidas 500cc", 8000)
    GRANDE = ("Combo Grande = 🍿 Pochoclo grande + 4 🥤 bebidas 500cc", 10000)

    # Constructor del enum. Se ejecuta para cada valor definido arriba.
    def __init__(self, nombre, precio):
        self.nombre = nombre    # Asigna el nombre descriptivo del combo
        self.precio = precio    # Asigna el precio correspondiente al combo

    # Método para obtener el nombre del combo
    def get_nombre(self):
        return self.nombre

    # Método para obtener el precio del combo
    def get_precio(self):
        return self.precio