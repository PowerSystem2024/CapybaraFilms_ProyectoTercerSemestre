from data.DatabaseConnection import DatabaseConnection

class DetalleReservaDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def agregar_detalle(self, id_reserva: int, id_butaca: int):
        try:
            sentencia = """
            INSERT INTO detalle_reserva (id_reserva, id_butaca)
            VALUES (%s, %s)
            """
            valores = (id_reserva, id_butaca)
            self.db.ejecutar_consulta(sentencia, valores)
        except Exception as e:
            print(f"Error al agregar detalle de reserva: {e}")

    def obtener_por_reserva(self, id_reserva: int):
        try:
            sentencia = """
            SELECT dr.id_detalle, dr.id_reserva, dr.id_butaca, b.fila, b.columna, b.id_sala, b.categoria, b.estado
            FROM detalle_reserva dr
            JOIN butaca b ON dr.id_butaca = b.id_butaca
            WHERE dr.id_reserva = %s
            """
            resultado = self.db.obtener_datos(sentencia, (id_reserva,))
            detalles = []
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
            return detalles
        except Exception as e:
            print(f"Error al obtener detalles por reserva: {e}")
            return []

    def eliminar_detalles_por_reserva(self, id_reserva: int):
        sql = "DELETE FROM detalle_reserva WHERE id_reserva = %s"
        self.db.ejecutar_consulta(sql, (id_reserva,))