from connection.conexion_db import db_conexion
import datetime, json, os, logging, threading

config = json.load(open("./config/config.json"))
db = db_conexion(config["host"], config["database"])
cursor = db.cursor(dictionary=True, buffered=True)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Equipos:
    def __init__(self, cursor, db, tipo):
        self.equipos_online = []
        self.equipos_offline = []
        self.mensajes = []
        
        cursor.execute("SELECT * FROM equipos WHERE equipos.tipo = '{}'".format(tipo))
        self.equipos = cursor.fetchall()

        # -- Verificar conexión a los equipos, lista conectados / lista desconectados --
        for equipo in self.equipos:
            self.db_e = db_conexion(equipo["ip"], db)
            if not self.db_e or equipo["id_estatus"] != 1:
                resultado = f"[{datetime.datetime.now()}] [INFO] Equipo: {equipo['nombre']:<10} | Estado: {'No conectado':<17} | IP: {equipo['ip']:<15}"                
                self.mensajes.append(resultado)
                self.equipos_offline.append(equipo)
            else:
                resultado = f"[{datetime.datetime.now()}] [INFO] Equipo: {equipo['nombre']:<10} | {"Estado: Conectado.":<17}  |  IP: {equipo['ip']:<15}"
                self.mensajes.append(resultado)
                self.equipos_online.append(equipo)

class Manager_data:
    
    # -- Identifica si hay que trabajar con la tarjeta o con el codigo del ticket
    def ident_dato(dato):
        if dato["id_tarjeta"] == None or dato["id_tarjeta"] == "0":
            return "codigo_entrada"
        else:
            return "id_tarjeta"
    
    def ident_dato2(dato):
        if dato["id_tarjeta"] == None or dato["id_tarjeta"] == "0":
            return "codigo_salida"
        else:
            return "id_tarjeta"

    # -- Verifica si el dato ya existe en la base de datos especificada --
    def existe_dato(tabla, columna, valor, valor2, cursor):
        if columna != "id_tarjeta":
            cursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(tabla, columna, valor))
        else: 
            cursor.execute("SELECT * FROM {} WHERE {} = {} AND fecha_entrada = '{}'".format(tabla, columna, valor, valor2))
        busqueda = cursor.fetchall()
        if len(busqueda) > 0:
            return True, busqueda[0]
        else:
            return False
    
    # -- Cambiar estatus de un registro (Tabla, Colum_ref = Columna de condicion, Valor_ref = Valor de condicion, Valor_nuevo = Valor a nuevo) --
    def cambio_estatus(tabla, colum_ref, valor_ref, fecha_ref, valor_nuevo, cursor):
        try:
            if type(fecha_ref) != datetime.datetime:
                cursor.execute("UPDATE {} SET id_estatus = {} WHERE {} = {}".format(tabla, valor_nuevo if type(valor_nuevo) is int else "'"+str(valor_nuevo)+"'", colum_ref, valor_ref if type(valor_ref) is int else "'"+str(valor_ref)+"'"))
            else:
                cursor.execute("UPDATE {} SET id_estatus = {} WHERE {} = {} AND fecha_entrada = '{}'".format(tabla, valor_nuevo if type(valor_nuevo) is int else "'"+str(valor_nuevo)+"'", colum_ref, valor_ref if type(valor_ref) is int else "'"+str(valor_ref)+"'", fecha_ref))
        except Exception as e:
            print(e)
            return False
        else:
            return True

    # -- Ingresar datos a la base de datos --
    def ingresar_datos(tabla, dato, cursor):  
        estructura = cursor.description
        estructura = [i[0] for i in estructura]
        estructura = list(estructura)[1:]
        dato = list(dato.values())[1:]
          
        sentencia = "INSERT INTO {} ({}) VALUES ({})".format(tabla, ", ".join(k for k, z in zip(estructura, dato) if z is not None ), ", ".join("'{}'".format(str(i)) if type(i) is str or type(i) is datetime.datetime else str(i) for i in dato if i is not None))
        cursor.execute(sentencia)
    
    #-- Actualizar dato a la base de datos --
    def actualizar_dato(tabla, dato, colum_ref, valor_ref, fecha_ref, cursor):
        estructura = cursor.description
        estructura = [i[0] for i in estructura]
        estructura = list(estructura)[1:]
        dato = list(dato.values())[1:]
        
        cadena = "UPDATE {} SET {}".format(tabla, "".join("{} = {}, ".format(i, ("'"+str(j)+"'") if type(j) is str or type(j) is datetime.datetime else j) for i, j in zip(estructura, dato) if j is not None ))
        if colum_ref != "id_tarjeta":
            sentencia = cadena[:-2] + " WHERE {} = {}".format(colum_ref, "'{}'".format(str(valor_ref)) if type(valor_ref) is str else valor_ref)
        else :
            sentencia = cadena[:-2] + " WHERE {} = {} AND fecha_entrada = '{}'".format(colum_ref, "'{}'".format(str(valor_ref)) if type(valor_ref) is str else valor_ref, fecha_ref)
        cursor.execute(sentencia)

    # -- Ingresar a los datos a la cache --
    def ingresar_cache(equipo, dato, cursor, metodo, tipo):
        if tipo == 1:
            cursor.execute("INSERT INTO cache_datos (id_equipo, tip_equipo, nombr_tabla, nombr_campo, id_valor, fecha_dat, metodo, tipo) VALUES ({},'{}','{}','{}','{}','{}','{}', {})".format(equipo["id_equipos"], equipo["tipo"], "accesinout", Manager_data.ident_dato(dato), dato[Manager_data.ident_dato(dato)], dato["fecha_entrada"], metodo, tipo))
        else:
            if equipo["tipo"] == "T":
                cursor.execute("INSERT INTO cache_datos (id_equipo, tip_equipo, nombr_tabla, nombr_campo, id_valor, metodo, tipo) VALUES ({},'{}','{}','{}','{}','{}',{})".format(equipo["id_equipos"], equipo["tipo"], "accesinout", "codigo_salida", dato["codigo_salida"], metodo, tipo))
            if equipo["tipo"] == "S":
                cursor.execute("INSERT INTO cache_datos (id_equipo, tip_equipo, nombr_tabla, nombr_campo, id_valor, fecha_dat, metodo, tipo) VALUES ({},'{}','{}','{}','{}','{}','{}', {})".format(equipo["id_equipos"], equipo["tipo"], "accesinout", Manager_data.ident_dato(dato), dato[Manager_data.ident_dato(dato)], dato["fecha_entrada"], metodo, tipo))

    # -- Ingresar a los datos a la cache_sync --
    def ingresar_cache_sync(equipo, dato, cursor):
        cursor.execute("INSERT INTO cache_datos_sync (id_equipo_sync, nombr_tabla_sync, valor_sync, metodo_sync, id_llave_sync) VALUES ({},'{}','{}','{}','{}')".format(equipo["id_equipos"], dato["nombr_tabla"], dato["id_valor"], dato["metodo"], dato["id_cache"]))

