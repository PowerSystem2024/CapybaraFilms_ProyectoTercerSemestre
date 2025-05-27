import psycopg2

class Butaca:
    def __init__(self, categoria, ubicacion, estado=False, id_butaca=None):
        self.id_butaca = id_butaca
        self.ubicacion = ubicacion
        self.categoria = categoria
        self.estado = estado

    def set_estado(self, estado):
        self.estado = estado

    def get_categoria(self):
        return self.categoria

    def is_estado(self):
        return self.estado

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def conectar(self):
        try:
            return psycopg2.connect(
                database="capybara_films",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def guardar(self):
        conn = self.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    if self.id_butaca is None:
                        cur.execute("""
                            INSERT INTO butacas (categoria, ubicacion, estado)
                            VALUES (%s, %s, %s) RETURNING id_butaca
                        """, (self.categoria, self.ubicacion, self.estado))
                        self.id_butaca = cur.fetchone()[0]
                    else:
                        cur.execute("""
                            UPDATE butacas SET categoria=%s, ubicacion=%s, estado=%s
                            WHERE id_butaca=%s
                        """, (self.categoria, self.ubicacion, self.estado, self.id_butaca))
                conn.commit()
                print("Butaca guardada correctamente.")
            except Exception as e:
                print(f"Error guardando butaca: {e}")
            finally:
                conn.close()

    def eliminar(self):
        if self.id_butaca is None:
            print("No se puede eliminar, la butaca no existe en la base.")
            return
        conn = self.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM butacas WHERE id_butaca = %s", (self.id_butaca,))
                conn.commit()
                print("Butaca eliminada correctamente.")
                self.id_butaca = None
            except Exception as e:
                print(f"Error eliminando butaca: {e}")
            finally:
                conn.close()

    @staticmethod
    def obtener_por_id(id_butaca):
        conn = None
        try:
            conn = psycopg2.connect(
                database="capybara_films",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            with conn.cursor() as cur:
                cur.execute("SELECT id_butaca, categoria, ubicacion, estado FROM butacas WHERE id_butaca = %s",
                            (id_butaca,))
                row = cur.fetchone()
                if row:
                    return Butaca(categoria=row[1], ubicacion=row[2], estado=row[3], id_butaca=row[0])
        except Exception as e:
            print(f"Error obteniendo butaca: {e}")
        finally:
            if conn:
                conn.close()
        return None

    @staticmethod
    def listar_todas():
        conn = None
        butacas = []
        try:
            conn = psycopg2.connect(
                database="capybara_films",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            with conn.cursor() as cur:
                cur.execute("SELECT id_butaca, categoria, ubicacion, estado FROM butacas")
                rows = cur.fetchall()
                for row in rows:
                    butacas.append(Butaca(categoria=row[1], ubicacion=row[2], estado=row[3], id_butaca=row[0]))
        except Exception as e:
            print(f"Error listando butacas: {e}")
        finally:
            if conn:
                conn.close()
        return butacas