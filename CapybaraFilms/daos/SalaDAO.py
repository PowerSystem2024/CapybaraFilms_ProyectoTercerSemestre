# Importa la clase Sala desde el paquete 'domain.entities'
from domain.entities.Sala import Sala

# Importa la clase DatabaseConnection que maneja la conexión a la base de datos
from data.DatabaseConnection import DatabaseConnection

# Importa el módulo psycopg2 para manejar errores de PostgreSQL
import psycopg2

# Definición de la clase SalaDAO (Data Access Object), encargada de interactuar con la tabla 'sala' en la base de datos
class SalaDAO:
    
    # Constructor de la clase que recibe una instancia de DatabaseConnection
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection  # Guarda la conexión a la base de datos para usarla en los métodos del DAO

    # Método para crear una nueva sala en la base de datos
    def crear_sala(self, sala: Sala):
        """
        Crear una sala con una capacidad fija de 12x12 (144 asientos).
        """
        try:
            # Consulta SQL para insertar una nueva sala
            sentencia = """
            INSERT INTO sala (nombre, id_pelicula)
            VALUES (%s, %s)
            """
            # Tupla con los valores a insertar: nombre de la sala y id de la película asignada
            valores = (sala.nombre, sala.id_pelicula)
            
            # Ejecuta la consulta usando el método definido en DatabaseConnection
            self.db.ejecutar_consulta(sentencia, valores)
            print(f"✔ Sala creada correctamente: {sala.nombre})")
        
        # Manejo de errores si ocurre un problema con la base de datos
        except psycopg2.Error as e:
            print("❌ Error inesperado al crear sala.")
            print(f"Detalles: {e}")

    # Método para buscar una sala por su ID
    def buscar_por_id(self, id_sala: int):
        try:
            # Consulta SQL para buscar una sala por su identificador
            sentencia = "SELECT id_sala, nombre, capacidad, id_pelicula FROM sala WHERE id_sala = %s"
            # Ejecuta la consulta y obtiene los datos
            resultado = self.db.obtener_datos(sentencia, (id_sala,))
            
            # Si se encontró una fila, se construye y devuelve un objeto Sala
            if resultado:
                fila = resultado[0]
                return Sala(fila[0], fila[1], fila[2], fila[3])
            
            # Si no se encontró, muestra mensaje y devuelve None
            print(f"No se encontró ninguna sala con ID {id_sala}.")
            return None
        
        # Captura errores de la base de datos
        except psycopg2.Error as e:
            print("Error inesperado al buscar sala.")
            print(f"Detalles: {e}")
            return None

    # Método para obtener todas las salas registradas en la base de datos
    def obtener_todas(self):
        try:
            # Consulta SQL que selecciona todos los campos necesarios de todas las salas
            sentencia = "SELECT id_sala, nombre, capacidad, id_pelicula FROM sala"
            # Ejecuta la consulta
            resultado = self.db.obtener_datos(sentencia)
            # Retorna una lista de objetos Sala creados a partir de los resultados
            return [Sala(fila[0], fila[1], fila[2], fila[3]) for fila in resultado]
        
        # Captura errores si algo sale mal
        except psycopg2.Error as e:
            print("Error al obtener todas las salas.")
            print(f"Detalles: {e}")
            return []

    # Método para buscar todas las salas asociadas a una película en particular
    def buscar_por_pelicula(self, id_pelicula: int):
        try:
            # Consulta SQL que selecciona las salas que proyectan una película específica
            sentencia = "SELECT id_sala, id_pelicula FROM sala WHERE id_pelicula = %s"
            resultado = self.db.obtener_datos(sentencia, (id_pelicula,))
            # Retorna una lista de objetos Sala (solo con id_sala e id_pelicula)
            return [Sala(fila[0], fila[1]) for fila in resultado]
        
        # Manejo de errores ante problemas en la consulta
        except psycopg2.Error as e:
            print("Error inesperado al buscar salas por película.")
            print(f"Detalles: {e}")
            return []

    # Método para eliminar una sala de la base de datos por su ID
    def eliminar_sala(self, id_sala: int):
        try:
            # Consulta SQL para eliminar la sala con el ID dado
            sentencia = "DELETE FROM sala WHERE id_sala = %s"
            # Ejecuta la consulta de eliminación
            self.db.ejecutar_consulta(sentencia, (id_sala,))
            print(f"Sala con ID {id_sala} eliminada correctamente.")
        
        # Captura errores durante la eliminación
        except psycopg2.Error as e:
            print("Error inesperado al eliminar sala.")
            print(f"Detalles: {e}")
