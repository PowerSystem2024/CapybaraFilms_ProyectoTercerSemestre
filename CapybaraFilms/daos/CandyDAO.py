from data.DatabaseConnection import DatabaseConnection
from domain.entities.Candy import Candy
from domain.entities.types.TipoCandy import TipoCandy

class CandyDAO:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection

    def crear_candy(self, candy: Candy):
        try:
            sentencia = """
            INSERT INTO candy (descripcion, precio)
            VALUES (%s, %s)
            """
            valores = (candy.descripcion, candy.precio)
            self.db.ejecutar_consulta(sentencia, valores)
        except Exception as e:
            print(f"Error al crear candy: {e}")

    def buscar_por_id(self, id_candy: int):
        try:
            sentencia = "SELECT id_candy, descripcion, precio FROM candy WHERE id_candy = %s"
            resultado = self.db.obtener_datos(sentencia, (id_candy,))
            if resultado:
                return Candy(*resultado[0])
            return None
        except Exception as e:
            print(f"Error al buscar candy por ID {id_candy}: {e}")
            return None

    def obtener_todos(self):
        try:
            sentencia = "SELECT id_candy, descripcion, precio FROM candy"
            resultado = self.db.obtener_datos(sentencia)
            return [Candy(*fila) for fila in resultado]
        except Exception as e:
            print(f"Error al obtener todos los candies: {e}")
            return []
        
    def eliminar_candy(self, id_candy: int):
        sql = "DELETE FROM candy WHERE id_candy = %s"
        self.db.ejecutar_consulta(sql, (id_candy,))