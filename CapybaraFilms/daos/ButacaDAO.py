import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from data.DatabaseConnection import DatabaseConnection
from domain.entities.Butaca import Butaca
from domain.entities.types.Ubicacion import Ubicacion
import psycopg2

class ButacaDAO:
    def __init__(self, db_connection: DatabaseConnection): # Aqui se recibe la conexión a la base de datos
        self.db = db_connection

    def buscar_por_id(self, id_butacas: list[int]): #Busca una lista de butacas por sus IDs
        sentencia = f"""
        SELECT id_butaca, fila, columna, categoria, precio
        FROM butaca
        WHERE id_butaca IN ({','.join(['%s'] * len(id_butacas))})
        """
        resultado = self.db.obtener_datos(sentencia, tuple(id_butacas))
        return [Butaca(*fila) for fila in resultado] #Crea una lista de objetos Butaca a partir del resultado

    def obtener_por_sala(self, id_sala):
        #Devuelve una lista de butacas correspondientes a una sala
        try:
            sentencia = "SELECT fila, columna, id_butaca, categoria, estado FROM butaca WHERE id_sala = %s"
            resultado = self.db.obtener_datos(sentencia, (id_sala,))
            # Validar el contenido de cada fila
            for fila in resultado: # si el resultado es una lista de tuplas, cada fila debe ser una tupla
                if not isinstance(fila[0], int) or not isinstance(fila[1], int) or \
                    not isinstance(fila[2], int) or not isinstance(fila[3], str) or \
                    not isinstance(fila[4], bool): # Verifica que los tipos de datos sean correctos
                    print(f"Datos inválidos en fila: {fila}")
                    continue  # Saltar filas no válidas

            return [Butaca(
                        fila[3],                      # devuelve la categoria
                        Ubicacion(fila[0], fila[1], fila[2]),  # fila, columna, id butaca
                        fila[4]                       # y el estado
                    ) for fila in resultado]
        except Exception as e:
            print(f"Error al obtener las butacas para la sala con ID {id_sala}: {e}")
            return []

    def actualizar_butaca(self, butaca: Butaca):
        #Actualiza los datos completos de una butaca en la base de datos
        try:
            sentencia = """
            UPDATE butaca
            SET fila = %s, columna = %s, id_sala = %s, categoria = %s, estado = %s
            WHERE id_butaca = %s
            """
            valores = (butaca.ubicacion.fila, butaca.columna, butaca.id_sala, butaca.categoria, butaca.estado, butaca.id_butaca)
            self.db.ejecutar_consulta(sentencia, valores)
        except psycopg2.Error as e:
            print("Error al actualizar la butaca.")
            print(f"Detalles: {e}")
        
    def actualizar_estado(self, id_butaca: int, estado: bool):
        #Actualiza solo el estado, ocupada o libre, de una butaca
        try:
            sentencia = "UPDATE butaca SET estado = %s WHERE id_butaca = %s"
            self.db.ejecutar_consulta(sentencia, (estado, id_butaca))
            print(f"Butaca seleccionada {'Ocupada' if estado else 'Libre'}.")
        except psycopg2.Error as e:
            print("Error al actualizar el estado de la butaca.")
            print(f"Detalles: {e}")
    
    def butacas_por_sala(self, id_sala: int):

        # Obtiene todas las butacas de una sala específica.

        try:
            sentencia = "SELECT id_butaca, fila, columna, categoria, estado FROM butaca WHERE id_sala = %s"
            resultado = self.db.obtener_datos(sentencia, (id_sala,)) 
            return [Butaca(fila[0], fila[1], fila[2], fila[3], fila[4]) for fila in resultado]
        except psycopg2.Error as e:
            print("Error al obtener las butacas por sala.")
            print(f"Detalles: {e}")
            return []
        
    def cantidad_butacas_disponibles(self, id_sala: int) -> int:

        # Cuenta la cantidad de butacas disponibles en una sala específica.

        try:
            sentencia = "SELECT COUNT(*) FROM butaca WHERE id_sala = %s AND estado = TRUE"
            resultado = self.db.obtener_datos(sentencia, (id_sala,))
            return resultado[0][0] if resultado else 0
        except psycopg2.Error as e:
            print("Error al contar las butacas disponibles.")
            print(f"Detalles: {e}")
            return 0

    #    def eliminar_butaca(self, id_butaca: int):
    #    query = "DELETE FROM butaca WHERE id_butaca = %s"
    #    self.db.ejecutar_consulta(query, (id_butaca,))