# Importaciones necesarias para el módulo
from data.DatabaseConnection import DatabaseConnection  # Conexión a la base de datos
from domain.entities.Reserva import Reserva           # Entidad Reserva
from domain.entities.Cliente import Cliente           # Entidad Cliente
from domain.entities.Sala import Sala                 # Entidad Sala
from daos.ButacaDAO import ButacaDAO                  # DAO para manejar butacas
from daos.ClienteDAO import ClienteDAO                # DAO para manejar clientes
from datetime import datetime                         # Para manejo de fechas/horas
import psycopg2                                       # Driver PostgreSQL para manejo de errores específicos

class ReservaDAO:
    def __init__(self, db_connection: DatabaseConnection):
        """Inicializa el DAO con una conexión a la base de datos."""
        self.db = db_connection  # Almacena la conexión a la DB para todas las operaciones
        
    # Variable de clase con la fecha/hora actual formateada
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def crear_reserva(self, id_cliente: int, id_sala: int, butacas_seleccionadas: list[int]):
        """
        Crea una nueva reserva en la base de datos.
        
        Parámetros:
            id_cliente: ID del cliente que realiza la reserva
            id_sala: ID de la sala donde se realiza la reserva
            butacas_seleccionadas: Lista de IDs de butacas reservadas
            
        Retorna:
            Objeto Reserva creado o None si falla
        """
        try:
            # Validaciones de entrada
            if not id_cliente:
                raise ValueError("El ID del cliente es inválido.")
            if not id_sala:
                raise ValueError("El ID de la sala es inválido.")
            if not butacas_seleccionadas or len(butacas_seleccionadas) == 0:
                raise ValueError("La lista de butacas seleccionadas está vacía o no es válida.")

            # 1. Insertar la reserva principal
            sentencia = """
            INSERT INTO reserva (id_cliente, id_sala, fecha_hora)
            VALUES (%s, %s, NOW())
            RETURNING id_reserva
            """
            valores = (id_cliente, id_sala)
            resultado = self.db.obtener_datos(sentencia, valores)

            if not resultado:
                raise Exception("No se devolvió ningún ID al crear la reserva.")

            id_reserva = resultado[0][0]  # Obtiene el ID generado

            # 2. Insertar detalles de butacas reservadas
            for id_butaca in butacas_seleccionadas:
                sentencia_detalle = """
                INSERT INTO detalle_reserva (id_reserva, id_butaca)
                VALUES (%s, %s)
                """
                valores_detalle = (id_reserva, id_butaca)
                self.db.ejecutar_consulta(sentencia_detalle, valores_detalle)

            # 3. Obtener objetos completos para construir la reserva
            butacas_dao = ButacaDAO(self.db)
            butacas_completas = butacas_dao.buscar_por_id(butacas_seleccionadas)
            
            cliente = ClienteDAO(self.db).buscar_por_id(id_cliente)
            if not cliente:
                raise Exception(f"No se pudo encontrar el cliente con ID {id_cliente}.")

            # 4. Construir y retornar objeto Reserva
            reserva = Reserva(
                cliente=cliente,
                sala=Sala(id_sala=id_sala, id_pelicula=None),
                butacas_asignadas=butacas_completas,
                id_reserva=id_reserva
            )

            return reserva

        except Exception as e:
            print(f"Error al crear la reserva: {e}")
            return None

    def buscar_por_id(self, id_reserva: int):
        """
        Busca una reserva por su ID.
        
        Parámetros:
            id_reserva: ID de la reserva a buscar
            
        Retorna:
            Objeto Reserva encontrado o None si no existe
        """
        try:
            sentencia = """
            SELECT id_reserva, id_cliente, id_sala, fecha_hora 
            FROM reserva 
            WHERE id_reserva = %s
            """
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
        """
        Obtiene todas las reservas existentes.
        
        Retorna:
            Lista de objetos Reserva o lista vacía si no hay reservas
        """
        try:
            sentencia = """
            SELECT id_reserva, id_cliente, id_sala, fecha_hora 
            FROM reserva
            """
            resultado = self.db.obtener_datos(sentencia)
            
            if not resultado:
                print("No se encontraron reservas.")
                return []
                
            print(f"Se encontraron {len(resultado)} reservas.")
            return [Reserva(*fila) for fila in resultado]
            
        except psycopg2.Error as e:
            print("Error al obtener reservas.")
            print(f"Detalles: {e}")
            return []

    def eliminar_reserva(self, id_reserva: int):
        """
        Elimina una reserva por su ID.
        
        Parámetros:
            id_reserva: ID de la reserva a eliminar
        """
        try:
            sentencia = "DELETE FROM reserva WHERE id_reserva = %s"
            self.db.ejecutar_consulta(sentencia, (id_reserva,))
            print(f"Reserva con ID {id_reserva} eliminada correctamente.")
            
        except psycopg2.Error as e:
            print("Error al eliminar reserva.")
            print(f"Detalles: {e}")