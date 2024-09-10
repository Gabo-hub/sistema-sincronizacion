import os, time, json, datetime, logging
import threading
import mysql.connector
from connection.conexion_db import tabla_crear
from connection.controladores import Manager_data, Equipos, ActualizacionService as actualizar

config = json.load(open("./config/config.json"))

class ServiceSalida(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mg_dat = Manager_data

    def db_conexion(self, IP, BD):
        try:
            # Establecemos la conexión a la base de datos
            mydb = mysql.connector.connect(
                host= IP,  # Dirección IP del servidor del puerto MySQL
                user= config["user"],  # Usuario de acceso a la base de datos
                password= config["password"],  # Contraseña de acceso a la base de datos
                database= BD,  # Nombre de la base de datos a la que se desea conectar
                connect_timeout= 3,  # Tiempo máximo de espera para establecer la conexión
                collation= 'utf8mb4_general_ci'  # Configuración de la codificación de caracteres
            )
        except Exception as e:
            # Si hay un error al establecer la conexión, mostramos el mensaje de error
            #print("No se pudo conectar a la base de datos: ", e)
            logging.error(" No se pudo conectar a la base de datos: " + str(e))
            return False

        # Creamos las tablas en la base de datos si no existen
        tabla_crear(mydb, config["tablas"])

        return mydb

    def run(self):
        try:
            # Conexión a la base de datos
            with self.db_conexion(config["host"], config["database"]) as db:
                with db.cursor(dictionary=True, buffered=True) as cursor:
                    yield f"[{datetime.datetime.now()}] [INFO] Conectando con las salidas"
                    
                    # Obtener los equipos en línea
                    equipos = Equipos(cursor, config["database"], "S")

                    yield from equipos.mensajes
                    yield "\n-------------------------------------------------------------------------------------\n"
                    # Procesar cada equipo en línea
                    for equipo in equipos.equipos_online:
                        yield from self.procesar_equipo(equipo, cursor, db)

                # Actualizar los datos de tipo 2

                yield from actualizar(equipos).actualizar_tipo2()

                logging.info("Datos enviados a las Salidas")
                yield f"[{datetime.datetime.now()}] [INFO] Datos enviados a las Salidas"

        except Exception as e:
            logging.error(f"ERROR: Error en la funcion principal: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] Error en la funcion principal: {e}"

    def procesar_equipo(self, equipo, cursor, db):
        datos_actualizados = 0
        try:
            # Establecer conexión con la base de datos del equipo
            with self.db_conexion(equipo["ip"], config["database"]) as db_e:
                with db_e.cursor(dictionary=True, buffered=True) as cursor_e:
                    # Consultar los datos de accesinout que cumplen ciertas condiciones
                    cursor_e.execute("SELECT * FROM accesinout WHERE (id_estatus = 21 AND id_condicion IN (3, 5)) AND version = 1")
                    datos = cursor_e.fetchall()

                    # Procesar cada dato obtenido
                    for dato in datos:
                        # Verificar si el dato ya existe en la base de datos principal
                        if self.mg_dat.existe_dato("accesinout", self.mg_dat.ident_dato2(dato), dato[self.mg_dat.ident_dato2(dato)], dato["fecha_entrada"], cursor):
                            # Actualizar el dato si ya existe
                            self.actualizar_dato(dato, cursor, db, cursor_e, db_e, equipo)
                            datos_actualizados += 1

            yield f"[{datetime.datetime.now()}] [INFO] Equipo {equipo['nombre']:10} | Datos Completados: {datos_actualizados}"
        except Exception as e:
            logging.error(f"Error procesando equipo {equipo['nombre']}: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] Error procesando equipo {equipo['nombre']}: {e}"

    def actualizar_dato(self, dato, cursor, db, cursor_e, db_e, equipo):
        ident = self.mg_dat.ident_dato2(dato)
        # Actualizar el dato en la base de datos principal
        cursor.execute(f"UPDATE accesinout SET id_condicion = %s, fecha_salida = %s, id_salida = %s, foto_salida = %s, saldo_anterior = %s, monto_cobrado = %s, saldo_actual = %s, version = 3, id_estatus = 1 WHERE {ident} = %s",
                       (dato["id_condicion"], dato["fecha_salida"], dato["id_salida"], dato["foto_salida"], dato["saldo_anterior"], dato["monto_cobrado"], dato["saldo_actual"], dato[ident]))
        db.commit()

        # Ingresar el dato en la caché
        self.mg_dat.ingresar_cache(equipo, dato, cursor, "actualizo", 2)
        db.commit()

        # Actualizar el dato en la base de datos del equipo
        cursor_e.execute(f"UPDATE accesinout SET version = 3, id_estatus = 1 WHERE {ident} = %s", (dato[ident],))
        db_e.commit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    service = ServiceSalida()
    service.start()