from daos.ClienteDAO import ClienteDAO
from data.DatabaseConnection import DatabaseConnection
import unicodedata # Importamos la biblioteca unicodedata para manejar caracteres Unicode comocaracteres especiales.
class ServicioValidacion:
    def __init__(self):
        # Inicializamos el servicio con conexión a la base de datos y DAO de clientes.
        try:
            self.db_connection = DatabaseConnection()  # Establecemos la conexión con la base de datos.
            self.cliente_dao = ClienteDAO(self.db_connection)  # Creamos una instancia del DAO para gestionar datos de clientes.
        except Exception as e:
            # Mostramos un mensaje de error si no podemos inicializar el servicio correctamente.
            print(f"Error inicializando ServicioValidacion: {e}")

    @staticmethod
    def es_numero(cadena):
        # Este método también verifica si la cadena es un número. Es equivalente a `es_solo_digitos`.
        return cadena.isdigit()

    @staticmethod
    def es_nombre_valido(cadena):
        # Este método verifica si el nombre es válido, es decir, que solo contenga letras y espacios.
        if not cadena or not isinstance(cadena, str):  # Primero verificamos que la cadena no esté vacía y que sea un texto.
            return False
        cadena = unicodedata.normalize('NFKC', cadena)  # Normalizamos el texto para tratar caracteres especiales (ej: acentos).
        return cadena.replace(" ", "").isalpha()  # Eliminamos los espacios y verificamos que solo contenga letras.