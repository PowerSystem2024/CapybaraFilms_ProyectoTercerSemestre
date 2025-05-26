from domain.entities.types.Ubicacion import Ubicacion
from domain.entities.Cliente import Cliente
from domain.entities.Butaca import Butaca
from domain.entities.Sala import Sala

# Excepción personalizada
class ReservaException(Exception):
    """Excepción personalizada para errores en reservas."""
    pass

class Reserva:
    def __init__(self, cliente, sala, candy, butacas_asignadas):
        self.cliente = cliente
        self.sala = sala
        self.candy = candy
        self.butacas_asignadas = butacas_asignadas

    def get_sala(self):
        return self.sala

    def get_candy(self):
        return self.candy

    def get_cliente(self):
        return self.cliente

    def get_precio_total(self):
        total = 0.0

        for butaca in self.butacas_asignadas:
            try:
                ubicacion = butaca.get_ubicacion()
                if ubicacion is None:
                    raise ReservaException("Ubicación de butaca es nula.")
                total += self.sala.precio_de_entrada(ubicacion)
            except Exception as e:
                print(f"Error al calcular precio de butaca: {e}")
        
        try:
            if self.candy is not None:
                total += self.candy.get_tipo().get_precio()
        except Exception as e:
            print(f"Error al calcular precio del combo: {e}")
        
        return total

    def mostrar_resumen(self):
        try:
            print("----------------------------------------------")
            print("--    Resumen de la Reserva:    --")
            print("----------------------------------------------")
            print(f"Cliente: {self.cliente.get_nombre()} {self.cliente.get_apellido()}")
            print(f"Sala: {str(self.sala)}")
            print("Butacas Reservadas:")

            total_entradas = 0.0
            for butaca in self.butacas_asignadas:
                try:
                    tipo = butaca.get_categoria().get_nombre()
                    ubicacion = butaca.get_ubicacion()
                    if ubicacion is None:
                        raise ReservaException("Ubicación de butaca es nula.")
                    precio_entrada = self.sala.precio_de_entrada(ubicacion)
                    total_entradas += precio_entrada

                    print(f" - Fila: {ubicacion.get_fila()}, "
                          f"Butaca: {ubicacion.get_butaca()} | "
                          f"Tipo: {tipo} | "
                          f"Precio: {precio_entrada}")
                    print("-----------------------------------------------------")
                except Exception as e:
                    print(f"Error en butaca: {e}")

            if self.candy is not None:
                try:
                    precio_combo = self.candy.get_tipo().get_precio()
                    print(f"Combo elegido: {self.candy.get_tipo().get_nombre()} | "
                          f"Precio: {precio_combo}")
                except Exception as e:
                    print(f"Error al mostrar combo: {e}")
            else:
                print("No se eligió combo.")
            
            total = total_entradas + (self.candy.get_tipo().get_precio() if self.candy is not None else 0)
            print("--------------------------------------------------------")
            print(f"Total a Pagar: {total}")
            print("--------------------------------------------------------")
            print(f"Usted recibirá su comprobante al correo electrónico: {self.cliente.get_email()}")

        except Exception as e:
            print(f"Error al mostrar resumen de la reserva: {e}")
