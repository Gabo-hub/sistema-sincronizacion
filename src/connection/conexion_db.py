import mysql.connector
import json
import logging
import datetime

# Log de informacion por errores de la db
logging.basicConfig(filename="./Logs/Registro.log", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Configuracion por json 
config = json.load(open("./config/config.json"))

def db_conexion(IP, BD):
    
    """
    Esta funcion establece una conexión a una base de datos MySQL.
    Recibe dos parametros: 
        IP: la direccion IP del servidor del puerto MySQL/MariaDB
        BD: el nombre de la base de datos a la que se desea conectar
    Retorna una conexión a la base de datos si se pudo establecer la conexión,
    de lo contrario retorna False.
    """
    
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

def tabla_crear(DB, tablas):

    """
    Esta funcion crea las tablas en la base de datos si no existen.
    Recibe dos parametros: 
        DB :una conexión a la base de datos 
        tablas: un diccionario con las tablas y sus campos.
    """

    cursor = DB.cursor(buffered=True)
    
    for tabla_nombre, tabla_valor in tablas.items():

        # Creamos la consulta SQL para crear la tabla
        crear_tabla = f"""
            CREATE TABLE IF NOT EXISTS {tabla_nombre} 
                ({', '.join([f"{columna_nombre} {tipo_dato}" for columna_nombre, tipo_dato in tabla_valor.items()])}) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """     
        
        try:
            # Ejecutamos la consulta SQL para crear la tabla
            cursor.execute(crear_tabla)
            # Confirmamos los cambios en la base de datos
            DB.commit()
        except mysql.connector.Error as e:
            # Si hay un error, mostramos el mensaje de error y revertimos los cambios en la base de datos
            print("No se pudo crear la tabla: ", e)
            DB.rollback()
