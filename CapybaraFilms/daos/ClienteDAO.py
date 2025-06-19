from data.DatabaseConnection import DatabaseConnection
from domain.entities.Cliente import Cliente
import psycopg2

class ClienteDAO:
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection

    def crear_cliente(self, cliente: Cliente):
        from services.ServicioValidacion import ServicioValidacion

        try:
            if not ServicioValidacion.es_nombre_valido(cliente.nombre):
                print(f"❌ Nombre inválido: {cliente.nombre}. No se registrará el cliente.")
                return
            if not ServicioValidacion.es_nombre_valido(cliente.apellido):
                print(f"❌ Apellido inválido: {cliente.apellido}. No se registrará el cliente.")
                return

            # Verificar si el cliente ya existe
            cliente_existente = self.buscar_por_dni(cliente.dni)
            if cliente_existente:
                print(f"❌ Ya existe un cliente registrado con este DNI: {cliente.dni}.")
                return
            # Si no existe, proceder a crear el cliente
            sentencia = """
            INSERT INTO cliente (dni, nombre, apellido, email)
            VALUES (%s, %s, %s, %s)
            RETURNING id_cliente
            """
            valores = (cliente.dni, cliente.nombre, cliente.apellido, cliente.email)
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"✔ Cliente creado correctamente: {cliente.nombre} {cliente.apellido}")
        except psycopg2.IntegrityError as e:
            print("❌ Error al crear cliente: Violación de integridad en la base de datos.")
            print(f"Detalles: {e}")
        except psycopg2.Error as e:
            print("❌ Error inesperado al crear cliente.")
            print(f"Detalles: {e}")

    def buscar_por_dni(self, dni: str):
        try:
            sentencia = "SELECT id_cliente, dni, nombre, apellido, email FROM cliente WHERE dni = %s"
            resultado = self.db.obtener_datos(sentencia, (dni,))
            if resultado:
                fila = resultado[0]
                return Cliente(fila[0], fila[1], fila[2], fila[3], fila[4])
            return None
        except psycopg2.Error as e:
            print("Error inesperado al buscar cliente por DNI.")
            print(f"Detalles: {e}")
            return None

    def obtener_todos(self):
        try:
            sentencia = "SELECT id_cliente, dni, nombre, apellido, email FROM cliente"
            resultado = self.db.obtener_datos(sentencia)
            return [Cliente(fila[0], fila[1], fila[2], fila[3], fila[4]) for fila in resultado]
        except psycopg2.Error as e:
            print("Error inesperado al obtener todos los clientes.")
            print(f"Detalles: {e}")
            return []

    def actualizar_cliente(self, cliente: Cliente):
        try:
            sentencia = """
            UPDATE cliente
            SET nombre = %s, apellido = %s, email = %s
            WHERE dni = %s
            """
            valores = (cliente.nombre, cliente.apellido, cliente.email, cliente.dni)
            self.db.ejecutar_consulta(sentencia, valores)
            print("Cliente actualizado correctamente.")
        except psycopg2.Error as e:
            print("Error inesperado al actualizar cliente.")
            print(f"Detalles: {e}")

    def eliminar_cliente(self, dni: str):
        try:
            sentencia = "DELETE FROM cliente WHERE dni = %s"
            valores = (dni,)
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"Cliente con DNI {dni} eliminado correctamente.")
        except psycopg2.Error as e:
            print("Error inesperado al eliminar cliente.")
            print(f"Detalles: {e}")
            
    def buscar_por_id(self, id_cliente: int):
        """
        Busca un cliente en la base de datos utilizando su ID y devuelve un objeto Cliente.
        """
        sentencia = """
        SELECT id_cliente, dni, nombre, apellido, email
        FROM cliente
        WHERE id_cliente = %s
        """
        try:
            resultado = self.db.obtener_datos(sentencia, (id_cliente,))
            if resultado:
                fila = resultado[0]  # Selecciona la primera fila devuelta
                # Crear un objeto Cliente con los datos obtenidos
                return Cliente(
                    id_cliente=fila[0],
                    dni=fila[1],
                    nombre=fila[2],
                    apellido=fila[3],
                    email=fila[4]
                )
            else:
                print(f"No se encontró ningún cliente con ID {id_cliente}.")
                return None
        except Exception as e:
            print(f"Error al buscar cliente por ID: {e}")
            return None