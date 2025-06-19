# Importamos los DAOs que interactúan con la base de datos
from daos.ClienteDAO import ClienteDAO
from daos.PeliculaDAO import PeliculaDAO
from daos.SalaDAO import SalaDAO
from daos.ButacaDAO import ButacaDAO
from daos.ReservaDAO import ReservaDAO
from daos.CandyDAO import CandyDAO
from services.cine_services import CineServices

# Conexión a la base de datos
from data.DatabaseConnection import DatabaseConnection

# Servicios con lógica de negocio del cine
from services.cine_services import CineServices

# Función principal del programa
def main():
    try:
        # Inicializar la conexión a la base de datos y los DAOs (acceso a datos)
        db_connection = DatabaseConnection()
        cliente_dao = ClienteDAO(db_connection)
        pelicula_dao = PeliculaDAO(db_connection)
        sala_dao = SalaDAO(db_connection)
        butaca_dao = ButacaDAO(db_connection)
        reserva_dao = ReservaDAO(db_connection)
        candy_dao = CandyDAO(db_connection)

        # Instanciamos los servicios del cine
        cine_services = CineServices()
        pelicula = None  # Inicializamos la variable película

        # Mostrar mensaje de bienvenida
        print("-----------------------------------------------------------------")
        print("*        🎥 🎞️  Bienvenido/a a Capybara's Films!  🍿🎬         *")
        print("-----------------------------------------------------------------\n")
        print("*       🍿📽️  Disfruta de la mejor experiencia de cine.  😄🌟   *")
        print("\nA continuación ingresa tus datos para adquirir las entradas 🎫 a la función de cine.\n")

        # Paso 1: Verificar o registrar cliente
        cliente = cine_services.verificar_y_validar_cliente(cliente_dao)
        if not cliente:
            print("❌ No se puede continuar sin un cliente registrado.")
            return  # Se corta la ejecución si no hay cliente válido
        cine_services.limpiar_pantalla()  # Limpia pantalla

        # Paso 2: Elegir película
        pelicula = cine_services.elegir_pelicula(pelicula_dao)
        if not pelicula:
            print("❌ No se seleccionó ninguna película.")
            return
        cine_services.limpiar_pantalla()

        # Paso 3: Seleccionar sala y cantidad de entradas
        sala, cantidad_entradas = cine_services.seleccionar_sala_y_entradas(sala_dao, butaca_dao, pelicula)
        if not sala or cantidad_entradas == 0:
            print("❌ No se seleccionó ninguna sala o entradas.")
            return
        cine_services.limpiar_pantalla()

        # Paso 4: Selección de butacas específicas
        butacas_seleccionadas = cine_services.seleccionar_butacas(butaca_dao, cantidad_entradas, sala)
        if not butacas_seleccionadas:
            print("❌ No se seleccionaron butacas válidas.")
            return
        ids_butacas_seleccionadas = [butaca.id_butaca for butaca in butacas_seleccionadas]
        cine_services.limpiar_pantalla()

        # Paso 5: Crear la reserva en la base de datos
        reserva = reserva_dao.crear_reserva(cliente.id_cliente, sala.id_sala, ids_butacas_seleccionadas)
        if not reserva:
            print("❌ No se pudo crear la reserva. Asegúrese de que los datos sean correctos.")
            return
        cine_services.limpiar_pantalla()

        # Paso 6: Elegir combos o golosinas (opcional)
        combos_seleccionados = cine_services.seleccionar_combos(candy_dao)
        if combos_seleccionados:
            print("\n=== 🥤  Combos Seleccionados 🍿 ===")
            for combo in combos_seleccionados:
                print(f"- {combo.get_nombre()} - Precio: {combo.get_precio()}")
        else:
            print("No se seleccionaron combos.")
        cine_services.limpiar_pantalla()

        # Asociar los combos seleccionados a la reserva (en el objeto reserva)
        reserva.candy = combos_seleccionados

        # Paso 7: Mostrar resumen de la reserva al usuario
        reserva.mostrar_resumen()

        # Mensaje final al usuario
        print(f"🌟🤗  ¡Compra exitosa! Gracias por visitar Capybara Films, {cliente.nombre}. 🎉")

    except Exception as e:
        # Captura de errores generales del programa
        print(f"⚠ Se produjo un error crítico en la aplicación: {e}")
    finally:
        # Siempre intenta cerrar la conexión a la base de datos, incluso si hubo error
        try:
            db_connection.cerrar_conexion()
        except Exception as e:
            print(f"⚠ Error cerrando la conexión a la base de datos: {e}")

# Verificamos que el script se está ejecutando directamente
if __name__ == "__main__":
    main()