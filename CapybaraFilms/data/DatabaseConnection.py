import psycopg2
from psycopg2 import OperationalError, DatabaseError
from contextlib import contextmanager
class DatabaseConnection:
    def __init__(self, database="railway", user="postgres", password="eeNfeLjGqTumwIOKqEDCVTjqHnUzpnuX", host="crossover.proxy.rlwy.net", port="55022"):
        """
        Constructor de la conexión a la base de datos.
        Se inicializa con los parámetros para conectarse a PostgreSQL.

        :param database: Nombre de la base de datos.
        :param user: Usuario de la base de datos.
        :param password: Contraseña del usuario.
        :param host: Dirección del servidor (local o remoto).
        :param port: Puerto del servidor PostgreSQL.
        """
        self.connection = None
        self.cursor = None
        self.config = {
            "database": database,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }
        # Intentar conexión al inicializar la clase
        self._conectar()

    def _conectar(self):
        """Realiza la conexión inicial a la base de datos."""
        try:
            self.connection = psycopg2.connect(**self.config) # ** se usa para desempaquetar el diccionario de configuración
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
        except OperationalError as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None
            self.cursor = None
            exit(1)

    def _validar_conexion_activa(self):
        """Verifica si la conexión y el cursor están activos."""
        if not self.connection or self.connection.closed:
            print("La conexión no está activa. Intentando reconectar...")
            self._conectar()
        if not self.cursor:
            self.cursor = self.connection.cursor()
            
    @contextmanager
    def manejar_cursor(self): # Aunque trabajamos con WITH, no necesitamos usarlo de forma explícita en nuestro código principal porque el manejo del contexto ya está embebido en este método.
        """Manejador de cursor con 'context manager'."""
        try:
            self._validar_conexion_activa()
            yield self.cursor # yield funciona como retorno temporal del cursor
            self.connection.commit()  # Confirmar cambios (si aplica)
        except Exception as e:
            self.connection.rollback()  # Deshacer cambios en caso de error
            raise e # raise re-lanza la excepción para que pueda ser manejada por el llamador
        finally:
            self.cursor.close()
            self.cursor = self.connection.cursor()  # Reabrir el cursor para próximas operaciones

    def ejecutar_consulta(self, consulta, valores=None):
        """
        Ejecuta una consulta SQL y confirma cambios en la base de datos.
        """
        try:
            with self.manejar_cursor() as cursor:
                cursor.execute(consulta, valores)
                self.connection.commit()
        except OperationalError as e:
            print(f"Error operacional durante la consulta: {e}")
        except DatabaseError as e:
            print(f"Error en la base de datos: {e}")
        except Exception as e:
            print(f"Error al ejecutar consulta ({consulta}): {e}")

    def obtener_datos(self, consulta, valores=None):
        """
        Ejecuta una consulta SQL para obtener datos y devuelve el resultado.

        :param consulta: Consulta SQL a ejecutar.
        :param params: Tupla con los parámetros opcionales para la consulta.
        :return: Lista de filas devueltas por la consulta.
        """
        try:
            with self.manejar_cursor() as cursor:
                cursor.execute(consulta, valores)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return []

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos de forma segura."""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
                print("Conexión cerrada correctamente.")
        except Exception as e:
            print(f"Error cerrando conexión: {e}")