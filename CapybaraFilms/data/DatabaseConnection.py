import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="capybara_films_db", # todavia no esta creada
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        self.cursor = self.connection.cursor() # Cursor para ejecutar consultas

    def ejecutar_consulta(self, consulta, params=None): # Ejecutamos una consulta SQL
        try:
            self.cursor.execute(consulta, params) # Ejecutamos la consulta SQL
            # Si la consulta es de tipo INSERT, UPDATE o DELETE, se hace commit
            self.connection.commit()
        except Exception as e:
            print(f"Error realizando consulta: {e}")
            self.connection.rollback()

    def obtener_datos(self, consulta, params=None): # Obtenemos datos de la base de datos
        try:
            self.cursor.execute(consulta, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error obteniendo datos: {e}")
            return [] # Retornamos una lista vacia en caso de error

    def cerrar_conexion(self): # Cerramos la conexión a la base de datos
        self.cursor.close()
        self.connection.close()