# -- Actualizar los datos a la cache --
class ActualizacionService:
    def __init__(self, equipos):
        self.equipos = equipos
        self._inicializar_cache()
        self.equipos_actualizados = {}

    def _inicializar_cache(self):
        try:
            cursor.execute("SELECT * FROM accesinout WHERE id_estatus = '21' AND version = '1' AND id_condicion IN ('1', '4') AND fecha_salida IS NULL")
            for i in cursor.fetchall():
                cursor.execute("INSERT INTO cache_datos (id_equipo, tip_equipo, nombr_tabla, nombr_campo, id_valor, fecha_dat, metodo, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                               (999, "P", "accesinout", Manager_data.ident_dato(i), i[Manager_data.ident_dato(i)], i["fecha_entrada"] or None, "actualizar", 1))
                Manager_data.cambio_estatus("accesinout", Manager_data.ident_dato(i), i[Manager_data.ident_dato(i)], i["fecha_entrada"], 1, cursor)
            
            cursor.execute("INSERT INTO cache_datos_sync (id_equipo_sync, nombr_tabla_sync, valor_sync, metodo_sync, id_llave_sync) SELECT cd.id_equipo, cd.nombr_tabla, cd.id_valor, cd.metodo, cd.id_cache FROM cache_datos cd LEFT JOIN cache_datos_sync cdy ON cdy.id_llave_sync = cd.id_cache AND cd.id_equipo = cdy.id_equipo_sync WHERE cdy.id_llave_sync IS NULL AND cd.id_equipo != 999")
            
            db.commit()
        except Exception as e:
            logging.error(f"[{datetime.datetime.now()}] [ERROR] en la inicialización de cache: {e}")
            yield f"[{datetime.datetime.now()}] [ERROR] en la inicialización de cache: {e}"

    def _actualizar_tipo(self, tipo, equipos_adicionales=None):
        try:
            cursor.execute("SELECT * FROM cache_datos WHERE tipo = %s AND fecha_act IS NULL",(tipo,))
            busqueda = cursor.fetchall()
            
            equipos_list = [self.equipos]
            if equipos_adicionales:
                equipos_list.extend(equipos_adicionales)

            self.equipos_actualizados = {}
            for i in busqueda:
                if all(self.confirmar_actualizacion(equipos, i) for equipos in equipos_list):
                    cursor.execute("UPDATE cache_datos SET fecha_act = NOW() WHERE id_cache = %s", (i["id_cache"],))
                    db.commit()
                    if i["id_equipo"] in self.equipos_actualizados:
                        self.equipos_actualizados[i["id_equipo"]] += 1
                    else:
                        self.equipos_actualizados[i["id_equipo"]] = 1
            
            for equipo, cantidad in self.equipos_actualizados.items():
                yield f"[{datetime.datetime.now()}] [INFO] Equipo:{equipo:16} | {cantidad} datos actualizados / ingresados"
            yield f"\n[{datetime.datetime.now()}] [INFO] Total de equipos actualizados para tipo {tipo}: {len(self.equipos_actualizados)}"
            yield "\n-------------------------------------------------------------------------------------\n"
        except Exception as e:
            yield f"[{datetime.datetime.now()}] [ERROR] en la actualización de tipo {tipo}: {e}"
            logging.error(f"Error en la actualización de tipo {tipo}: {e}")

    def actualizar_tipo1(self):
        yield "\n-------------------------------------------------------------------------------------\nActualización de datos: De tipo 1\n"
        equipos_t = Equipos(cursor, config["database"], "T")
        yield from equipos_t.mensajes
        equipos_s = Equipos(cursor, config["database"], "S")
        yield from equipos_s.mensajes
        yield from self._actualizar_tipo(1, [equipos_t, equipos_s])

    def actualizar_tipo2(self):
        yield "\n-------------------------------------------------------------------------------------\nActualización de datos: De tipo 2\n"
        equipos_t = Equipos(cursor, config["database"], "T")
        yield from equipos_t.mensajes
        equipos_s = Equipos(cursor, config["database"], "S")
        yield from equipos_s.mensajes
        yield from self._actualizar_tipo(2, [equipos_t, equipos_s])
    
    def actualizar_tipo3(self):
        yield "Actualización de datos: De tipo 3\n"
        equipos_e = Equipos(cursor, config["database"], "E")
        yield from equipos_e.mensajes
        equipos_s = Equipos(cursor, config["database"], "S")
        yield from equipos_s.mensajes
        yield from self._actualizar_tipo(3, [equipos_e, equipos_s])
    
    def confirmar_actualizacion(self, equipos, dato):
        total_equipos = len(equipos.equipos_online) + len(equipos.equipos_offline)
        return sum(1 for equipo in equipos.equipos_online if self._procesar_equipo(equipo, dato)) == total_equipos

    def _procesar_equipo(self, equipo, dato):
        if dato["id_equipo"] == equipo["id_equipos"] or (dato["nombr_campo"] == "id_tarjeta" and equipo["tipo"] == "T"):
            return True

        with db_conexion(equipo["ip"], config["database"]) as db_e:
            with db_e.cursor(dictionary=True, buffered=True) as cursor_db2:
                if self._verificar_cache_sync(dato, equipo):
                    return True
                
                if dato["tip_equipo"] == "T" and dato["tipo"] == 2 and equipo["tipo"] == "T":
                    dato_actual = Manager_data.existe_dato(dato["nombr_tabla"], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor)    
                    dato_actual[1]
                    
                    cursor_db2.execute("SELECT * FROM accesinout WHERE codigo_entrada = '{}'".format(dato_actual[1]["codigo_entrada"]))
                    dato_viejo = cursor_db2.fetchone()
                    
                    nombr_campo_original = dato["nombr_campo"]
                    valor_campo_original = dato["id_valor"]
                    
                    dato["id_valor"] = dato_actual[1]["codigo_entrada"]
                    dato["nombr_campo"] = "codigo_entrada"

                    if dato_viejo:
                        resultado = self._actualizar_dato_existente(dato, equipo, cursor_db2, db_e)
                    else:
                        resultado = self._ingresar_nuevo_dato(dato, equipo, cursor_db2, db_e)
                    
                    dato["nombr_campo"] = nombr_campo_original
                    dato["id_valor"] = valor_campo_original
                    return resultado
                
                if dato["tip_equipo"] == "E" and dato["nombr_campo"] == 'id_tarjeta':
                    cursor_db2.execute("SELECT * FROM accesinout WHERE id_tarjeta = %s", (dato["id_valor"],))
                    dato_viejo = cursor_db2.fetchone()
                    if dato_viejo:
                        return self._actualizar_dato_existente(dato, equipo, cursor_db2, db_e)
                    else:
                        return self._ingresar_nuevo_dato(dato, equipo, cursor_db2, db_e)
                    
                dato_viejo = Manager_data.existe_dato(dato["nombr_tabla"], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor_db2)
                return self._actualizar_dato_existente(dato, equipo, cursor_db2, db_e) if dato_viejo else self._ingresar_nuevo_dato(dato, equipo, cursor_db2, db_e)

    def _verificar_cache_sync(self, dato, equipo):
        cursor.execute("SELECT 1 FROM cache_datos_sync WHERE id_llave_sync = %s AND id_equipo_sync = %s", (dato["id_cache"], equipo["id_equipos"]))
        return cursor.fetchone() is not None

    def _actualizar_dato_existente(self, dato, equipo, cursor_db2, db_e):
        dato_act = Manager_data.existe_dato(dato["nombr_tabla"], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor)
        if not dato_act:
            return False

        try:
            if dato["tipo"] == 1:
                self._actualizar_tipo1(dato, dato_act, equipo, cursor_db2)
            elif dato["tipo"] == 2:
                self._actualizar_tipo2(dato, dato_act, equipo, cursor_db2)
            elif dato["tipo"] == 3:
                Manager_data.actualizar_dato(dato["nombr_tabla"], dato_act[1], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor_db2)

            Manager_data.ingresar_cache_sync(equipo, dato, cursor)
            db_e.commit()
            return True
        except Exception as e:
            logging.error(f"Error en la actualización de datos: {e}")
            db_e.rollback()
        return False

    def _actualizar_tipo1(self, dato, dato_act, equipo, cursor_db2):
        if equipo["tipo"] == "E":
            Manager_data.actualizar_dato(dato["nombr_tabla"], dato_act[1], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor_db2)
        else:
            cursor_db2.execute("UPDATE {} SET fecha_entrada = %s, id_entrada = %s, foto_entrada = %s, serie_entrada = %s WHERE {} = %s".format(dato["nombr_tabla"], dato["nombr_campo"]), 
                               (dato_act[1]["fecha_entrada"], dato_act[1]["id_entrada"], dato_act[1]["foto_entrada"], dato_act[1]["serie_entrada"], dato["id_valor"]))

    def _actualizar_tipo2(self, dato, dato_act, equipo, cursor_db2):
        if dato['tip_equipo'] == "T" and equipo["tipo"] == "T" or dato["tip_equipo"] == "T" and equipo["tipo"] == "S":
            cursor_db2.execute("UPDATE accesinout SET fecha_entrada = %s, id_entrada = %s, foto_entrada = %s, codigo_entrada = %s, serie_entrada = %s, id_taquilla = %s, id_factura = %s, codigo_salida = %s, id_pases = %s, placa_vehiculo = %s WHERE {} = %s".format(dato["nombr_campo"]), 
                               (dato_act[1]["fecha_entrada"], dato_act[1]["id_entrada"], dato_act[1]["foto_entrada"], dato_act[1]["codigo_entrada"], dato_act[1]["serie_entrada"], dato_act[1]["id_taquilla"], dato_act[1]["id_factura"], dato_act[1]["codigo_salida"], dato_act[1]["id_pases"], dato_act[1]["placa_vehiculo"], dato["id_valor"]))
        elif dato['tip_equipo'] == "S" and equipo["tipo"] == "S" or dato["tip_equipo"] == "S" and equipo["tipo"] == "T":
            Manager_data.actualizar_dato(dato["nombr_tabla"], dato_act[1], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor_db2)

    def _ingresar_nuevo_dato(self, dato, equipo, cursor_db2, db_e):
        dato_act = Manager_data.existe_dato(dato["nombr_tabla"], dato["nombr_campo"], dato["id_valor"], dato["fecha_dat"], cursor)
        if not dato_act:
            return False

        try:
            if dato["tipo"] == 1 and dato["nombr_campo"] == "codigo_entrada" and equipo["tipo"] == 'S':
                return True
            Manager_data.ingresar_datos(dato["nombr_tabla"], dato_act[1], cursor_db2)
            Manager_data.ingresar_cache_sync(equipo, dato, cursor)
            db_e.commit()
            return True
        except Exception as e:
            logging.error(f"Error en el ingreso de datos: {e}")
            db_e.rollback()
        return False
