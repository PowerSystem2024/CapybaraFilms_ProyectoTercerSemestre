class Butaca:
    def __init__(self,id_butaca,fila, columna,categoria,estado=False):
        self.id_butaca = id_butaca #identificador de la butaca
        self.categoria = categoria #categoría de la butaca(ej: común o premium)
        self.fila = fila #fila donde se encuentra esa butaca
        self.columna = columna #columna donde se encunetra la buatac
        self.estado = estado  #estado de ocupación, si está ocupada o libre

    #método para cambiar el estado de la butaca
    def set_estado(self, estado):
        self.estado = estado

    #Nos devuelve la categoría de la butaca
    def get_categoria(self):
        return self.categoria

    #devuelve true si está ocupada y false si está libre
    def is_estado(self):
        return self.estado

    def get_ubicacion(self):#la ubicación de la butaca seleccionada
        return self.ubicacion
    
    def set_categoria(self, categoria):#si es común o premium
        self.categoria = categoria

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def get_fila(self): #fila donde está ubicada la butaca
        return self.fila
    
    def get_columna(self): #columna donde está ubicada la butaca
        return self.columna

    def __str__(self): # texto a imprimir de la butaca seleccionada por el cliente
        return f"Categoria: {self.categoria}, Ubicacion: {self.ubicacion}, Estado: {'Ocupada' if self.estado else 'Libre'}"