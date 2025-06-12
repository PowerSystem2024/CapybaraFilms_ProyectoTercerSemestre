from domain.entities.Pelicula import Pelicula
import psycopg2

class PeliculaDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def crear_pelicula(self, pelicula: Pelicula):
        try:
            sentencia = """
            INSERT INTO pelicula (nombre, director, duracion, genero, idioma, formato)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (
                pelicula.nombre,
                pelicula.director,
                pelicula.duracion,
                pelicula.genero,
                pelicula.idioma,
                pelicula.formato,
            )
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"Película creada correctamente: {pelicula.nombre}")
        except psycopg2.Error as e:
            print("Error inesperado al crear película.")
            print(f"Detalles: {e}")

    def buscar_por_id(self, id_pelicula: int):
        try:
            sentencia = "SELECT id_pelicula, nombre, director, duracion, genero, idioma, formato FROM pelicula WHERE id_pelicula = %s"
            resultado = self.db.obtener_datos(sentencia, (id_pelicula,))
            if resultado:
                fila = resultado[0]
                return Pelicula(*fila) # el * permite desempaquetar la tupla directamente en los parámetros del constructor de Pelicula
            print(f"No se encontró ninguna película con ID {id_pelicula}.")
            return None
        except psycopg2.Error as e:
            print("Error al buscar película.")
            print(f"Detalles: {e}")
            return None

    def obtener_todas(self):
        try:
            sentencia = "SELECT id_pelicula, nombre, director, duracion, genero, idioma, formato FROM pelicula order by id_pelicula asc"
            resultado = self.db.obtener_datos(sentencia)
            return [Pelicula(*fila) for fila in resultado]
        except psycopg2.Error as e:
            print("Error inesperado al obtener todas las películas.")
            print(f"Detalles: {e}")
            return []

    def actualizar_pelicula(self, pelicula: Pelicula):
        try:
            sentencia = """
            UPDATE pelicula
            SET nombre = %s, director = %s, duracion = %s, genero = %s, idioma = %s, formato = %s
            WHERE id_pelicula = %s
            """
            valores = (
                pelicula.nombre,
                pelicula.director,
                pelicula.duracion,
                pelicula.genero,
                pelicula.idioma,
                pelicula.formato,
                pelicula.id_pelicula,
            )
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"Película actualizada correctamente: {pelicula.nombre}")
        except psycopg2.Error as e:
            print("Error inesperado al actualizar película.")
            print(f"Detalles: {e}")

    def eliminar_pelicula(self, id_pelicula: int):
        try:
            sentencia = "DELETE FROM pelicula WHERE id_pelicula = %s"
            self.db.ejecutar_consulta(sentencia, (id_pelicula,))
            print(f"Película con ID {id_pelicula} eliminada correctamente.")
        except psycopg2.Error as e:
            print("Error inesperado al eliminar película.")
            print(f"Detalles: {e}")

    def mostrar_peliculas(self):
        try:
            sentencia = "SELECT * FROM peliculas"
            self.db.obtener_datos(sentencia)
            return self.obtener_todas()
        except Exception as e:
            print(f"Error al mostrar películas: {e}")