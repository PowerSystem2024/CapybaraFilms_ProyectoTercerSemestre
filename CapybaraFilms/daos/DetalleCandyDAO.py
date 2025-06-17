# Importamos la clase de conexión a la base de datos
from data.DatabaseConnection import DatabaseConnection

# Importamos las entidades necesarias: Candy y su tipo (TipoCandy)
from domain.entities.Candy import Candy
from domain.entities.types.TipoCandy import TipoCandy

# Clase encargada de gestionar el acceso a los datos de la tabla detalle_candy
class DetalleCandyDAO:
    def __init__(self, db_connection: DatabaseConnection):
        # Recibe una instancia de conexión a la base de datos
        self.db = db_connection

    # Método para agregar un detalle de candy a una reserva
    def agregar_detalle(self, id_reserva: int, id_candy: int, cantidad: int = 1):
        sentencia = """
        INSERT INTO detalle_candy (id_reserva, id_candy, cantidad)
        VALUES (%s, %s, %s)
        """
        valores = (id_reserva, id_candy, cantidad)
        # Ejecutamos la consulta usando el método correspondiente del objeto de base de datos
        self.db.ejecutar_consulta(sentencia, valores)

    # Método para obtener todos los detalles de candy asociados a una reserva específica
    def obtener_por_reserva(self, id_reserva: int):
        try:
            sentencia = """
            SELECT dc.id_detalle, dc.id_reserva, dc.id_candy, dc.cantidad, c.descripcion, c.precio
            FROM detalle_candy dc
            JOIN candy c ON dc.id_candy = c.id_candy
            WHERE dc.id_reserva = %s
            """  # Consultamos la tabla detalle_candy unida a la tabla candy

            resultado = self.db.obtener_datos(sentencia, (id_reserva,))
            detalles = []

            for fila in resultado:
                # Creamos un objeto Candy para cada resultado
                candy = Candy(
                    id_candy=fila[2],
                    tipo=TipoCandy[fila[4].upper()],  # Convertimos la descripción en un tipo de Enum
                    cantidad=fila[3],
                )
                detalles.append(candy)

            return detalles
        except Exception as e:
            # En caso de error, mostramos un mensaje y devolvemos una lista vacía
            print(f"Error al obtener detalles por reserva: {e}")
            return []

    # Método para eliminar todos los detalles de candy relacionados con una reserva
    def eliminar_detalles_por_reserva(self, id_reserva: int):
        query = "DELETE FROM detalle_candy WHERE id_reserva = %s"
        self.db.ejecutar_consulta(query, (id_reserva,))