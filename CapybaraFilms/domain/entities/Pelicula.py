from capybarafilms.domain.entities.types import FormatoPelicula

class Pelicula:
    def __init__(self, nombre: str, director: str, duracion: int, genero: str, idioma: str, formato: FormatoPelicula):
        """Inicializa todos los atributos de la película."""
        self.nombre = nombre
        self.director = director
        self.duracion = duracion
        self.genero = genero
        self.idioma = idioma
        self.formato = formato

    def get_nombre(self) -> str:
        """Devuelve el nombre de la película."""
        return self.nombre

    def set_nombre(self, nombre: str):
        """Establece un nuevo nombre a la película."""
        self.nombre = nombre

    def get_director(self) -> str:
        """Devuelve el director de la película."""
        return self.director

    def set_director(self, director: str):
        """Establece un nuevo director a la película."""
        self.director = director

    def get_duracion(self) -> int:
        """Devuelve la duración de la película en minutos."""
        return self.duracion

    def set_duracion(self, duracion: int):
        """Establece una nueva duración a la película."""
        self.duracion = duracion

    def get_genero(self) -> str:
        """Devuelve el género de la película."""
        return self.genero

    def set_genero(self, genero: str):
        """Establece un nuevo género a la película."""
        self.genero = genero

    def get_idioma(self) -> str:
        """Devuelve el idioma de la película."""
        return self.idioma

    def set_idioma(self, idioma: str):
        """Establece un nuevo idioma a la película."""
        self.idioma = idioma

    def get_formato(self) -> FormatoPelicula:
        """Devuelve el formato de la película."""
        return self.formato

    def set_formato(self, formato: FormatoPelicula):
        """Establece un nuevo formato a la película."""
        self.formato = formato

    def __str__(self) -> str:
        """Devuelve una representación en texto de la película."""
        return f"Pelicula {{ nombre: '{self.nombre}', director: '{self.director}', duracion: {self.duracion}, genero: '{self.genero}', idioma: '{self.idioma}', formato: {self.formato} }}"