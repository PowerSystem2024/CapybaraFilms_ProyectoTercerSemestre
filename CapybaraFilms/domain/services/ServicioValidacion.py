class ServicioValidacion:

    def obtener_datos_cliente(self):
        # Solicitar y validar el nombre
        while True:
            nombre = input("Por favor, ingrese su nombre: ").strip() # .strip() elimina espacios en blanco
            # Validar que el nombre no esté vacío y que contenga solo letras.
            if nombre:
                break
            print("El nombre no puede estar vacío. Intente de nuevo.")

        # Solicitar y validar el apellido
        while True:
            apellido = input("Ahora ingrese su apellido: ").strip()
            if apellido:
                break
            print("El apellido no puede estar vacío. Intente de nuevo.")

        # Validar el DNI
        dni = self.obtener_dni_valido()

        # Validar el correo electrónico
        while True:
            correo = input("Ingrese su mail (debe contener '@' y terminar con '.com'): ").strip()
            if "@" in correo and correo.endswith(".com"):
                break
            print("Correo electrónico inválido. Intente nuevamente.")

        # Regresar un diccionario con los datos del cliente
        return {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "correo": correo
        }

    def obtener_dni_valido(self):
        while True:
            dni = input("Ahora ingrese su DNI (8 dígitos): ").strip()
            if len(dni) == 8 and dni.isdigit() and not dni.startswith("00"):
                return dni
            print("DNI inválido. Intente nuevamente.")

    @staticmethod
    def es_solo_digitos(cadena):
        return cadena.isdigit()

    @staticmethod
    def es_numero(cadena):
        return cadena.isdigit()