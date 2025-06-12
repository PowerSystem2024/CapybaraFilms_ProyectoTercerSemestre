class Butaca:
    def __init__(self,id_butaca,fila, columna,categoria,estado=False):
        self.id_butaca = id_butaca
        self.categoria = categoria
        self.fila = fila
        self.columna = columna
        self.estado = estado
        
    def set_estado(self, estado):
        self.estado = estado

    def get_categoria(self):
        return self.categoria
    
    def is_estado(self):
        return self.estado

    def get_ubicacion(self):
        return self.ubicacion
    
    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def get_fila(self):
        return self.fila
    
    def get_columna(self):
        return self.columna

    def __str__(self):
        return f"Categoria: {self.categoria}, Ubicacion: {self.ubicacion}, Estado: {'Ocupada' if self.estado else 'Libre'}"