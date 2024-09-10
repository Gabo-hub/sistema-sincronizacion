import json
from PySide6 import QtWidgets, QtCore, QtGui
from views.buscar_dato import Ui_Buscar_dato
from connection.conexion_db import db_conexion

config = json.load(open("./config/config.json"))

class Buscar_dato(QtWidgets.QWidget):
    def __init__(self, tablas):
        super().__init__()
        self.ui = Ui_Buscar_dato()
        self.ui.setupUi(self) 
        self.icono = QtGui.QIcon()
        self.icono.addFile("./assets/icon_kparking.png")
        self.setWindowIcon(self.icono)
        self.setWindowModality(QtCore.Qt.ApplicationModal) # Hace que la ventana sea modal

        self.tablas = [''] # Lista de tablas
        self.tablas.extend(tablas)

        self.db = db_conexion(config["host"], config["database"]) # Conectar con la base de datos
        self.cursordb = self.db.cursor(dictionary=True, buffered=True)
        
        self.ui.combob_tabla.setCurrentIndex(-1) # Inicializa el combobox con una opción vacía
        self.ui.combob_tabla.addItems(self.tablas)
        self.ui.combob_tabla.currentTextChanged.connect(self.habilitar_columnas)

        self.ui.button_Buscar.clicked.connect(self.buscarDato)
        self.ui.button_Limpiar.clicked.connect(self.limpiar)

    def habilitar_columnas(self, tabla):
        if tabla:
            self.cursordb.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s ORDER BY ordinal_position", (tabla,))
            columnas = [columna['COLUMN_NAME'] for columna in self.cursordb.fetchall()]
            self.ui.combob_columna.clear()
            self.ui.combob_columna.setEnabled(True)
            self.ui.combob_columna.addItems(columnas)
        else:
            self.ui.combob_columna.clear()
            self.ui.combob_columna.setEnabled(False)

    def buscarDato(self):
        if self.ui.combob_tabla.currentText() == "" or self.ui.combob_columna.currentText() == "" or self.ui.linea_buscar.text() == "":
            return
        self.cursordb.execute("SELECT * FROM {} WHERE {} = %s LIMIT 1000".format(self.ui.combob_tabla.currentText(), self.ui.combob_columna.currentText()), (self.ui.linea_buscar.text(),))
        datos = self.cursordb.fetchall()
        self.ui.tree_tabla_busqueda.clear()
        # Obtener las columnas de la tabla actual
        columnas = list(datos[0].keys()) if datos else []

        # Configurar el número de columnas y las etiquetas del encabezado
        self.ui.tree_tabla_busqueda.setColumnCount(len(columnas))
        self.ui.tree_tabla_busqueda.setHeaderLabels(columnas)

        # Limpiar el árbol antes de agregar nuevos elementos
        self.ui.tree_tabla_busqueda.clear()

        # Agregar los datos al árbol
        for i, dato in enumerate(datos):
            item = QtWidgets.QTreeWidgetItem([str(dato[columna]) for columna in columnas])
            self.ui.tree_tabla_busqueda.addTopLevelItem(item)

        # Ajustar el tamaño de las columnas para que se ajusten al contenido
        for i in range(len(columnas)):
            self.ui.tree_tabla_busqueda.resizeColumnToContents(i)
    
    def limpiar(self):
        self.ui.combob_tabla.setCurrentIndex(-1)
        self.ui.combob_columna.setCurrentIndex(-1)
        self.ui.linea_buscar.clear()
        self.ui.tree_tabla_busqueda.clear()