import os, time, json, datetime, logging
import threading
import mysql.connector
from connection.conexion_db import tabla_crear
from connection.controladores import Manager_data, Equipos, ActualizacionService as actualizar

config = json.load(open("./config/config.json"))

class ServiceTaquilla(threading.Thread):
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
            # Establecer conexión con la base de datos
            with self.db_conexion(config["host"], config["database"]) as db:
                with db.cursor(dictionary=True, buffered=True) as cursor:
                    yield f"[{datetime.datetime.now()}] [INFO] Conectando con las taquillas"   
                    
                    # Crear instancia de Equipos para obtener equipos online
                    equipos = Equipos(cursor, config["database"], "T")

                    yield from equipos.mensajes
                    yield "\n-------------------------------------------------------------------------------------\n"
                    # Procesar cada equipo online
                    for equipo in equipos.equipos_online:
                        yield from self.procesar_equipo(equipo, cursor, db)

                # Actualizar datos de tipo 2 y 3

                yield from actualizar(equipos).actualizar_tipo2()
                yield from actualizar(equipos).actualizar_tipo3()

                logging.info("Datos enviados a las Taquillas")
                yield f"[{datetime.datetime.now()}] [INFO] Datos enviados a las Taquillas"

        except Exception as e:
            logging.error(f"ERROR: Error en la funcion principal: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] en la funcion principal: {e}"

    def procesar_equipo(self, equipo, cursor, db):
        datos_actualizados = 0
        try:
            # Establecer conexión con la base de datos del equipo
            with self.db_conexion(equipo["ip"], config["database"]) as db_e:
                with db_e.cursor(dictionary=True, buffered=True) as cursor_e:
                    # Obtener datos de accesinout con condiciones específicas
                    cursor_e.execute("SELECT * FROM accesinout WHERE id_estatus = 21 AND id_condicion = 2 AND version = 1")
                    datos = cursor_e.fetchall()

                    # Procesar cada dato obtenido
                    for dato in datos:
                        # Verificar si el dato ya existe en la base de datos principal
                        dato_exis = self.mg_dat.existe_dato("accesinout", self.mg_dat.ident_dato(dato), dato[self.mg_dat.ident_dato(dato)], dato["fecha_entrada"], cursor)
                        if dato_exis:
                            # Actualizar el dato existente
                            self.actualizar_dato(dato, dato_exis, equipo, cursor, cursor_e, db, db_e)
                            datos_actualizados += 1

            yield f"[{datetime.datetime.now()}] [INFO] Equipo {equipo['nombre']:10} | Datos Completados: {datos_actualizados}"
        except Exception as e:
            logging.error(f"Error procesando equipo {equipo['nombre']}: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] Error procesando equipo {equipo['nombre']}: {e}"

    def actualizar_dato(self, dato, dato_exis, equipo, cursor, cursor_e, db, db_e):
        # Actualizar el dato en la base de datos principal
        cursor.execute("UPDATE accesinout SET id_condicion = %s, id_taquilla = %s, id_factura = %s, codigo_salida = %s, id_pases = %s, placa_vehiculo = %s, version = 2 WHERE codigo_entrada = %s", 
                       (dato["id_condicion"], dato["id_taquilla"], dato["id_factura"], dato["codigo_salida"], dato["id_pases"], dato['placa_vehiculo'], dato_exis[1]["codigo_entrada"]))
        db.commit()
        
        # Ingresar el dato actualizado en la caché
        dato_actualizado = dato_exis[1].copy()
        dato_actualizado["codigo_salida"] = dato["codigo_salida"]
        self.mg_dat.ingresar_cache(equipo, dato_actualizado, cursor, "actualizo", 2)
        db.commit()

        # Actualizar el dato en la base de datos del equipo
        cursor_e.execute("UPDATE accesinout SET id_entrada = %s, foto_entrada = %s, serie_entrada = %s, id_estatus = 1, version = 2 WHERE codigo_entrada = %s", 
                         (dato_exis[1]["id_entrada"], dato["foto_entrada"], dato["serie_entrada"], dato_exis[1]["codigo_entrada"]))
        db_e.commit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")