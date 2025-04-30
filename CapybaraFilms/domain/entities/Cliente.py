class Cliente:
    def __init__(self, nombre, apellido, dni, eMail):
        # Constructor que inicializa los atributos del cliente
        self.nombre = nombre  # Almacena el nombre
        self.apellido = apellido  # Almacena el apellido
        self.dni = dni  # Almacena el DNI
        self.eMail = eMail  # Almacena el email

    # Métodos:
    # obtener el nombre del cliente
    def get_nombre(self):
        return self.nombre

    # Establecer un nuevo nombre al cliente
    def set_nombre(self, nombre):
        self.nombre = nombre

    # Obtener el apellido del cliente
    def get_apellido(self):
        return self.apellido

    # Establecer un nuevo apellido al cliente
    def set_apellido(self, apellido):
        self.apellido = apellido

    # Obtener el DNI del cliente
    def get_dni(self):
        return self.dni

    # Establecer un nuevo DNI al cliente
    def set_dni(self, dni):
        self.dni = dni

    # Obtener el email del cliente
    def get_email(self):
        return self.eMail

    # Establecer un nuevo email al cliente
    def set_email(self, eMail):
        self.eMail = eMail

    # Método que devuelve una representación en texto del cliente
    def __str__(self):
        return f"Cliente: \n  Nombre: {self.nombre}\n  Apellido: {self.apellido}\n  DNI: {self.dni}\n  eMail: {self.eMail}"
