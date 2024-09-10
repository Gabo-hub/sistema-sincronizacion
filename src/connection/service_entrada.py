import time, os, json, logging, datetime
import threading
import mysql.connector
from connection.conexion_db import tabla_crear
from connection.controladores import Manager_data, Equipos, ActualizacionService as actualizar

config = json.load(open("./config/config.json"))
logging.basicConfig(level=logging.ERROR)

class ServiceEntrada(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mg_dat = Manager_data

    def db_conexion(self, IP, BD):
        try:
            mydb = mysql.connector.connect(
                host=IP,
                user=config["user"],
                password=config["password"],
                database=BD,
                connect_timeout=3,
                collation='utf8mb4_general_ci'
            )
        except Exception as e:
            logging.error(f"No se pudo conectar a la base de datos: {e}")
            return False

        tabla_crear(mydb, config["tablas"])
        return mydb

    def run(self):
        try:
            with self.db_conexion(config["host"], config["database"]) as db:
                with db.cursor(dictionary=True, buffered=True) as cursor:
                    yield f"[{datetime.datetime.now()}] [INFO] Realizando consulta de conexion de equipos"
                    
                    equipos = Equipos(cursor, config["database"], "E")

                    yield from equipos.mensajes
                    yield "\n-------------------------------------------------------------------------------------\n"
                    for equipo in equipos.equipos_online:
                        yield from self.procesar_equipo(equipo, cursor, db)

                    yield from actualizar(equipos).actualizar_tipo1()

        except Exception as e:
            logging.error(f"Error en la funcion principal: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] En la funcion principal: {e}"

    def procesar_equipo(self, equipo, cursor, db):
        datos_ingresados = datos_actualizados = 0
        try:
            with self.db_conexion(equipo["ip"], config["database"]) as db_e:
                with db_e.cursor(dictionary=True, buffered=True) as cursor_db2:
                    cursor_db2.execute("SELECT * FROM accesinout WHERE accesinout.id_estatus = 21")
                    datos = cursor_db2.fetchall()

                    for dato in datos:
                        ingresado, actualizado = self.procesar_dato(dato, cursor, cursor_db2, equipo)
                        datos_ingresados += ingresado
                        datos_actualizados += actualizado

                    db.commit()
                    db_e.commit()
                    db_e.close()
            
            yield f"[{datetime.datetime.now()}] [INFO] Equipo {equipo['nombre']:<10} | Datos ingresados: {datos_ingresados:<2} | Datos actualizados: {datos_actualizados}"
        except Exception as e:
            logging.error(f"Error procesando equipo {equipo['nombre']}: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] Procesando equipo {equipo['nombre']}: {e}"

    def procesar_dato(self, dato, cursor, cursor_db2, equipo):
        try:
            dato_exis = self.mg_dat.existe_dato("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"] if self.mg_dat.ident_dato(dato) == "id_tarjeta" else "x", cursor)
            
            if dato_exis:
                if dato_exis[1]["id_condicion"] == 1 or dato_exis[1]["id_condicion"] == 4:
                    self.mg_dat.actualizar_dato("accesinout", dato, self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"] if self.mg_dat.ident_dato(dato) == "id_tarjeta" else "x", cursor)
                    self.mg_dat.cambio_estatus("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], 1, cursor_db2)
                    self.mg_dat.ingresar_cache(equipo, dato, cursor, "actualizo", 1)
                    self.mg_dat.cambio_estatus("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], 1, cursor)
                else:
                    cursor.execute("UPDATE accesinout SET `id_estatus` = %s, `fecha_entrada` = %s, `id_entrada` = %s, `foto_entrada` = %s, `serie_entrada` = %s WHERE `codigo_entrada` = %s", (1, dato["fecha_entrada"], dato["id_entrada"], dato["foto_entrada"], dato["serie_entrada"], dato["codigo_entrada"]))
                    self.mg_dat.cambio_estatus("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], 1, cursor_db2)
                    cursor.execute("INSERT INTO cache_datos (id_equipo, tip_equipo, nombr_tabla, nombr_campo, id_valor, fecha_dat, metodo, tipo) VALUES ({},'{}','{}','{}','{}','{}','{}', {})".format(999, "P", "accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], "actualizo", 1))
                return 0, 1
            else:
                self.mg_dat.ingresar_datos("accesinout", dato, cursor)
                self.mg_dat.cambio_estatus("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], 1, cursor_db2)
                self.mg_dat.ingresar_cache(equipo, dato, cursor, "ingreso", 1)
                self.mg_dat.cambio_estatus("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], 1, cursor)
                return 1, 0
        except Exception as e:
            logging.error(f"Error procesando dato: {e}")
            return 0, 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == '__main__':
    service = ServiceEntrada()
    service.start()