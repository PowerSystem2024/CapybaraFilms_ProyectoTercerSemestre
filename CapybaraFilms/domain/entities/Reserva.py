# Importación de Clases
# Clase Ubicación
from capybarafilms.domain.entities.types import Ubicacion

class Reserva:
    # Método inicializador de la reserva con el cliente, sala, combo(candy) y butacas
    def __init__(self, cliente, sala, candy, butacas_asignadas):
        # Sala -> donde se proyectará la película
        self.sala = sala
        # Candy -> Combo comprado (puede ser 'None')
        self.candy = candy
        # Cliente -> Persona que realiza la reserva
        self.cliente = cliente
        # Butacas Asignadas -> Lista de las butacas reservadas
        self.butacas_asignadas = butacas_asignadas  # Lista de butacas reservadas

    # Métodos Getter
    # Método para obtener la sala de la reserva.
    def get_sala(self):
        return self.sala
    
    # Método para obtener el combo de la reserva (puede ser 'None').
    def get_candy(self):
        return self.candy
    
    # Método para obtener el cliente de la reserva.
    def get_cliente(self):
        return self.cliente

    # Método que calcula el precio total de la reserva.
    def get_precio_total(self):
        # Inicializa el total en cero
        total = 0.0  
        
        # Ciclo for
        for butaca in self.butacas_asignadas:
            # Obtiene de la ubicación de la butaca.
            ubicacion = butaca.get_ubicacion() 
            
            # Sentencia if
            if ubicacion is not None:
                # Suma el precio de la entrada
                total += self.sala.precio_de_entrada(ubicacion)  
            else:
                # Mensaje de error
                print("Error: La ubicación de la butaca es nula.")  
        
        # Sentencia if
        if self.candy is not None:
            # Suma el precio del combo si existe
            total += self.candy.get_tipo().get_precio()  

        # Devuelve el total calculado    
        return total  

    # Método que muestra un resumen de la reserva.
    def mostrar_resumen(self):
        print("----------------------------------------------")
        print("--    Resumen de la Reserva:    --")
        print("----------------------------------------------")
        print(f"Cliente: {self.cliente.get_nombre()} {self.cliente.get_apellido()}")
        print(f"Sala: {str(self.sala)}")
        print("Butacas Reservadas:")

        # Inicializa el total de entradas   
        total_entradas = 0.0  
        
        # Ciclo for
        for butaca in self.butacas_asignadas:
            tipo = butaca.get_categoria().get_nombre()
            precio_entrada = self.sala.precio_de_entrada(butaca.get_ubicacion())
            total_entradas += precio_entrada
            
            print(f" - Fila: {butaca.get_ubicacion().get_fila()}, "
                  f"Butaca: {butaca.get_ubicacion().get_butaca()} | "
                  f"Tipo: {tipo} | "
                  f"Precio: {precio_entrada}")
            print("-----------------------------------------------------")
        
        # Sentencia if
        # Si se eligió el combo
        if self.candy is not None:
            precio_combo = self.candy.get_tipo().get_precio()
            print(f"Combo elegido: {self.candy.get_tipo().get_nombre()} | "
                  f"Precio: {precio_combo}")
        # Si no se eligió ningún combo (None)
        else:
            print("No se eligió combo.")
        
        # Calcula el total de todo (entradas y combo(candy))
        total = total_entradas + (self.candy.get_tipo().get_precio() if self.candy is not None else 0)
        
        print("--------------------------------------------------------")
        print(f"Total a Pagar: {total}")
        print("--------------------------------------------------------")
        print(f"Usted recibirá su comprobante al correo electrónico: {self.cliente.get_eMail()}")
