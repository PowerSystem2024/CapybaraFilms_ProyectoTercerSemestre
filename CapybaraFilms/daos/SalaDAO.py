from domain.entities.Sala import Sala
from data.DatabaseConnection import DatabaseConnection
import psycopg2

class SalaDAO:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection

    def crear_sala(self, sala: Sala):
        """
        Crear una sala con una capacidad fija de 12x12 (144 asientos).
        """
        try:
            sentencia = """
            INSERT INTO sala (nombre, id_pelicula)
            VALUES (%s, %s)
            """
            valores = (sala.nombre, sala.id_pelicula)
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"✔ Sala creada correctamente: {sala.nombre})")
        except psycopg2.Error as e:
            print("❌ Error inesperado al crear sala.")
            print(f"Detalles: {e}")
            
    def buscar_por_id(self, id_sala: int):
        try:
            sentencia = "SELECT id_sala, nombre, capacidad, id_pelicula FROM sala WHERE id_sala = %s"
            resultado = self.db.obtener_datos(sentencia, (id_sala,))
            if resultado:
                fila = resultado[0]
                return Sala(fila[0], fila[1], fila[2], fila[3])
            print(f"No se encontró ninguna sala con ID {id_sala}.")
            return None
        except psycopg2.Error as e:
            print("Error inesperado al buscar sala.")
            print(f"Detalles: {e}")
            return None

    def obtener_todas(self):
        try:
            sentencia = "SELECT id_sala, nombre, capacidad, id_pelicula FROM sala"
            resultado = self.db.obtener_datos(sentencia)
            return [Sala(fila[0], fila[1], fila[2], fila[3]) for fila in resultado]
        except psycopg2.Error as e:
            print("Error al obtener todas las salas.")
            print(f"Detalles: {e}")
            return []

    def buscar_por_pelicula(self, id_pelicula: int):
        try:
            sentencia = "SELECT id_sala, id_pelicula FROM sala WHERE id_pelicula = %s"
            resultado = self.db.obtener_datos(sentencia, (id_pelicula,))
            return [Sala(fila[0], fila[1]) for fila in resultado]
        except psycopg2.Error as e:
            print("Error inesperado al buscar salas por película.")
            print(f"Detalles: {e}")
            return []

    def eliminar_sala(self, id_sala: int):
        try:
            sentencia = "DELETE FROM sala WHERE id_sala = %s"
            self.db.ejecutar_consulta(sentencia, (id_sala,))
            print(f"Sala con ID {id_sala} eliminada correctamente.")
        except psycopg2.Error as e:
            print("Error inesperado al eliminar sala.")
            print(f"Detalles: {e}")