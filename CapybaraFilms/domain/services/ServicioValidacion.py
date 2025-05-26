from domain.entities.Cliente import Cliente
from data.DatabaseConnection import DatabaseConnection

class ServicioValidacion:
    def __init__(self):
        try:
            self.db_connection = DatabaseConnection()  # Conexión a la base de datos
        except Exception as e:
            print(f"Error inicializando ServicioValidacion: {e}")

    def buscar_o_registrar_cliente(self, dni):
        """
        Busca a un cliente en la base de datos por su DNI.
        Si no está registrado, solicita los datos y lo registra.
        """
        try:
            # Buscar cliente en la base de datos
            cliente_data = self.db_connection.buscar_cliente_por_dni(dni)

            if cliente_data:
                # Cliente encontrado, crear instancia de Cliente
                cliente_fila = cliente_data[0]
                return Cliente(
                    nombre=cliente_fila[0],  # Columna 'nombre'
                    apellido=cliente_fila[1],  # Columna 'apellido'
                    dni=cliente_fila[3],  # Columna 'dni'
                    email=cliente_fila[2],  # Columna 'email'
                )
            else:
                # Cliente no encontrado, registrar nuevo
                print(f"DNI {dni} no registrado. Por favor ingrese sus datos para continuar.")
                nombre = input("Ingrese su nombre: ").strip()
                apellido = input("Ingrese su apellido: ").strip()
                while True:
                    email = input("Ingrese su correo electrónico: ").strip()
                    if "@" in email and email.endswith(".com"):
                        break
                    print("Correo electrónico inválido. Intente nuevamente.")

                # Insertar nuevo cliente
                self.db_connection.ejecutar_consulta(
                    "INSERT INTO cliente (nombre, apellido, dni, email) VALUES (%s, %s, %s, %s)",
                    (nombre, apellido, email, dni)
                )
                print(f"Cliente registrado correctamente. Bienvenido, {nombre} {apellido}.")
                return Cliente(nombre, apellido, dni, email)
        except Exception as e:
            print(f"Error en buscar_o_registrar_cliente: {e}")
            return None
    
    @staticmethod
    def es_solo_digitos(cadena):
        return cadena.isdigit()

    @staticmethod
    def es_numero(cadena):
        return cadena.isdigit()