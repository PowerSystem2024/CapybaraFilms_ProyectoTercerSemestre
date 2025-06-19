# Importaciones necesarias para el módulo
from datetime import datetime
from domain.entities.types.TipoButaca import TipoButaca
from domain.entities.Cliente import Cliente
from domain.entities.types.TipoCandy import TipoCandy
from domain.entities.Sala import Sala

class Reserva:
    def __init__(self, cliente, sala, candy=None, butacas_asignadas=None, fecha_hora=None, id_reserva=None):
        """
        Constructor de la clase Reserva.
        
        Args:
            cliente (Cliente): Objeto que representa al cliente que hace la reserva
            sala (Sala): Objeto que representa la sala de cine
            candy (list, optional): Lista de objetos Candy (combos de comida). Defaults to None.
            butacas_asignadas (list, optional): Lista de butacas reservadas. Defaults to None.
            fecha_hora (datetime, optional): Fecha y hora de la reserva. Si es None, usa la fecha/hora actual.
            id_reserva (str, optional): Identificador único de la reserva. Normalmente asignado por la BD.
        """
        self.id_reserva = id_reserva  # Identificador único de la reserva (opcional, asignado por la BD).
        self.cliente = cliente       # Referencia al objeto Cliente.
        self.sala = sala             # Referencia al objeto Sala.
        self.candy = candy           # Referencia al objeto Candy (puede ser None).
        self.butacas_asignadas = butacas_asignadas if butacas_asignadas else []  # Lista de butacas, vacía si no se proporciona
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now()  # Fecha actual si no se especifica

    def calcular_precio_total(self):
        """
        Calcula el precio total de la reserva sumando:
        - El precio de todas las butacas reservadas
        - El precio de los combos de candy (si existen)
        
        Returns:
            float: Precio total de la reserva
        """
        total = 0.0

        # Sumar el precio de las butacas reservadas
        for butaca in self.butacas_asignadas:
            try:
                # Obtiene el precio según la categoría de la butaca (usando el enum TipoButaca)
                total += TipoButaca[butaca.get_categoria().upper()].get_precio()
            except Exception as e:
                print(f"Error al calcular precio de la butaca: {e}")

        # Sumar el costo de candy (si aplica)
        if self.candy:
            for candy in self.candy:
                try:
                    total += candy.get_precio()
                except Exception as e:
                    print(f"Error al calcular precio del combo: {e}")

        return total
    
    def mostrar_resumen(self):
        """
        Muestra por pantalla un resumen detallado de la reserva con formato legible.
        Incluye:
        - Información del cliente
        - Detalles de la sala
        - Listado de butacas con sus precios
        - Combos seleccionados (si hay)
        - Total a pagar
        """
        from services.cine_services import CineServices
        try:
            print("\n----------------------------------------------")
            print("--           Resumen de la Reserva           --")
            print("----------------------------------------------")
            print(f"Cliente: {self.cliente.get_nombre()} {self.cliente.get_apellido()}")
            print(f"Correo electrónico: {self.cliente.get_email()}")
            print(f"Sala asignada: {self.sala.id_sala}")

            # Resumen de butacas reservadas
            print("\nButacas Reservadas:")
            total_butacas = 0  # Para acumular el precio de las butacas reservadas
            for butaca in self.butacas_asignadas:
                # Usar la función `obtener_precio_por_categoria` desde cine_services
                precio = CineServices.obtener_precio_por_categoria(butaca.get_categoria())
                total_butacas += precio
                print(f" - Fila: {butaca.get_fila()}, Columna: {butaca.get_columna()} | Categoria: {butaca.get_categoria()} | Precio: {precio}")

            # Combos seleccionados
            print("\nCombos Seleccionados:")
            total_combos = 0  # Para acumular el precio de los combos seleccionados
            if self.candy:
                for candy in self.candy:
                    print(f" - {candy.get_nombre()} | Precio: {candy.get_precio()}")
                    total_combos += candy.get_precio()
            else:
                print("No se seleccionaron combos.")
            
            # Calcular el total general
            total = total_butacas + total_combos
            print("\n----------------------------------------------")
            print(f"Total a Pagar: {total}")
            print("----------------------------------------------")
            print(f"Usted recibirá su comprobante al correo electrónico: {self.cliente.get_email()}\n")

        except Exception as e:
            print(f"Error al mostrar el resumen de la reserva: {e}")