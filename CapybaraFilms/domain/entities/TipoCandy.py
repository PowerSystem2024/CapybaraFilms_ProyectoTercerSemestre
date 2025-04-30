from enum import Enum

# Definimos el enum TipoCandy
class TipoCandy(Enum):
    CHICO = "Combo Chico"
    MEDIANO = "Combo Mediano"
    GRANDE = "Combo Grande"

    def get_nombre(self):
        return self.value

# Definimos la clase Candy
class Candy:
    def __init__(self, tipo):
        self.tipo = tipo  # Se asigna el tipo de combo
    
    def get_tipo(self):
        return self.tipo  # Se devuelve el tipo de candy
    
    def __str__(self):
        return f"Candy: {self.tipo.get_nombre()}"  # Devuelve el nombre del tipo de candy