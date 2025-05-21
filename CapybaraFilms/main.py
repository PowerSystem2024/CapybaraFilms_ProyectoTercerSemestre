from domain.services.ServicioCompraEntradas import ServicioCompraEntradas
from domain.services.ServicioValidacion import ServicioValidacion
from domain.entities.Pelicula import Pelicula
from domain.entities.Sala import Sala
from domain.entities.types.Ubicacion import Ubicacion
from domain.entities.Butaca import Butaca
from domain.entities.Reserva import Reserva

class ComprarEntradaTest:
    def __init__(self):
        self.servicio_compra = ServicioCompraEntradas()
        self.servicio_validacion = ServicioValidacion()

    def ejecutar(self):
        # Iniciar proceso de compra
        print("--------------------------------------------------------------------")
        print("Bienvenido/a al sistema de compra de entradas de Capybara Films.")
        print("--------------------------------------------------------------------\n")

        # Crear instancia del cliente usando ServicioValidacion
        cliente = self.servicio_validacion.obtener_datos_cliente()
        print(f"Hola, {cliente.get_nombre()} {cliente.get_apellido()}.\n")

        # Mostrar las opciones de películas disponibles
        print("Películas disponibles:")
        peliculas = [
            Pelicula("Shrek", "Andrew Adamson", 90, "Comedia", "Español", "2D"),
            Pelicula("Avengers: Endgame", "Russo Brothers", 181, "Acción", "Español", "3D"),
            Pelicula("Jurassic Park", "Steven Spielberg", 127, "Ciencia Ficción", "Español", "2D"),
        ]

        for index, pelicula in enumerate(peliculas, start=1):
            print(f"{index}. {pelicula.get_nombre()} ({pelicula.get_formato()})")

        # Seleccionar película
        pelicula_index = self.servicio_compra.seleccionar_pelicula(len(peliculas))
        pelicula_seleccionada = peliculas[pelicula_index]

        # Crear sala con la película seleccionada
        sala = Sala(pelicula_seleccionada)

        # Mostrar matriz inicial de butacas
        print("\nDistribución inicial de las butacas:")
        sala.mostrar_butacas()

        # Solicitar cantidad de entradas a comprar
        cantidad_entradas = self.servicio_compra.solicitar_cantidad_entradas()

        # Seleccionar las butacas
        print("\nPor favor seleccione las butacas:")
        butacas_reservadas = self.servicio_compra.seleccionar_butacas(cantidad_entradas, sala)

        # Solicitar combo (opcional)
        combo = self.servicio_compra.seleccionar_combo()

        # Crear la reserva y mostrar resumen
        reserva = Reserva(
            cliente=cliente,  # Cliente ya es un objeto de la clase Cliente
            sala=sala,
            candy=combo,
            butacas_asignadas=butacas_reservadas,
        )
        print("\nResumen de la reserva:")
        reserva.mostrar_resumen()

        print("\nGracias por su compra. ¡Disfrute la función!")

if __name__ == "__main__":
    comprar_entrada_test = ComprarEntradaTest()
    comprar_entrada_test.ejecutar()