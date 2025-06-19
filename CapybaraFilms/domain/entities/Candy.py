from domain.entities.types.TipoCandy import TipoCandy

class Candy:
    def __init__(self, tipo):
        self.tipo = tipo  # Se asigna el tipo de combo

    def get_tipo(self):
        return self.tipo  # Devuelve el tipo de candy

    def __str__(self):
        return f"Candy: {TipoCandy.get_nombre()}"  # Muestra el nombre del candy

    @staticmethod
    def obtener_combo():
        combos = [
            TipoCandy.CHICO,
            TipoCandy.MEDIANO,
            TipoCandy.GRANDE,
        ]
        print("👨‍👩‍👧‍👦🍿🥤  Seleccione el combo deseado:")
        for producto, combo in enumerate(combos, start=1):
            print(f"[{producto}] {combo.get_nombre()}")

        while True:
            try:
                opc = int(input(" 🍿🥤  Seleccione el número de combo: "))
                if 1 <= opc <= len(combos):
                    return Candy(combos[opc - 1])  # Crear y devolver el objeto Candy con el tipo seleccionado
                else:
                    print(f"Por favor, seleccione un número entre 1 y {len(combos)}.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")