from capybarafilms.domain.entities import Butaca, Candy, Catalogo, Cliente, Reserva, Sala
from capybarafilms.domain.entities.types import Ubicacion
from capybarafilms.domain.services.servicio_validacion import es_numero

class ServicioCompraEntradas:
    def __init__(self):
        self.entrada = input  # Usa input() para leer entradas del usuario

    def iniciar_compra(self):
        print("--------------------------------------------------------------------")
        print("*              Bienvenido/a a Capybara's Films!               *")
        print("--------------------------------------------------------------------")
        print("***    Disfruta de la mejor experiencia de cine.     ***")
        print()
        print("A continuación ingrese sus datos para adquirir las entradas a la función de cine.")

    def mostrar_peliculas(self):
        print("¿Qué película desea ver?")
        for index, pelicula in enumerate(Catalogo.get_peliculas(), start=1):
            print(f"{index}) {pelicula.nombre}")

    def seleccionar_pelicula(self):
        while True:
            print("Seleccione el número de la película:")
            entrada_usuario = self.entrada()
            if es_numero(entrada_usuario):
                opcion = int(entrada_usuario)
                if 1 <= opcion <= len(Catalogo.get_peliculas()):
                    return opcion - 1
                else:
                    print(f"Opción inválida. Elija un número entre 1 y {len(Catalogo.get_peliculas())}.")
            else:
                print("Entrada inválida. Por favor, ingrese un número.")

    def solicitar_cantidad_entradas(self):
        while True:
            print("¿Cuántas entradas desea comprar?")
            entrada_usuario = self.entrada()
            if es_numero(entrada_usuario):
                cantidad = int(entrada_usuario)
                if cantidad > 0:
                    return cantidad
                else:
                    print("La cantidad debe ser mayor que cero.")
            else:
                print("Entrada inválida. Por favor, ingrese un número.")

    def seleccionar_butacas(self, cantidad_entradas, sala):
        butacas_seleccionadas = []
        self.mostrar_matriz_butacas(sala)

        for i in range(cantidad_entradas):
            while True:
                try:
                    fila = int(input(f"Ingrese la fila (0 a 11) para la entrada {i+1}: "))
                    while fila < 0 or fila >= 12:
                        print("Número de fila no válido.")
                        fila = int(input("Ingrese nuevamente la fila (0 a 11): "))

                    butaca = int(input(f"Ingrese el número de butaca (0 a 11) para la entrada {i+1}: "))
                    while butaca < 0 or butaca >= 12:
                        print("Número de butaca no válido.")
                        butaca = int(input("Ingrese nuevamente el número de butaca (0 a 11): "))

                    ubicacion = Ubicacion(fila, butaca)
                    if sala.butaca_esta_ocupada(ubicacion):
                        print("La butaca está ocupada. Intente con otra.")
                    else:
                        butaca_seleccionada = sala.get_butaca(ubicacion)
                        butacas_seleccionadas.append(butaca_seleccionada)
                        sala.asignar_butaca(ubicacion)
                        break
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")
        return butacas_seleccionadas

    def mostrar_matriz_butacas(self, sala):
        filas = 12
        butacas_por_fila = 12

        print("   ", end="")
        for b in range(butacas_por_fila):
            print(f" {b} ", end="")
        print()

        for fila in range(filas):
            print(f"{fila} ", end="")
            for butaca in range(butacas_por_fila):
                b = sala.get_butaca(Ubicacion(fila, butaca))
                if b.estado:
                    print("[X] ", end="")
                else:
                    print("[ ] ", end="")
            print()

    def realizar_reserva(self, cliente, sala, candy, butacas):
        return Reserva(cliente, sala, candy, butacas)

    def seleccionar_combo(self):
        print("""
¿Desea comprar algún combo de nuestro candy?
1) Sí
2) No""")
        while True:
            entrada_usuario = self.entrada()
            if entrada_usuario.strip() and es_numero(entrada_usuario):
                opcion_combo = int(entrada_usuario)
                if opcion_combo == 1:
                    # Lógica para seleccionar el combo real debería ir aquí
                    return Candy.obtener_combo()  # Ejemplo, depende del sistema
                elif opcion_combo == 2:
                    return None
                else:
                    print("Opción inválida. Por favor, elija 1 o 2.")
            else:
                print("Entrada inválida. Por favor, ingrese un número.")