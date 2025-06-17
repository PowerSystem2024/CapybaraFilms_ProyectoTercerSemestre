from domain.entities.Cliente import Cliente
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

    def buscar_o_registrar_cliente(self, dni: str):
        """
        Este método busca un cliente en la base de datos por su DNI.
        Si no existe, lo registra validando correctamente sus datos.
        """
        try:
            # Paso 1: Buscar un cliente existente por su DNI.
            cliente = self.cliente_dao.buscar_por_dni(dni)  # Llamamos al DAO para buscar al cliente.
            if cliente:  # Si el cliente existe...
                print(f"\n✔ Cliente encontrado: {cliente.nombre} {cliente.apellido}")  # Mostramos los datos del cliente.
                return cliente  # Retornamos el cliente encontrado.

            # Paso 2: Si el cliente no existe, ofrecemos registrarlo.
            print(f"❌ No se encontró un cliente con este DNI.\n")
            opcion = input("¿Desea registrarse como cliente? (s/n): ").strip().lower()
            # Le pedimos al usuario que decida si quiere registrarse. Eliminamos espacios y convertimos el texto a minúsculas.

            if opcion != "s":  # Si la respuesta no es "s" (sí)...
                print("Debe registrarse para continuar con la compra.")  # Mostramos un mensaje de advertencia.
                return None  # Salimos de este paso sin hacer nada más.

            # Paso 3: Validar los datos del cliente para el registro.
            # Validamos el nombre ingresado por el usuario.
            while True:
                nombre = input("Ingrese su nombre: ").strip()  # Solicitamos el nombre al usuario.
                if self.es_nombre_valido(nombre):  # Verificamos que el nombre sea válido (solo letras y espacios).
                    break  # Salimos del bucle si el nombre es válido.
                print("❌ El nombre solo debe contener letras y espacios. Intente nuevamente.")  # Mostramos un error si no es válido.

            # Validamos el apellido ingresado por el usuario.
            while True:
                apellido = input("Ingrese su apellido: ").strip()  # Solicitamos el apellido al usuario.
                if self.es_nombre_valido(apellido):  # Verificamos que el apellido sea válido (solo letras y espacios).
                    break  # Salimos del bucle si el apellido es válido.
                print("❌ El apellido solo debe contener letras y espacios. Intente nuevamente.")  # Mostramos un error si no es válido.

            # Validamos el correo electrónico ingresado por el usuario.
            while True:
                email = input("Ingrese su correo electrónico: ").strip()  # Solicitamos el email al usuario.
                if "@" in email and email.endswith(".com"):  # Verificamos que el email contenga "@" y termine en ".com".
                    break  # Salimos del bucle si el correo es válido.
                print("❌ Correo electrónico inválido. Intente nuevamente.")  # Mostramos un error si no es válido.

            # Paso 4: Crear y registrar al cliente en la base de datos.
            cliente = Cliente(  # Creamos una nueva instancia del cliente con los datos ingresados.
                id_cliente=None,  # El ID se configura automáticamente en la base de datos.
                dni=dni,
                nombre=nombre,
                apellido=apellido,
                email=email
            )
            self.cliente_dao.crear_cliente(cliente)  # Registramos al cliente en la base de datos utilizando el DAO.

            # Paso 5: Confirmar que el cliente se registró correctamente.
            cliente = self.cliente_dao.buscar_por_dni(dni)  # Volvemos a buscar al cliente registrado por su DNI.
            if not cliente:  # Si no se encuentra al cliente recién creado...
                raise Exception("❌ No se pudo confirmar el registro del cliente en la base de datos. Intente nuevamente.")  # Lanzamos un error.

            print(f"✔ Cliente registrado correctamente: {nombre} {apellido}")  # Confirmamos el registro exitoso.
            return cliente  # Retornamos el cliente registrado.

        except Exception as e:
            # Mostramos un mensaje si ocurre un error inesperado en este proceso.
            print(f"⚠ Error en buscar_o_registrar_cliente: {e}")
            return None  # Retornamos None si algo falla.

    @staticmethod
    def es_solo_digitos(cadena):
        # Este método verifica si la cadena contiene solo dígitos (números).
        return cadena.isdigit()

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