from domain.services.ServicioCompraEntradas import ServicioCompraEntradas
from domain.services.ServicioValidacion import ServicioValidacion
from domain.entities.Pelicula import Pelicula
from domain.entities.Sala import Sala
from domain.entities.Reserva import Reserva

class ComprarEntradaTest:
    def __init__(self):
        try:
            self.servicio_compra = ServicioCompraEntradas()
            self.servicio_validacion = ServicioValidacion()
        except Exception as e:
            print(f"Error inicializando la aplicación: {e}")
            exit(1)

    def ejecutar(self):
        try:
            # Solicitar DNI e identificar o registrar al cliente
            while True:
                dni = input("Ingrese su DNI: ").strip()
                if len(dni) == 8 and dni.isdigit() and not dni.startswith("00"):
                    break
                print("DNI inválido. Intente nuevamente.")

            # Buscar al cliente en la base de datos o registrar si no existe
            cliente = self.servicio_validacion.buscar_o_registrar_cliente(dni)
            if not cliente:
                print("Ocurrió un error al procesar el cliente.")
                return

            print(f"\nBienvenido, {cliente.get_nombre()} {cliente.get_apellido()}.\n")

            # Continuar con el flujo de selección de películas, reserva, etc.
            peliculas = [
                Pelicula("Shrek", "Andrew Adamson", 90, "Comedia", "Español", "2D"),
                Pelicula("Avengers: Endgame", "Russo Brothers", 181, "Acción", "Español", "3D"),
                Pelicula("Jurassic Park", "Steven Spielberg", 127, "Ciencia Ficción", "Español", "2D"),
            ]

            print("Películas disponibles:")
            for index, pelicula in enumerate(peliculas, start=1):
                print(f"{index}. {pelicula.get_nombre()} ({pelicula.get_formato()})")

            pelicula_index = self.servicio_compra.seleccionar_pelicula(len(peliculas))
            pelicula_seleccionada = peliculas[pelicula_index]

            sala = Sala(pelicula_seleccionada)
            sala.mostrar_butacas()

            cantidad_entradas = self.servicio_compra.solicitar_cantidad_entradas()
            butacas_reservadas = self.servicio_compra.seleccionar_butacas(cantidad_entradas, sala)
            combo = self.servicio_compra.seleccionar_combo()

            reserva = Reserva(cliente, sala, combo, butacas_reservadas)
            reserva.mostrar_resumen()

            print("\nGracias por su compra. ¡Disfrute la función!")

        except Exception as e:
            print(f"Error durante la ejecución del programa: {e}")

if __name__ == "__main__":
    try:
        comprar_entrada_test = ComprarEntradaTest()
        comprar_entrada_test.ejecutar()
    except Exception as e:
        print(f"Error crítico en la aplicación: {e}")