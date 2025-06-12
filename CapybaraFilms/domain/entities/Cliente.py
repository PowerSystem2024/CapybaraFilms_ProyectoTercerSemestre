import psycopg2

class Cliente:
    def __init__(self, id_cliente=None, dni=None, nombre=None, apellido=None, email=None):
        self.id_cliente = id_cliente
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

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
        return f"Cliente({self.id_cliente}, {self.dni}, {self.nombre}, {self.apellido}, {self.email})"
