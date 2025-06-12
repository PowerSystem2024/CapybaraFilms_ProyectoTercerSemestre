from data.DatabaseConnection import DatabaseConnection
from domain.entities.Reserva import Reserva
from domain.entities.Cliente import Cliente
from domain.entities.Sala import Sala
from daos.ButacaDAO import ButacaDAO
from daos.ClienteDAO import ClienteDAO
from datetime import datetime

import psycopg2

class ReservaDAO:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection
        
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def crear_reserva(self, id_cliente: int, id_sala: int, butacas_seleccionadas: list[int]):
        try:
            if not id_cliente:
                raise ValueError("El ID del cliente es inválido.")
            if not id_sala:
                raise ValueError("El ID de la sala es inválido.")
            if not butacas_seleccionadas or len(butacas_seleccionadas) == 0:
                raise ValueError("La lista de butacas seleccionadas está vacía o no es válida.")

            # Insertar en la tabla `reserva` (la fecha/hora automáticamente se genera con `NOW`)
            sentencia = """
            INSERT INTO reserva (id_cliente, id_sala, fecha_hora)
            VALUES (%s, %s, NOW())
            RETURNING id_reserva
            """
            valores = (id_cliente, id_sala)
            resultado = self.db.obtener_datos(sentencia, valores)

            if not resultado:
                raise Exception("No se devolvió ningún ID al crear la reserva.")

            id_reserva = resultado[0][0]

            # Insertar registros en "detalle_reserva" para las butacas seleccionadas
            for id_butaca in butacas_seleccionadas:
                sentencia_detalle = """
                INSERT INTO detalle_reserva (id_reserva, id_butaca)
                VALUES (%s, %s)
                """
                valores_detalle = (id_reserva, id_butaca)
                self.db.ejecutar_consulta(sentencia_detalle, valores_detalle)

                # Transformar IDs en objetos Butaca utilizando el DAO
                butacas_dao = ButacaDAO(self.db)
                butacas_completas = butacas_dao.buscar_por_id(butacas_seleccionadas)
                
                cliente = ClienteDAO(self.db).buscar_por_id(id_cliente)
                if not cliente:
                    raise Exception(f"No se pudo encontrar el cliente con ID {id_cliente}.")

            # Crear objeto Reserva
            reserva = Reserva(
                cliente=cliente,
                sala=Sala(id_sala=id_sala, id_pelicula=None),
                butacas_asignadas=butacas_completas,  # Usar objetos `Butaca` completos
                id_reserva=id_reserva
            )

            return reserva

        except Exception as e:
            print(f"Error al crear la reserva: {e}")
            return None

    def buscar_por_id(self, id_reserva: int):
        try:
            sentencia = "SELECT id_reserva, id_cliente, id_sala, fecha_hora FROM reserva WHERE id_reserva = %s"
            resultado = self.db.obtener_datos(sentencia, (id_reserva,))
            if resultado:
                fila = resultado[0]
                return Reserva(fila[0], fila[1], fila[2], fila[3])
            print(f"No se encontró ninguna reserva con ID {id_reserva}.")
            return None
        except psycopg2.Error as e:
            print("Error al buscar reserva.")
            print(f"Detalles: {e}")
            return None

    def obtener_todas(self):
        try:
            sentencia = "SELECT id_reserva, id_cliente, id_sala, fecha_hora FROM reserva"
            resultado = self.db.obtener_datos(sentencia)
            if not resultado:
                print("No se encontraron reservas.")
                return []
            print(f"Se encontraron {len(resultado)} reservas.")
            print("Detalles de las reservas:")
            for fila in resultado:
                print(f"ID Reserva: {fila[0]}, Cliente ID: {fila[1]}, Sala ID: {fila[2]}, Fecha y Hora: {fila[3]}")
            return [Reserva(*fila) for fila in resultado]
        except psycopg2.Error as e:
            print("Error al obtener reservas.")
            print(f"Detalles: {e}")
            return []

    def eliminar_reserva(self, id_reserva: int):
        try:
            sentencia = "DELETE FROM reserva WHERE id_reserva = %s"
            self.db.ejecutar_consulta(sentencia, (id_reserva,))
            print(f"Reserva con ID {id_reserva} eliminada correctamente.")
        except psycopg2.Error as e:
            print("Error al eliminar reserva.")
            print(f"Detalles: {e}")