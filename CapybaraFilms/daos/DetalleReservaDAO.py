# Importa la clase DatabaseConnection que maneja la conexión con la base de datos
from data.DatabaseConnection import DatabaseConnection

# Clase encargada de manejar operaciones sobre la tabla detalle_reserva
class DetalleReservaDAO:

    # Constructor que recibe una conexión a la base de datos
    def __init__(self, db_connection):
        self.db = db_connection  # Se guarda la conexión para usarla en los métodos del DAO

    # Método para agregar un nuevo detalle de reserva (asociar una butaca a una reserva)
    def agregar_detalle(self, id_reserva: int, id_butaca: int):
        try:
            # Consulta SQL para insertar un nuevo registro en detalle_reserva
            sentencia = """
            INSERT INTO detalle_reserva (id_reserva, id_butaca)
            VALUES (%s, %s)
            """
            # Tupla con los valores que se van a insertar
            valores = (id_reserva, id_butaca)
            # Ejecuta la consulta usando el método de la conexión
            self.db.ejecutar_consulta(sentencia, valores)
        except Exception as e:
            # Si ocurre un error, se muestra en consola
            print(f"Error al agregar detalle de reserva: {e}")

    # Método para obtener todos los detalles de una reserva específica
    def obtener_por_reserva(self, id_reserva: int):
        try:
            # Consulta SQL con JOIN para traer detalles y datos de la butaca asociada
            sentencia = """
            SELECT dr.id_detalle, dr.id_reserva, dr.id_butaca, b.fila, b.columna, b.id_sala, b.categoria, b.estado
            FROM detalle_reserva dr
            JOIN butaca b ON dr.id_butaca = b.id_butaca
            WHERE dr.id_reserva = %s
            """
            # Ejecuta la consulta con el ID de la reserva como parámetro
            resultado = self.db.obtener_datos(sentencia, (id_reserva,))
            
            detalles = []  # Lista donde se almacenarán los resultados
            
            # Recorre los resultados y construye un diccionario por cada fila
            for fila in resultado:
                detalles.append({
                    "id_detalle": fila[0],
                    "id_reserva": fila[1],
                    "id_butaca": fila[2],
                    "butaca": {
                        "fila": fila[3],
                        "columna": fila[4],
                        "id_sala": fila[5],
                        "categoria": fila[6],
                        "estado": fila[7]
                    }
                })
            
            # Devuelve la lista con todos los detalles encontrados
            return detalles
        
        except Exception as e:
            # Si algo falla, se muestra el error y se devuelve una lista vacía
            print(f"Error al obtener detalles por reserva: {e}")
            return []

    # Método para eliminar todos los detalles asociados a una reserva en particular
    def eliminar_detalles_por_reserva(self, id_reserva: int):
        # Consulta SQL para eliminar todos los registros con ese id_reserva
        sql = "DELETE FROM detalle_reserva WHERE id_reserva = %s"
        # Ejecuta la consulta usando el método de la conexión
        self.db.ejecutar_consulta(sql, (id_reserva,))
