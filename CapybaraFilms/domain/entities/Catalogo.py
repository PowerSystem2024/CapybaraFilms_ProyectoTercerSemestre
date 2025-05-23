import psycopg2
from enum import Enum

class FormatoPelicula(Enum):
    DOS_D = "2D"
    TRES_D = "3D"

class Pelicula:
    def __init__(self, nombre, director, duracion, genero, idioma, formato):
        self.nombre = nombre
        self.director = director
        self.duracion = duracion
        self.genero = genero
        self.idioma = idioma
        self.formato = formato

class Catalogo:
    def __init__(self):
        self.db_config = {
            'dbname': 'capybara_films',
            'user': 'postgres',
            'password': '1234',
            'host': 'localhost',
            'port': '5433'
        }

    def conectar(self):
        try:
            return psycopg2.connect(**self.db_config)
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def insertar_pelicula(self, pelicula):
        conn = self.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO peliculas (nombre, director, duracion, genero, idioma, formato)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        pelicula.nombre,
                        pelicula.director,
                        pelicula.duracion,
                        pelicula.genero,
                        pelicula.idioma,
                        pelicula.formato.value
                    ))
                conn.commit()
                print(f"Película '{pelicula.nombre}' insertada exitosamente")
            except Exception as e:
                print(f"Error al insertar película: {e}")
            finally:
                conn.close()

    def insertar_varias_peliculas(self, peliculas):
        conn = self.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    for pelicula in peliculas:
                        cur.execute("""
                            INSERT INTO peliculas (nombre, director, duracion, genero, idioma, formato)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, (
                            pelicula.nombre,
                            pelicula.director,
                            pelicula.duracion,
                            pelicula.genero,
                            pelicula.idioma,
                            pelicula.formato.value
                        ))
                conn.commit()
                print("Películas insertadas correctamente")
            except Exception as e:
                print(f"Error al insertar películas: {e}")
            finally:
                conn.close()

    def get_peliculas(self):
        conn = self.conectar()
        peliculas = []
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM peliculas")
                    for row in cur.fetchall():
                        formato = FormatoPelicula.DOS_D if row[6] == "2D" else FormatoPelicula.TRES_D
                        pelicula = Pelicula(
                            nombre=row[1],
                            director=row[2],
                            duracion=row[3],
                            genero=row[4],
                            idioma=row[5],
                            formato=formato
                        )
                        peliculas.append(pelicula)
            except Exception as e:
                print(f"Error al obtener películas: {e}")
            finally:
                conn.close()
        return peliculas

    def mostrar_peliculas(self):
        conn = self.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM peliculas")
                    peliculas = cur.fetchall()
                    if peliculas:
                        print("\nPelículas en la base de datos:")
                        for pelicula in peliculas:
                            print(f"ID: {pelicula[0]}")
                            print(f"Nombre: {pelicula[1]}")
                            print(f"Director: {pelicula[2]}")
                            print(f"Duración: {pelicula[3]} minutos")
                            print(f"Género: {pelicula[4]}")
                            print(f"Idioma: {pelicula[5]}")
                            print(f"Formato: {pelicula[6]}")
                            print("-" * 50)
                    else:
                        print("No hay películas en la base de datos")
            except Exception as e:
                print(f"Error al mostrar películas: {e}")
            finally:
                conn.close()

    def probar_conexion(self):
        try:
            conn = self.conectar()
            if conn:
                print("¡Conexión exitosa a la base de datos!")
                conn.close()
            return True
        except Exception as e:
            print(f"Error al conectar: {e}")
            return False

# Lista de películas a insertar
peliculas = [
    Pelicula("Cuando el terror acecha", "John Carpenter", 100, "Terror", "Español", FormatoPelicula.DOS_D),
    Pelicula("El Señor de los Anillos: La Comunidad del Anillo", "Peter Jackson", 178, "Aventura", "Español", FormatoPelicula.DOS_D),
    Pelicula("El Padrino", "Francis Ford Coppola", 175, "Crimen", "Español", FormatoPelicula.DOS_D),
    Pelicula("Forrest Gump", "Robert Zemeckis", 142, "Drama", "Español", FormatoPelicula.DOS_D),
    Pelicula("Jurassic Park", "Steven Spielberg", 127, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D),
    Pelicula("Star Wars: Episodio IV - Una Nueva Esperanza", "George Lucas", 121, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D),
    Pelicula("Matrix", "Lana Wachowski, Lilly Wachowski", 136, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D),
    Pelicula("Coco", "Lee Unkrich, Adrian Molina", 105, "Animación", "Español", FormatoPelicula.DOS_D),
    Pelicula("La La Land", "Damien Chazelle", 128, "Musical", "Español", FormatoPelicula.DOS_D),
    Pelicula("El gran Lebowski", "Joel Coen, Ethan Coen", 117, "Comedia", "Español", FormatoPelicula.DOS_D),
    Pelicula("Pulp Fiction", "Quentin Tarantino", 154, "Crimen", "Español", FormatoPelicula.DOS_D),
    Pelicula("Los Increíbles", "Brad Bird", 115, "Animación", "Español", FormatoPelicula.DOS_D),
    Pelicula("El Rey León", "Roger Allers, Rob Minkoff", 88, "Animación", "Español", FormatoPelicula.DOS_D),
    Pelicula("Gladiador", "Ridley Scott", 155, "Acción", "Español", FormatoPelicula.DOS_D),
    Pelicula("Avatar", "James Cameron", 162, "Ciencia Ficción", "Español", FormatoPelicula.TRES_D),
    Pelicula("Harry Potter y la piedra filosofal", "Chris Columbus", 152, "Aventura", "Español", FormatoPelicula.DOS_D),
    Pelicula("Los Vengadores", "Joss Whedon", 143, "Acción", "Español", FormatoPelicula.DOS_D),
]

# Ejemplo de uso
if __name__ == "__main__":
    catalogo = Catalogo()
    catalogo.probar_conexion()
    catalogo.insertar_varias_peliculas(peliculas)
    catalogo.mostrar_peliculas()
