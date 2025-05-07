package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.TipoCandy;

public class Candy {

    private TipoCandy tipo; // El tipo de combo: chico, mediano o grande.

    // Constructor que recibe el tipo de combo.
    public Candy(TipoCandy tipo) {
        this.tipo = tipo; // Se asigna el tipo de combo.
    }

    // Devuelve el tipo de combo que se ha seleccionado.
    public TipoCandy getTipo() {
        return tipo; // Se devuelve el tipo de candy.
    }

    // Método para mostrar el nombre del combo cuando se imprime.
    @Override
    public String toString() {
        return "Candy: " + tipo.getNombre(); // Devuelve el nombre del tipo de candy.
    }    
}
