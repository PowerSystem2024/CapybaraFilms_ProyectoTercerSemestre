from capybarafilms.domain.entities.types import TipoButaca  # Tipo de butaca (COMUN o PREMIUM)
from capybarafilms.domain.entities.types import Ubicacion   # Clase de ubicación


class Sala:
    def __init__(self, pelicula):
        self.capacidad = 12  # Capacidad de la sala (12x12)
        self.min_premium = 5  # Desde la fila 5
        self.max_premium = 7  # Hasta la fila 7
        self.pelicula = pelicula  # Película proyectada
        self.butacas = [[None for _ in range(self.capacidad)] for _ in range(self.capacidad)]  # Matriz 12x12
        self.llenar_butacas()

    def llenar_butacas(self):
        for fila in range(self.capacidad):
            for butaca in range(self.capacidad):
                if self.min_premium <= fila <= self.max_premium:
                    self.butacas[fila][butaca] = Butaca(TipoButaca.PREMIUM, Ubicacion(fila, butaca))
                else:
                    self.butacas[fila][butaca] = Butaca(TipoButaca.COMUN, Ubicacion(fila, butaca))

    def asignar_butaca(self, ubicacion):
        fila = ubicacion.get_fila()
        columna = ubicacion.get_butaca()
        if 0 <= fila < self.capacidad and 0 <= columna < self.capacidad:
            butaca = self.butacas[fila][columna]
            if not butaca.is_estado():
                butaca.set_estado(True)
            else:
                print("La butaca se encuentra ocupada.")
        else:
            print("Fila o butaca inválidos.")

    def precio_de_entrada(self, ubicacion):
        fila = ubicacion.get_fila()
        columna = ubicacion.get_butaca()
        if 0 <= fila < self.capacidad and 0 <= columna < self.capacidad:
            return (
                self.butacas[fila][columna].get_categoria().get_precio() +
                self.pelicula.get_formato().get_precio_extra()
            )
        else:
            print("Fila o butaca inválidos.")
            return 0

    def butaca_esta_ocupada(self, ubicacion):
        return self.butacas[ubicacion.get_fila()][ubicacion.get_butaca()].is_estado()

    def get_butaca(self, ubicacion):
        return self.butacas[ubicacion.get_fila()][ubicacion.get_butaca()]

    def get_capacidad(self):
        return self.capacidad

    def __str__(self):
        resultado = "Sala N° 1\n"
        resultado += f"Película: {self.pelicula.get_nombre()}\n"
        resultado += f"Formato de la película: {self.pelicula.get_formato()}\n"
        resultado += f"Género de la película: {self.pelicula.get_genero()}\n"
        resultado += f"Duración: {self.pelicula.get_duracion()} min.\n"
        resultado += f"Dirigida por: {self.pelicula.get_director()}\n\n"
        resultado += "Butacas Seleccionadas: \n"
        for fila in range(self.capacidad):
            for butaca in range(self.capacidad):
                b = self.butacas[fila][butaca]
                resultado += "[X]" if b.is_estado() else "[ ]"
            resultado += "\n"
        return resultado