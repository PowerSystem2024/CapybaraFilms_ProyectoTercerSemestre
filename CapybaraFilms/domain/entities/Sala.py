class Sala:
    def __init__(self, id_sala, id_pelicula=None):
        """
        Inicializador de la clase Sala.
        :param id_sala: Identificador único de la sala.
        :param id_pelicula: Identificador de la película que se proyecta en esta sala (opcional).
        """
        self.id_sala = id_sala
        self.id_pelicula = id_pelicula
        self.butacas = []

    @property
    def get_id_sala(self):
        return self.id_sala

    def set_id_sala(self, id_sala):
        self.id_sala = id_sala
        
    @property
    def get_id_pelicula(self):
        return self.id_pelicula

    def set_id_pelicula(self, id_pelicula):
        self.id_pelicula = id_pelicula

    def __str__(self):
        return f"Sala ID: {self.id_sala}, Película ID: {self.id_pelicula}"