from data.DatabaseConnection import DatabaseConnection
from domain.entities.Candy import Candy
from domain.entities.types.TipoCandy import TipoCandy

class DetalleCandyDAO:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection

    def agregar_detalle(self, id_reserva: int, id_candy: int, cantidad: int = 1):
        sentencia = """
        INSERT INTO detalle_candy (id_reserva, id_candy, cantidad)
        VALUES (%s, %s, %s)
        """
        valores = (id_reserva, id_candy, cantidad)
        self.db.ejecutar_consulta(sentencia, valores)

    def obtener_por_reserva(self, id_reserva: int):
        try:
            sentencia = """
            SELECT dc.id_detalle, dc.id_reserva, dc.id_candy, dc.cantidad, c.descripcion, c.precio
            FROM detalle_candy dc
            JOIN candy c ON dc.id_candy = c.id_candy
            WHERE dc.id_reserva = %s
            """ # consultamos la tabla detalle_candy y la tabla candy
            resultado = self.db.obtener_datos(sentencia, (id_reserva,))
            detalles = []
            for fila in resultado:
                # Crear objetos Candy directamente
                candy = Candy(
                    id_candy=fila[2],
                    tipo=TipoCandy[fila[4].upper()],
                    cantidad=fila[3],
                )
                detalles.append(candy)
            return detalles
        except Exception as e:
            print(f"Error al obtener detalles por reserva: {e}")
            return []

    def eliminar_detalles_por_reserva(self, id_reserva: int):
        query = "DELETE FROM detalle_candy WHERE id_reserva = %s"
        self.db.ejecutar_consulta(query, (id_reserva,))