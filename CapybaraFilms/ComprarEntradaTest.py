from domain.services.ServicioValidacion import ServicioValidacion
import psycopg2

class ComprarEntradaTest:
    def __init__(self):
        self.validacion = ServicioValidacion()

    def iniciar_compra(self):
        print("Iniciando proceso de compra...")

    def mostrar_peliculas(self):
        # Ejemplo: Películas disponibles (esto deberiamos agregar en la base de datos)
        self.peliculas = [
            {"id": 1, "titulo": "Star Wars", "formato": "IMAX"},
            {"id": 2, "titulo": "Avengers: Endgame", "formato": "3D"},
            {"id": 3, "titulo": "Jurassic Park", "formato": "2D"}
        ]
        print("Películas disponibles:")
        for pelicula in self.peliculas:
            print(f"[{pelicula['id']}] {pelicula['titulo']} - {pelicula['formato']}")

    def seleccionar_pelicula(self):
        while True:
            try:
                opc = int(input("Seleccione una película por su ID: "))
                pelicula = next((p for p in self.peliculas if p["id"] == opc), None)
                if pelicula:
                    print(f"Has seleccionado: {pelicula['titulo']}")
                    return pelicula
                else:
                    print("Por favor, seleccione un ID válido.")
            except ValueError:
                print("Entrada inválida. Intente otra vez.")

    def solicitar_cantidad_entradas(self):
        while True:
            try:
                cantidad = int(input("¿Cuántas entradas desea comprar?: "))
                if cantidad > 0:
                    return cantidad
                print("Debe ingresar una cantidad mayor a cero.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

    def seleccionar_combo(self):
        combos = [
            {"id": 1, "descripcion": "Combo 1: Nachos + Refresco ($5)", "precio": 5},
            {"id": 2, "descripcion": "Combo 2: Palomitas + Refresco ($4)", "precio": 4},
        ]
        print("Seleccione un combo:")
        for combo in combos:
            print(f"[{combo['id']}] {combo['descripcion']}")

        while True:
            try:
                opc = int(input("Seleccione un combo por su ID: "))
                combo_seleccionado = next((c for c in combos if c["id"] == opc), None)
                if combo_seleccionado:
                    print(f"Has seleccionado: {combo_seleccionado['descripcion']}")
                    return combo_seleccionado
                else:
                    print("Por favor, seleccione un ID válido.")
            except ValueError:
                print("Entrada inválida. Intente otra vez.")

    def realizar_reserva(self, cliente, pelicula, combo, cantidad_entradas):
        print(f"\nRealizando reserva para {cliente['nombre']} {cliente['apellido']}...")
        print(f"Película: {pelicula['titulo']} ({pelicula['formato']})")
        print(f"Entradas: {cantidad_entradas}")
        print(f"Combo seleccionado: {combo['descripcion']}")
        # Aquí deberiamos guardar la reserva en la base de datos

    def ejecutar(self):
        # Iniciar el flujo de compra
        self.iniciar_compra()

        # Validar datos del cliente
        cliente = self.validacion.obtener_datos_cliente()

        # Mostrar y seleccionar película
        self.mostrar_peliculas()
        pelicula = self.seleccionar_pelicula()

        # Solicitar cantidad de entradas
        cantidad_entradas = self.solicitar_cantidad_entradas()

        # Seleccionar combo
        combo = self.seleccionar_combo()

        # Realizar la reserva
        self.realizar_reserva(cliente, pelicula, combo, cantidad_entradas)

        # Mensaje de agradecimiento
        print(f"\n¡Gracias por su compra, {cliente['nombre']} {cliente['apellido']}! Disfrute la función.")


if __name__ == "__main__":
    test = ComprarEntradaTest()
    test.ejecutar()