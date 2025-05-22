import psycopg2
class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="capybara_films",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            self.cursor = None
            print("No se pudo establecer la conexión con la base de datos.")
            exit(1)

    def obtener_datos(self, consulta, params=None):
        if not self.cursor:
            print("No se pudo ejecutar la consulta porque la conexión no está activa.")
            return []
        try:
            self.cursor.execute(consulta, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return []

    def ejecutar_consulta(self, consulta, params=None):
        if not self.connection:
            print("No se pudo ejecutar la consulta porque la conexión no está activa.")
            return
        try:
            self.cursor.execute(consulta, params)
            self.connection.commit()
        except Exception as e:
            print(f"Error al ejecutar consulta: {e}")
            if self.connection:
                self.connection.rollback()

    def buscar_cliente_por_dni(self, dni):
        if not self.cursor:
            print("La conexión no está activa. No se puede buscar al cliente.")
            return []
        try:
            consulta = "SELECT * FROM cliente WHERE dni = %s"
            return self.obtener_datos(consulta, (dni,))
        except Exception as e:
            print(f"Error buscando cliente por DNI: {e}")
            return []

    def cerrar_conexion(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Conexión cerrada.")
        except Exception as e:
            print(f"Error cerrando conexión: {e}")