from domain.entities.Cliente import Cliente
from daos.ClienteDAO import ClienteDAO
from data.DatabaseConnection import DatabaseConnection
import unicodedata


class ServicioValidacion:
    def __init__(self):
        try:
            self.db_connection = DatabaseConnection()  # Conexión a la base de datos
            self.cliente_dao = ClienteDAO(self.db_connection)
        except Exception as e:
            print(f"Error inicializando ServicioValidacion: {e}")

    def buscar_o_registrar_cliente(self, dni: str):
        """
        Busca al cliente por DNI y lo registra si no existe. Valida cada dato antes de continuar.
        :param dni: DNI del cliente.
        :return: Objeto Cliente.
        """
        try:
            # 1. Buscar cliente existente por DNI
            cliente = self.cliente_dao.buscar_por_dni(dni)
            if cliente:
                print(f"\n✔ Cliente encontrado: {cliente.nombre} {cliente.apellido}")
                return cliente

            # 2. Registrar un cliente nuevo si no existe
            print(f"❌ No se encontró un cliente con este DNI.\n")
            opcion = input("¿Desea registrarse como cliente? (s/n): ").strip().lower()

            if opcion != "s":
                print("Debe registrarse para continuar con la compra.")
                return None

            # Validar el nombre (primer campo)
            while True:
                nombre = input("Ingrese su nombre: ").strip()
                if self.es_nombre_valido(nombre):
                    break
                print("❌ El nombre solo debe contener letras y espacios. Intente nuevamente.")

            # Validar el apellido (segundo campo)
            while True:
                apellido = input("Ingrese su apellido: ").strip()
                if self.es_nombre_valido(apellido):
                    break
                print("❌ El apellido solo debe contener letras y espacios. Intente nuevamente.")

            # Validar el email (tercer campo)
            while True:
                email = input("Ingrese su correo electrónico: ").strip()
                if "@" in email and email.endswith(".com"):
                    break
                print("❌ Correo electrónico inválido. Intente nuevamente.")

            # Registrar al cliente en la base de datos
            self.cliente_dao.crear_cliente(Cliente(
                id_cliente=None,
                dni=dni,
                nombre=nombre,
                apellido=apellido,
                email=email
            ))
            if not self.es_nombre_valido(cliente.nombre):
                print(f"❌ Nombre inválido: {cliente.nombre}. No se registrará el cliente.")
                return None

            self.cliente_dao.crear_cliente(cliente)
            print(f"✔ Cliente registrado correctamente: {nombre} {apellido}")

            # Volver a buscar al cliente registrado para obtener su ID
            cliente = self.cliente_dao.buscar_por_dni(dni)
            if not cliente:
                raise Exception("❌ No se pudo confirmar el registro del cliente en la base de datos. Intente nuevamente.")

            return cliente
        except Exception as e:
            print(f"⚠ Error en buscar_o_registrar_cliente: {e}")
            return None
        
    @staticmethod
    def es_solo_digitos(cadena):
        return cadena.isdigit()

    @staticmethod
    def es_numero(cadena):
        return cadena.isdigit()
    
    @staticmethod
    def es_nombre_valido(cadena):
        if not cadena or not isinstance(cadena, str):
            return False
        cadena = unicodedata.normalize('NFKC', cadena)  # Normaliza caracteres especiales
        return cadena.replace(" ", "").isalpha()

