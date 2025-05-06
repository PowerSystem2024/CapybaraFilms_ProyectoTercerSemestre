class Butaca:
    def __init__(self, categoria, ubicacion):
        self.ubicacion = ubicacion  # Asigna la ubicación de la butaca (fila, número).
        self.categoria = categoria  # Asigna el tipo de butaca (común o premium).
        self.estado = False  # Por defecto, la butaca está libre (estado = False).

    def set_estado(self, estado):
        #Cambia el estado de la butaca (ocupada o libre)
        self.estado = estado

    def get_categoria(self):
        #Devuelve el tipo de butaca.
        return self.categoria

    def is_estado(self):
        #Verifica si la butaca está ocupada (True) o libre (False)
        return self.estado

    def get_ubicacion(self):
        #Devuelve la ubicación de la butaca (fila y número)
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        #Cambia la ubicación de la butaca
        self.ubicacion = ubicacion
