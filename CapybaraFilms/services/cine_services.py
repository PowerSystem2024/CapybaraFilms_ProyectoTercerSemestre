import sys
import os
from domain.entities.Pelicula import Pelicula
from domain.entities.types.TipoCandy import TipoCandy
from daos.ClienteDAO import ClienteDAO
from daos.PeliculaDAO import PeliculaDAO
from daos.SalaDAO import SalaDAO
from daos.ButacaDAO import ButacaDAO
from domain.entities.Cliente import Cliente
from services.ServicioValidacion import ServicioValidacion
from domain.entities.Sala import Sala
from domain.entities.Butaca import Butaca
from domain.entities.types.Ubicacion import Ubicacion
from daos.CandyDAO import CandyDAO
from domain.entities.types.TipoButaca import TipoButaca

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

class CineServices:
    def __init__(self):
        self.entrada = input # Inicializamos el servicio con la función input, que permite al usuario ingresar datos desde la consola.
        
    def solicitar_cantidad_entradas(self):
        while True:

            print("¿Cuántas entradas desea comprar? 🎟️🎟️")

            entrada_usuario = self.entrada()  # Leemos la entrada del usuario.
            if ServicioValidacion.es_numero(entrada_usuario):  # Verificamos si la entrada es un número válido.
                cantidad = int(entrada_usuario)  # Convertimos la entrada en un número entero.
                if cantidad > 0:  # Validamos que la cantidad sea mayor que cero.
                    return cantidad  # Devolvemos la cantidad válida.
                else:
                    print("La cantidad debe ser mayor que cero.")  # Mostramos un mensaje si la cantidad no es válida.
            else:
                print("Entrada inválida. Por favor, ingrese un número.")  # Mostramos un error si la entrada no es numérica.

    def mostrar_matriz_butacas(self, sala: Sala, butaca_dao: ButacaDAO): # Este método muestra todas las butacas de una sala en formato de matriz.

        print(f"\n Buscando sala 🎭🎬...")
        butacas = butaca_dao.butacas_por_sala(sala.id_sala) # Obtenemos todas las butacas de la sala con el ID dado.
        print("\nSeleccione su butaca: 🪑🍿 ")


        for fila in range(1, 13): # Recorremos las filas de la matriz de butacas, de 1 a 12.
            print(f"{fila}\t", end="") # Mostramos el número de cada fila. /t es un tabulador.
            for columna in range(1, 13): # Recorremos las columnas, de 1 a 12.
                # Verificamos si la butaca está disponible. Si está disponible, mostramos un espacio " ", si no, mostramos "X".
                estado = " " if self.butaca_esta_disponible(butacas, fila, columna) else "X"
                print(f"[{estado}]", end=" ") # Mostramos la butaca en forma visual. end=" " separa los elementos en la misma línea.
            print(f"\n") # Cambiamos de fila.
        print("") # Salto de línea para separar la matriz de butacas de la información del cliente.

    def seleccionar_combos(self, candy_dao: CandyDAO):
        # Mostramos el menú de combos y permitimos al usuario seleccionar cuántos combos desea agregar.
        combos_seleccionados = []  # Creamos una lista vacía para los combos seleccionados.

        print("\n=== ❤️  Menú de Combos  🍿🥤 ===")

        print("¿Deseas comprar un combo de pochoclos y bebidas? \n")
        while True:  # Permitimos que el usuario elija múltiples combos.
            print("0. No agregar combo")  # Opción de no agregar más combos.
            for idx, tipo in enumerate(TipoCandy, start=1):  # Enumeramos los combos disponibles.
                print(f"{idx}. {tipo.get_nombre()} - Precio: {tipo.get_precio()}")  # Mostramos el nombre y el precio del combo.

            try:
                opcion = int(input("\n🍿 Seleccione el combo que desea agregar (por número): "))  # Leemos la opción ingresada por el usuario.

                if opcion == 0:
                    break  # Si el usuario elige 0, terminamos este proceso.
                elif 1 <= opcion <= len(TipoCandy):  # Verificamos si la opción está dentro del rango válido.
                    combo_seleccionado = list(TipoCandy)[opcion - 1]  # Obtenemos el combo seleccionado.
                    combos_seleccionados.append(combo_seleccionado)  # Agregamos el combo a la lista.

                    print(f"😄 Combo '{combo_seleccionado.get_nombre()}' agregado.")
                    print("\n 🍿  Deseas agregar otro combo?\n")

                else:
                    print("❌ Opción inválida. Inténtelo nuevamente.")  # Si la opción no es válida, mostramos un error.
            except ValueError:
                print("❌ Entrada inválida. Por favor ingrese un número válido.")  # Si el usuario ingresa algo que no es un número, mostramos un error.
        return combos_seleccionados  # Retornamos la lista de combos seleccionados.

    def elegir_pelicula(self, pelicula_dao: PeliculaDAO): # Este método muestra al usuario todas las películas disponibles y le permite elegir una.
        try:
            print("\n=== Selecciona una Película 🎥 ===")

            peliculas = pelicula_dao.obtener_todas() # Obtenemos todas las películas disponibles de la base de datos.
            for idx, pelicula in enumerate(peliculas, start=1): # Enumeramos las películas desde 1 para facilitar la elección.
                print(f"{idx}. {pelicula.nombre} - {pelicula.director} ({pelicula.duracion} min) - Formato: {pelicula.formato}")
                # Mostramos el índice, el nombre de la película, el director, la duración y el formato.

            while True: # Repetimos hasta que el usuario seleccione una película válida.
                try:

                    opcion = int(input(f" 🎥 Seleccione una película (1-{len(peliculas)}): ")) # Pedimos al usuario que seleccione la película por su número.

                    if 1 <= opcion <= len(peliculas): # Verificamos que la opción esté dentro del rango mostrado.
                        return peliculas[opcion - 1] # Retornamos la película seleccionada (se ajusta el índice a base 0).
                    else:
                        print("❌ Por favor, elija una opción válida.") # Mostramos un error si la opción está fuera del rango.
                except ValueError:
                    print("❌ Entrada inválida. Por favor ingrese un número.") # Mostramos un error si el usuario no ingresa un número.
        except Exception as e:
            print(f"⚠ Error al seleccionar película: {e}") # Capturamos cualquier error inesperado.

    def seleccionar_sala_y_entradas(self, sala_dao: SalaDAO, butaca_dao: ButacaDAO, pelicula: Pelicula):
        # Este método permite seleccionar una sala para la película y la cantidad de entradas que desea comprar.
        try:
            print(f"\n=== 🎫🎬  Salas para la Película: {pelicula.nombre} ===\n")

            salas = sala_dao.buscar_por_pelicula(pelicula.id_pelicula) # Obtenemos todas las salas que proyectan la película.

            if not salas: # Si no hay salas asociadas a la película...
                print("❌ No hay salas disponibles para la película seleccionada.")
                return None, 0 # Retornamos un valor nulo.


            cantidad_butacas_disponibles = butaca_dao.cantidad_butacas_disponibles(salas[0].id_sala) # Consultamos cuántas butacas disponibles hay en la sala.
            cantidad_entradas = int(input("🎫✨ ¿Cuántas entradas desea comprar? ")) # Preguntamos cuántas entradas desea comprar.
            
            if cantidad_entradas <= 0 or cantidad_entradas > cantidad_butacas_disponibles: # Validamos que haya suficientes butacas disponibles.
                print(f"❌ No hay suficientes entradas disponibles.")
                return None, 0 # Retornamos valores nulos si no hay disponibilidad.

            return salas[0], cantidad_entradas # Retornamos la sala seleccionada y la cantidad de entradas.
        except IndexError:
            print("❌ Ocurrió un error al buscar las salas.") # Mostramos un error si no encontramos salas.
            return None, 0
        except Exception as e:
            print(f"⚠ Error inesperado: {e}") # Capturamos cualquier otro error inesperado.

    def _solicitar_ubicacion(self, numero_seleccion: int) -> Ubicacion:
        # Este método permite al usuario seleccionar la fila y columna de la butaca que desea ocupar.

        print(f"\n📍✨ Seleccione la ubicación de la butaca número {numero_seleccion + 1}:")
        while True:  # Repetimos hasta que el usuario elija una ubicación válida.
            try:
                fila = int(input("🤗  Primero elegi la fila (1-12): "))  # Pedimos la fila de la butaca.
                columna = int(input("🫶  Ahora elegi la columna (1-12): "))  # Pedimos la columna de la butaca.

                if 1 <= fila <= 12 and 1 <= columna <= 12:  # Validamos que la fila y la columna estén dentro del rango permitido.
                    return Ubicacion(fila=fila, columna=columna, butaca=None)  # Creamos y retornamos una instancia de Ubicacion.
                else:
                    print("⚠️ Fila y columna deben estar entre 1 y 12. Intente nuevamente.")  # Mostramos un error si la ubicación no es válida.
            except ValueError:
                print("⚠️ Entrada inválida. Por favor ingrese números para fila y columna.")  # Mostramos un error si el usuario ingresa caracteres no numéricos.
    
    def butaca_esta_disponible(self, butacas: list[Butaca], fila: int, columna: int) -> bool:
        # Este método verifica si una butaca específica está disponible (sin ocupar).
        for butaca in butacas:  # Recorremos cada butaca en la lista de butacas.
            if butaca.get_fila() == fila and butaca.get_columna() == columna:  # Comparamos la fila y la columna.
                return butaca.is_estado()  # Retorna True si la butaca está disponible.
        return False  # Retornamos False si no está disponible o no encontramos la butaca.

    def get_butaca(self, butacas: list, ubicacion: Ubicacion) -> Butaca:
        # Este método busca y retorna una butaca específica según su ubicación (fila y columna).
        for butaca in butacas:  # Recorremos todas las butacas disponibles.
            if butaca.fila == ubicacion.get_fila() and butaca.columna == ubicacion.get_columna():
                return butaca  # Retornamos el objeto Butaca si coincide con la ubicación.
        return None  # Retornamos None si la butaca no existe.

    def seleccionar_butacas(self, butaca_dao: ButacaDAO, cantidad_entradas: int, sala: Sala):
        # Este método permite al usuario seleccionar varias butacas en una sala específica.
        butacas_seleccionadas = []  # Creamos una lista para almacenar las butacas seleccionadas.

        # Obtenemos todas las butacas disponibles y mostramos la disposición en la sala.
        butacas = butaca_dao.butacas_por_sala(sala.id_sala)
        self.mostrar_matriz_butacas(sala, butaca_dao)

        for i in range(cantidad_entradas):  # Repetimos este proceso tantas veces como entradas se compraron.
            while True:
                ubicacion = self._solicitar_ubicacion(i)  # Pedimos al usuario que seleccione una ubicación.

                butaca_seleccionada = self.get_butaca(butacas, ubicacion)  # Buscamos la butaca seleccionada.
                if butaca_seleccionada is None:  # Si la butaca no existe, mostramos un mensaje de error.
                    print("⚠️ No existe una butaca en esa ubicación. Intente nuevamente.")
                    continue
                if not butaca_seleccionada.is_estado():  # Si la butaca ya está ocupada, mostramos un mensaje de error.
                    print("⚠️ La butaca ya está ocupada. Intente con otra.")
                    continue

                # Cambiamos el estado de la butaca a ocupada y actualizamos su estado en la base de datos.
                butaca_seleccionada.set_estado(False)
                butaca_dao.actualizar_estado(butaca_seleccionada.id_butaca, False)

                # Agregamos la butaca seleccionada a la lista.
                butacas_seleccionadas.append(butaca_seleccionada)
                break
        return butacas_seleccionadas  # Retornamos la lista de butacas seleccionadas.
    
    def obtener_precio_por_categoria(categoria):
        # Este método obtiene el precio de una butaca según su categoría (tipo).
        try:
            # Buscamos en el diccionario `TipoButaca` la categoría en mayúsculas y obtenemos su precio.
            return TipoButaca[categoria.upper()].get_precio()
        except KeyError:
            # Si la categoría no existe en `TipoButaca`, mostramos un error al usuario.
            print(f"Categoría '{categoria}' no encontrada en TipoButaca")
            return 0  # Retornamos 0 si no se encontró la categoría para manejar el error de manera más segura.

    def verificar_y_validar_cliente(self, cliente_dao: ClienteDAO):
        # Este método verifica si un cliente existe por DNI y, si no existe, permite registrarlo y validarlo.
        from services.ServicioValidacion import ServicioValidacion  # Importamos el servicio de validación.

        try:
            while True:  # Repetimos este proceso hasta obtener un cliente válido.
                dni = input(" 🪪  Ingresa tu DNI para verificar la existencia en el sistema: ").strip()

                # Eliminamos los espacios en blanco al inicio y al final del DNI ingresado.
                if not dni.isdigit() or len(dni) != 8:  # Validamos que el DNI solo contenga números y tenga exactamente 8 dígitos.
                    print("❌ El DNI debe contener exactamente 8 caracteres numéricos. Inténtelo nuevamente.")
                    continue  # Continuamos el bucle si el DNI no es válido.

                cliente = cliente_dao.buscar_por_dni(dni)  # Buscamos al cliente en la base de datos usando el DNI.
                if cliente:  # Si encontramos al cliente, mostramos un mensaje de bienvenida y lo retornamos.

                    print(f" 😍🌟  ¡Bienvenido nuevamente {cliente.nombre} {cliente.apellido} ({cliente.email})!🎉🫶🏻")
                    return cliente
                else:  # Si no encontramos al cliente, pedimos datos para registrarlo.
                    print(" 😞💔  No se encontró un cliente con este DNI.")
                    opcion = input("\n ✨🏅  ¿Deseas registrarte como cliente? (s/n): ").strip().lower()

                    # Eliminamos espacios en blanco y convertimos la respuesta a minúsculas para evitar inconsistencias.
                    if opcion == "s":  # Si el usuario desea registrarse...
                        # Validamos el nombre ingresado, verificando que contenga solo letras y/o espacios.
                        while True:
                            nombre = input("\n 🆔  Por favor, ingresa tu nombre: ").strip()  # Pedimos el nombre del cliente.

                            if not ServicioValidacion.es_nombre_valido(nombre):  # Usamos el servicio de validación para verificar el nombre.
                                print("❌ Nombre inválido: Debe contener solo letras y espacios. Inténtelo nuevamente.")
                                continue  # Volvemos a pedir el nombre si no es válido.
                            break  # Salimos del bucle si el nombre es válido.

            # Validamos el apellido ingresado siguiendo el mismo procedimiento que para el nombre.
                while True:

                    apellido = input("\n ✍️  Ahora ingresá tu apellido: ").strip()  # Pedimos el apellido del cliente.

                    if not ServicioValidacion.es_nombre_valido(apellido):  # Validamos el apellido.
                        print("❌ Apellido inválido: Debe contener solo letras y espacios. Inténtelo nuevamente.")
                        continue  # Volvemos a pedir el apellido si no es válido.
                    break  # Salimos del bucle si el apellido es válido.

                # Validamos el correo electrónico ingresado, verificando que tenga un formato básico válido.
                while True:

                    email = input("\n 📬  Y ahora ingresá tu correo electrónico: ").strip()  # Pedimos el correo electrónico.

                    if "@" not in email or "." not in email:  # Aseguramos que el correo contenga '@' y un dominio.
                        print("❌ Correo inválido: Debe contener '@' y un dominio. Inténtelo nuevamente.")
                        continue  # Volvemos a pedir el correo si no es válido.
                    break  # Salimos del bucle si el correo es válido.

                # Creamos un nuevo cliente con los datos ingresados.
                cliente = Cliente(None, dni, nombre, apellido, email)
                cliente_dao.crear_cliente(cliente)  # Registramos al cliente en la base de datos.

                # Verificamos que el cliente se haya registrado correctamente.
                cliente_creado = cliente_dao.buscar_por_dni(dni)  # Buscamos nuevamente al cliente por su DNI.
                if cliente_creado:  # Si el cliente fue creado correctamente, damos la bienvenida.
                    print(f" 😄🎉  Cliente registrado correctamente. ¡Bienvenido {cliente_creado.nombre} {cliente_creado.apellido}!")
                    return cliente_creado  # Retornamos el cliente registrado.
                
                elif opcion == "n":  # Si el usuario no desea registrarse, mostramos un mensaje y retornamos None.
                    print(" 💔 Debe registrarse para continuar con la compra.")
                    return None
                
                else:  # Si la opción ingresada no es válida, mostramos un error.
                    print("❌ Opción inválida. Intente nuevamente.")

        except ValueError as ve:  # Capturamos errores de valores incorrectos.
            print(f"⚠ Error con los valores ingresados: {ve}")
        except Exception as e:  # Capturamos cualquier otro error crítico.
            print(f"⚠ Error crítico durante la verificación de cliente: {e}")

    def limpiar_pantalla(self):
        # Este método limpia la consola para que la experiencia del usuario sea más ordenada y agradable.
        import os  # Importamos el módulo `os` que nos permite acceder a comandos del sistema operativo.
        os.system('cls' if os.name == 'nt' else 'clear')
        # Usamos el comando `cls` si estamos en Windows (`nt`) o `clear` si estamos en Linux/Mac.