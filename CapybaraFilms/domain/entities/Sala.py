import psycopg2
from domain.entities.types.TipoButaca import TipoButaca
from domain.entities.types.Ubicacion import Ubicacion
from domain.entities.Butaca import Butaca
from domain.entities.Pelicula import Pelicula

class Sala:
    def __init__(self, pelicula, conn):
        self.capacidad = 12
        self.min_premium = 5
        self.max_premium = 7
        self.pelicula = pelicula
        self.butacas = [[None for _ in range(self.capacidad)] for _ in range(self.capacidad)]
        self.conn = conn  # conexión a PostgreSQL

        # Guardar la película en la base de datos y obtener su ID
        self.pelicula_id = self.guardar_pelicula()

        # Crear la sala y guardar su ID
        self.sala_id = self.guardar_sala()

        # Cargar y guardar todas las butacas
        self.llenar_butacas()
        self.guardar_butacas()

    def guardar_pelicula(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO peliculas (nombre, formato, genero, duracion, director)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """, (
            self.pelicula.get_nombre(),
            str(self.pelicula.get_formato()),
            self.pelicula.get_genero(),
            self.pelicula.get_duracion(),
            self.pelicula.get_director()
        ))
        pelicula_id = cursor.fetchone()[0]
        self.conn.commit()
        return pelicula_id

    def guardar_sala(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO salas (pelicula_id)
            VALUES (%s) RETURNING id
        """, (self.pelicula_id,))
        sala_id = cursor.fetchone()[0]
        self.conn.commit()
        return sala_id

    def llenar_butacas(self):
        for fila in range(self.capacidad):
            for columna in range(self.capacidad):
                tipo = TipoButaca.PREMIUM if self.min_premium <= fila <= self.max_premium else TipoButaca.COMUN
                self.butacas[fila][columna] = Butaca(tipo, Ubicacion(fila, columna))

    def guardar_butacas(self):
        cursor = self.conn.cursor()
        for fila in range(self.capacidad):
            for columna in range(self.capacidad):
                butaca = self.butacas[fila][columna]
                tipo = str(butaca.get_categoria())
                estado = butaca.is_estado()
                cursor.execute("""
                    INSERT INTO butacas (sala_id, fila, columna, tipo, ocupada)
                    VALUES (%s, %s, %s, %s, %s)
                """, (self.sala_id, fila, columna, tipo, estado))
        self.conn.commit()

    def asignar_butaca(self, ubicacion):
        fila = ubicacion.get_fila()
        columna = ubicacion.get_butaca()
        if 0 <= fila < self.capacidad and 0 <= columna < self.capacidad:
            butaca = self.butacas[fila][columna]
            if not butaca.is_estado():
                butaca.set_estado(True)
                self.actualizar_estado_butaca_db(fila, columna)
                print(f"Butaca en fila {fila + 1}, columna {columna + 1} reservada con éxito.")
            else:
                print("La butaca seleccionada ya está ocupada.")
        else:
            print("Fila o butaca inválidos.")

    def actualizar_estado_butaca_db(self, fila, columna):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE butacas
            SET ocupada = TRUE
            WHERE sala_id = %s AND fila = %s AND columna = %s
        """, (self.sala_id, fila, columna))
        self.conn.commit()

    def mostrar_butacas(self):
        print("Distribución de las butacas:\n")
        for fila in range(self.capacidad):
            for columna in range(self.capacidad):
                b = self.butacas[fila][columna]
                print("[X]" if b.is_estado() else "[ ]", end=" ")
            print()
        print()

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
