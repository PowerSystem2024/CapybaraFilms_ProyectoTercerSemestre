from daos.ClienteDAO import ClienteDAO
from daos.PeliculaDAO import PeliculaDAO
from daos.SalaDAO import SalaDAO
from daos.ButacaDAO import ButacaDAO
from daos.ReservaDAO import ReservaDAO
from data.DatabaseConnection import DatabaseConnection
from services.cine_services import CineServices
from daos.CandyDAO import CandyDAO

def main():
    try:
        # Inicializar conexión a la base de datos y DAOs
        db_connection = DatabaseConnection()
        cliente_dao = ClienteDAO(db_connection)
        pelicula_dao = PeliculaDAO(db_connection)
        sala_dao = SalaDAO(db_connection)
        butaca_dao = ButacaDAO(db_connection)
        reserva_dao = ReservaDAO(db_connection)
        candy_dao = CandyDAO(db_connection)
        cine_services = CineServices()
        pelicula = None

        # Mensaje de bienvenida
        print("-----------------------------------------------------------------")
        print("*              Bienvenido/a a Capybara's Films!               *")
        print("-----------------------------------------------------------------\n")
        print("*           Disfruta de la mejor experiencia de cine.          *")
        print("\nA continuación ingresa tus datos para adquirir las entradas a la función de cine.\n")

        # Paso 1: Verificar cliente (con creación y validación)
        cliente = cine_services.verificar_y_validar_cliente(cliente_dao)
        if not cliente:
            print("❌ No se puede continuar sin un cliente registrado.")
            return
        cine_services.limpiar_pantalla()

        # Paso 2: Seleccionar película
        pelicula = cine_services.elegir_pelicula(pelicula_dao)
        if not pelicula:
            print("❌ No se seleccionó ninguna película.")
            return
        cine_services.limpiar_pantalla()

        # Paso 3: Seleccionar sala y entradas
        sala, cantidad_entradas = cine_services.seleccionar_sala_y_entradas(sala_dao, butaca_dao, pelicula)
        if not sala or cantidad_entradas == 0:
            print("❌ No se seleccionó ninguna sala o entradas.")
            return
        cine_services.limpiar_pantalla()

        # Paso 4: Seleccionar butacas
        butacas_seleccionadas = cine_services.seleccionar_butacas(butaca_dao, cantidad_entradas, sala)
        if not butacas_seleccionadas:
            print("❌ No se seleccionaron butacas válidas.")
            return
        ids_butacas_seleccionadas = [butaca.id_butaca for butaca in butacas_seleccionadas]
        cine_services.limpiar_pantalla()

        # Paso 5: Confirmar reserva
        reserva = reserva_dao.crear_reserva(cliente.id_cliente, sala.id_sala, ids_butacas_seleccionadas)
        if not reserva:
            print("❌ No se pudo crear la reserva. Asegúrese de que los datos sean correctos.")
            return
        cine_services.limpiar_pantalla()

        # Paso 6: Seleccionar combos (opcional)
        combos_seleccionados = cine_services.seleccionar_combos(candy_dao)
        if combos_seleccionados:
            print("\n=== Combos Seleccionados ===")
            for combo in combos_seleccionados:
                print(f"- {combo.get_nombre()} - Precio: {combo.get_precio()}")
        else:
            print("No se seleccionaron combos.")
        cine_services.limpiar_pantalla()
        
        # Asociar los combos seleccionados a la reserva
        reserva.candy = combos_seleccionados

        # Paso 7: Imprimir resumen de la reserva
        reserva.mostrar_resumen()

        # Mensaje final
        print(f"✔ ¡Compra exitosa! Gracias por visitar Capybara Films, {cliente.nombre}.")

    except Exception as e:
        print(f"⚠ Se produjo un error crítico en la aplicación: {e}")
    finally:
        try:
            db_connection.cerrar_conexion()
        except Exception as e:
            print(f"⚠ Error cerrando la conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()