class Ubicacion:
    # Esta clase representa la posición de una butaca en el cine.
    
    def __init__(self, fila, butaca):
        # Constructor que inicializa la fila y la butaca.
        self.fila = fila  # Asignamos el número de fila
        self.butaca = butaca  # Asignamos el número de la butaca
    
    # Metodos:
    # Devuelve el número de fila.
    def get_fila(self):
        return self.fila
    
    # Permite cambiar el número de fila.
    def set_fila(self, fila):
        self.fila = fila  # Actualiza el número de fila
    
    # Devuelve el número de la butaca.
    def get_butaca(self):
        return self.butaca
    
    # Permite cambiar el número de la butaca.
    def set_butaca(self, butaca):
        self.butaca = butaca  # Actualiza el número de la butaca
