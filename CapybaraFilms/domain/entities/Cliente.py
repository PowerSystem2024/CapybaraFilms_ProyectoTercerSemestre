import psycopg2

class Cliente:
    def __init__(self, nombre, apellido, dni, email):

        # Constructor que inicializa los atributos del cliente
        self.nombre = nombre  # Almacena el nombre
        self.apellido = apellido  # Almacena el apellido
        self.dni = dni  # Almacena el DNI
        self.email = email  # Almacena el email


    # Métodos:
    # obtener el nombre del cliente
    def get_nombre(self):
        return self.nombre

    # Establecer un nuevo nombre al cliente
    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre

    # Obtener el apellido del cliente
    def get_apellido(self):
        return self.apellido

    # Establecer un nuevo apellido al cliente
    def set_apellido(self, apellido):
        if not apellido.strip():
            raise ValueError("El apellido no puede estar vacío.")
        self.apellido = apellido

    # Obtener el DNI del cliente
    def get_dni(self):
        return self.dni

    # Establecer un nuevo DNI al cliente
    def set_dni(self, dni):
        if not str(dni).isdigit():
            raise ValueError("El DNI debe contener solo números.")
        self.dni = dni

    # Obtener el email del cliente
    def get_email(self):
        return self.email

    # Establecer un nuevo email al cliente
    def set_email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError("El email no es valido.")
        self.email = email

    # Método que devuelve una representación en texto del cliente
    def __str__(self):
        return f"Cliente: \n  Nombre: {self.nombre}\n  Apellido: {self.apellido}\n  DNI: {self.dni}\n  email: {self.email}"


# ----------------------------------------
# BASE DE DATOS
# ----------------------------------------

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            dbname="capybara_films",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

def guardar_cliente_en_bd(cliente):
    conn = conectar_bd()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO cliente (nombre, apellido, dni, "email")
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (cliente.get_nombre(), cliente.get_apellido(), cliente.get_dni(), cliente.get_email()))
            conn.commit()
            cursor.close()
            conn.close()
            print("Cliente guardado correctamente.")
        except Exception as e:
            print("Error al guardar el cliente:", e)

#cliente1 = Cliente("Maria", "Acosta", "42338065", "macosta23@email.com")
#guardar_cliente_en_bd(cliente1)
