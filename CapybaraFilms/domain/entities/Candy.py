from capybarafilms.domain.entities.types import TipoCandy

class Candy:
    def __init__(self, tipo: TipoCandy):
        """Inicializa el objeto Candy con un tipo de combo."""
        self.tipo = tipo

    def get_tipo(self) -> TipoCandy:
        """Devuelve el tipo de combo que se ha seleccionado."""
        return self.tipo

    def __str__(self) -> str:
        """Devuelve el nombre del combo cuando se imprime."""
        return f"Candy: {self.tipo.get_nombre()}"