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
        self.entrada = input  # Usa input() para leer entradas del usuario
        
    def solicitar_cantidad_entradas(self):
        while True:
            print("¿Cuántas entradas desea comprar?")
            entrada_usuario = self.entrada()
            if ServicioValidacion.es_numero(entrada_usuario):
                cantidad = int(entrada_usuario)
                if cantidad > 0:
                    return cantidad
                else:
                    print("La cantidad debe ser mayor que cero.")
            else:
                print("Entrada inválida. Por favor, ingrese un número.")

    def mostrar_matriz_butacas(self, sala: Sala, butaca_dao: ButacaDAO):
        print(f"\nBuscando sala...")
        butacas = butaca_dao.butacas_por_sala(sala.id_sala)
        print("\nSeleccione su butaca: ")
        for fila in range(1,13):
            print(f"{fila}\t", end="")
            for columna in range(1, 13):
                estado = " " if self.butaca_esta_disponible(butacas,fila,columna) else "X"
                print(f"[{estado}]", end=" ")
            print(f"\n")
        print("")

    def seleccionar_combos(self, candy_dao: CandyDAO):
        """
        Permite al usuario seleccionar uno o más combos del menú.
        :return: Lista de combos seleccionados.
        """
        combos_seleccionados = []
        print("\n=== Menú de Combos ===")
        print("¿Deseas comprar un combo de pochoclos y bebidas? \n")
        while True:  # El usuario puede elegir múltiples combos o finalizar la selección
            print("0. No agregar combo")
            for idx, tipo in enumerate(TipoCandy, start=1):
                print(f"{idx}. {tipo.get_nombre()} - Precio: {tipo.get_precio()}")

            try:
                opcion = int(input("\nSeleccione el combo que desea agregar (por número): "))
                if opcion == 0:  # Finalizar selección
                    break  # Salimos del bucle interactivo
                elif 1 <= opcion <= len(TipoCandy):  # Selección válida del usuario
                    combo_seleccionado = list(TipoCandy)[opcion - 1]  # Obtener el combo por índice
                    combos_seleccionados.append(combo_seleccionado)  # Agregar a la lista
                    print(f"Combo '{combo_seleccionado.get_nombre()}' agregado.")
                    print("\nDesea agregar otro combo?")
                else:
                    print("❌ Opción inválida. Inténtelo nuevamente.")
            except ValueError:
                print("❌ Entrada inválida. Por favor ingrese un número válido.")

        return combos_seleccionados

    def verificar_cliente(self, cliente_dao: ClienteDAO):
        try:
            while True:
                dni = input("Ingrese su DNI para verificar su existencia en el sistema: ").strip()
                if not dni.isdigit() or len(dni) != 8:
                    print("❌ El DNI debe contener exactamente 8 caracteres numéricos. Inténtelo nuevamente.")
                    continue

                cliente = cliente_dao.buscar_por_dni(dni)
                if cliente:
                    print(f"✔ ¡Bienvenido nuevamente {cliente.nombre} {cliente.apellido} ({cliente.email})!")
                    return cliente
                else:
                    print("❌ No se encontró un cliente con este DNI.")
                    opcion = input("¿Desea registrarse como cliente? (s/n): ").strip().lower()
                    if opcion == "s":
                        nombre = input("Ingrese su nombre: ").strip()
                        apellido = input("Ingrese su apellido: ").strip()
                        email = input("Ingrese su correo electrónico: ").strip()

                        cliente = Cliente(None, dni, nombre, apellido, email)
                        cliente_dao.crear_cliente(cliente)
                        print(f"✔ Cliente {nombre} {apellido} registrado correctamente.")
                        return cliente
                    elif opcion == "n":
                        print("Debe registrarse para continuar con la compra.")
                    else:
                        print("❌ Opción inválida. Intente nuevamente.")
        except ValueError as ve:
            print(f"⚠ Error con los valores ingresados: {ve}")
        except Exception as e:
            print(f"⚠ Error crítico durante la verificación de cliente: {e}")

    def elegir_pelicula(self, pelicula_dao: PeliculaDAO):
        """
        Permite al usuario seleccionar una película disponible.
        Maneja excepciones relacionadas con entradas inválidas.
        """
        try:
            print("\n=== Selecciona una Película ===")
            peliculas = pelicula_dao.obtener_todas()
            for idx, pelicula in enumerate(peliculas, start=1):
                print(f"{idx}. {pelicula.nombre} - {pelicula.director} ({pelicula.duracion} min) - Formato: {pelicula.formato}")

            while True:
                try:
                    opcion = int(input(f"Seleccione una película (1-{len(peliculas)}): "))
                    if 1 <= opcion <= len(peliculas):
                        return peliculas[opcion - 1]
                    else:
                        print("❌ Por favor, elija una opción válida.")
                except ValueError:
                    print("❌ Entrada inválida. Por favor ingrese un número.")
        except Exception as e:
            print(f"⚠ Error al seleccionar película: {e}")

    def seleccionar_sala_y_entradas(self, sala_dao: SalaDAO,butaca_dao :ButacaDAO, pelicula: Pelicula):
        """
        Permite al usuario seleccionar una sala y la cantidad de entradas.
        Maneja excepciones relacionadas con entradas inválidas y la base de datos.
        """
        try:
            print(f"\n=== Salas para la Película: {pelicula.nombre} ===\n")
            salas = sala_dao.buscar_por_pelicula(pelicula.id_pelicula)

            cantidad_butacas_disponibles = butaca_dao.cantidad_butacas_disponibles(salas[0].id_sala)
            cantidad_entradas = int(input("¿Cuántas entradas desea comprar? "))
            if cantidad_entradas <= 0 or cantidad_entradas > cantidad_butacas_disponibles:
                print(f"❌ No hay suficientes entradas disponibles.")
                return None, 0
        except IndexError:
            print("❌ No hay salas disponibles para la película seleccionada.")
            return None, 0
        return salas[0], cantidad_entradas
    
    def _solicitar_ubicacion(self, numero_seleccion: int) -> Ubicacion:
        """
        Solicita al usuario la ubicación de una butaca (fila y columna).
        :param numero_seleccion: Número de la butaca que el usuario está seleccionando en esta iteración.
        :return: Instancia del objeto Ubicacion con los datos proporcionados.
        """
        print(f"\nSeleccione la ubicación de la butaca número {numero_seleccion + 1}:")
        while True:
            try:
                fila = int(input("Ingrese la fila (1-12): "))
                columna = int(input("Ingrese la columna (1-12): "))
                
                if 1 <= fila <= 12 and 1 <= columna <= 12:
                    return Ubicacion(fila=fila, columna=columna, butaca=None)  # Retorna instancia de Ubicacion
                else:
                    print("⚠️ Fila y columna deben estar entre 1 y 12. Intente nuevamente.")
            except ValueError:
                print("⚠️ Entrada inválida. Por favor ingrese números para fila y columna.")
    
    def set_butacas(self, sala: Sala, butacas: list):
            """
            Asigna una lista de Butacas a la sala (a nivel de lógica, no afecta la base de datos).
            """
            sala.butacas = butacas  # Extiende dinámicamente la sala con las butacas

    def butaca_esta_disponible(self, butacas: list[Butaca], fila: int, columna: int) -> bool:
        """
        Verifica si una butaca está disponible en función de su fila y columna.
        """
        for butaca in butacas:
            if butaca.get_fila() == fila and butaca.get_columna() == columna:
                return butaca.is_estado()  # Verdadero si está disponible
        return False  # La butaca no está en la lista o está ocupada

    def get_butaca(self, butacas: list, ubicacion: Ubicacion) -> Butaca:
        """
        Obtiene una butaca específica desde la lista de butacas según su ubicación.
        :param butacas: Lista de butacas.
        :param ubicacion: Ubicación con fila y columna.
        :return: Objeto Butaca o None si no existe.
        """
        for butaca in butacas:
            if butaca.fila == ubicacion.get_fila() and butaca.columna == ubicacion.get_columna():
                return butaca
        return None
    
    def seleccionar_butacas(self, butaca_dao: ButacaDAO, cantidad_entradas: int, sala: Sala):
        """
        Permite al usuario seleccionar múltiples butacas en una sala.
        Verifica ocupación, asigna butacas y actualiza la base de datos.
        """
        butacas_seleccionadas = []

        # Obtener y mostrar las butacas disponibles en la sala
        butacas = butaca_dao.butacas_por_sala(sala.id_sala)
        self.mostrar_matriz_butacas(sala, butaca_dao)

        # Proceso de selección de butacas
        for i in range(cantidad_entradas):
            while True:
                # Solicitar ubicación al usuario
                ubicacion = self._solicitar_ubicacion(i)

                # Verificar si la butaca está ocupada
                butaca_seleccionada = self.get_butaca(butacas, ubicacion)
                if butaca_seleccionada is None:
                    print("⚠️ No existe una butaca en esa ubicación. Intente nuevamente.")
                    continue
                if not butaca_seleccionada.is_estado():
                    print("⚠️ La butaca ya está ocupada. Intente con otra.")
                    continue

                # Cambiar el estado de la butaca (marcar como ocupada) y actualizar en la base de datos
                butaca_seleccionada.set_estado(False)
                butaca_dao.actualizar_estado(butaca_seleccionada.id_butaca, False)

                # Agregarla a la lista de seleccionadas
                butacas_seleccionadas.append(butaca_seleccionada)
                break
        return butacas_seleccionadas
    
    def obtener_precio_por_categoria(categoria):
        try:
            return TipoButaca[categoria.upper()].get_precio()
        except KeyError:
            print(f"Categoría '{categoria}' no encontrada en TipoButaca")
            return 0
        
    def verificar_y_validar_cliente(self, cliente_dao: ClienteDAO):
        """
        Verifica si un cliente existe por su DNI y lo registra si no existe.
        Además, valida que se haya creado correctamente antes de retornar.
        
        :param cliente_dao: DAO para gestionar operaciones sobre la entidad Cliente.
        :return: Objeto Cliente validado y listo para usar, o None si no se puede continuar.
        """
        from services.ServicioValidacion import ServicioValidacion

        try:
            while True:
                dni = input("Ingrese su DNI para verificar su existencia en el sistema: ").strip()
                if not dni.isdigit() or len(dni) != 8:
                    print("❌ El DNI debe contener exactamente 8 caracteres numéricos. Inténtelo nuevamente.")
                    continue

                # Intentar buscar al cliente por DNI
                cliente = cliente_dao.buscar_por_dni(dni)
                if cliente:
                    print(f"✔ ¡Bienvenido nuevamente {cliente.nombre} {cliente.apellido} ({cliente.email})!")
                    return cliente
                else:
                    print("❌ No se encontró un cliente con este DNI.")
                    opcion = input("\n¿Desea registrarse como cliente? (s/n): ").strip().lower()

                    if opcion == "s":
                        # Validar nombre y apellido inmediatamente después del input
                        while True:
                            nombre = input("\nIngrese su nombre: ").strip()
                            if not ServicioValidacion.es_nombre_valido(nombre):
                                print("❌ Nombre inválido: Debe contener solo letras y espacios. Inténtelo nuevamente.")
                                continue
                            break  # Sale del bucle cuando el nombre es válido

                        while True:
                            apellido = input("\nIngrese su apellido: ").strip()
                            if not ServicioValidacion.es_nombre_valido(apellido):
                                print("❌ Apellido inválido: Debe contener solo letras y espacios. Inténtelo nuevamente.")
                                continue
                            break  # Sale del bucle cuando el apellido es válido

                        # Validar el correo (opcional)
                        while True:
                            email = input("\nIngrese su correo electrónico: ").strip()
                            if "@" not in email or "." not in email:  # Validación básica
                                print("❌ Correo inválido: Debe contener '@' y un dominio. Inténtelo nuevamente.")
                                continue
                            break  # Sale del bucle cuando el correo es válido

                        cliente = Cliente(None, dni, nombre, apellido, email)
                        cliente_dao.crear_cliente(cliente)

                        # Validar que el cliente fue registrado correctamente
                        cliente_creado = cliente_dao.buscar_por_dni(dni)
                        if cliente_creado:
                            print(f"✔ Cliente registrado correctamente. ¡Bienvenido {cliente_creado.nombre} {cliente_creado.apellido}!")
                            return cliente_creado  # Devuelve el objeto Cliente creado
                        else:
                            print("❌ No se pudo confirmar el registro del cliente. Intente nuevamente.")
                    elif opcion == "n":
                        print("Debe registrarse para continuar con la compra.")
                        return None
                    else:
                        print("❌ Opción inválida. Intente nuevamente.")
        except ValueError as ve:
            print(f"⚠ Error con los valores ingresados: {ve}")
        except Exception as e:
            print(f"⚠ Error crítico durante la verificación de cliente: {e}")
            
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')