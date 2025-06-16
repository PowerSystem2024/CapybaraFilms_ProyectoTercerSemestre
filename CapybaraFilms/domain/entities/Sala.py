# Definición de la clase Sala, que representa una sala de cine
class Sala:
    
    # Método constructor (__init__) que se ejecuta al crear una nueva instancia de la clase
    def __init__(self, id_sala, id_pelicula=None):
        """
        Inicializador de la clase Sala.
        :param id_sala: Identificador único de la sala.
        :param id_pelicula: Identificador de la película que se proyecta en esta sala (opcional).
        """
        self.id_sala = id_sala            # Asigna el ID de la sala al atributo de la instancia
        self.id_pelicula = id_pelicula    # Asigna el ID de la película (si se pasa uno) al atributo
        self.butacas = []                 # Inicializa una lista vacía para representar las butacas de la sala

    # Decorador @property para acceder al ID de la sala como si fuera un atributo, pero en realidad es un método
    @property
    def get_id_sala(self):
        return self.id_sala               # Devuelve el ID de la sala

    # Método para establecer (modificar) el ID de la sala
    def set_id_sala(self, id_sala):
        self.id_sala = id_sala            # Asigna un nuevo ID a la sala

    # Decorador @property para acceder al ID de la película como si fuera un atributo
    @property
    def get_id_pelicula(self):
        return self.id_pelicula           # Devuelve el ID de la película asignada a la sala

    # Método para establecer (modificar) el ID de la película
    def set_id_pelicula(self, id_pelicula):
        self.id_pelicula = id_pelicula    # Asigna un nuevo ID de película a la sala

    # Método especial que define cómo se representará un objeto Sala cuando se lo convierta a cadena (por ejemplo, con print)
    def __str__(self):
        return f"Sala ID: {self.id_sala}, Película ID: {self.id_pelicula}"
        # Devuelve un string con los IDs de la sala y la película para mostrar información resumida
