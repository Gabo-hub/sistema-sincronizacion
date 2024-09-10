import json
from PySide6 import QtWidgets, QtCore, QtGui
from views.equipos_detalles import Ui_Equipos_Detalles
from connection.conexion_db import db_conexion

# Carga la configuración desde un archivo JSON
config = json.load(open("./config/config.json"))

class Equipos_Detalles(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Equipos_Detalles()
        self.ui.setupUi(self)
        
        # Configura el icono de la ventana
        self.icono = QtGui.QIcon()
        self.icono.addFile("./assets/icon_kparking.png")
        self.setWindowIcon(self.icono)
        
        # Hace que la ventana sea modal
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # Establece la conexión a la base de datos
        self.db = db_conexion(config["host"], config["database"])
        self.cursordb = self.db.cursor(dictionary=True, buffered=True)

        # Obtiene la lista de equipos de la base de datos
        self.cursordb.execute('SELECT * FROM equipos')
        self.consulta = self.cursordb.fetchall()
        self.consulta = [equipo["nombre"] for equipo in self.consulta]

        # Prepara la lista de equipos para el combo box
        self.equipos = ['']
        self.equipos.extend(self.consulta)
        
        # Agrega los equipos al combo box y conecta la señal de cambio
        self.ui.combo_equipos.addItems(self.equipos)
        self.ui.combo_equipos.currentTextChanged.connect(self.cargar_datos)

    def cargar_datos(self):
        if self.ui.combo_equipos.currentText() != '':
            # Carga los datos del equipo seleccionado
            self.cursordb.execute(f"SELECT * FROM equipos WHERE nombre = '{self.ui.combo_equipos.currentText()}'")
            self.consulta = self.cursordb.fetchall()
            
            # Muestra los datos del equipo en el árbol de información
            self.ui.tree_info_equipo.clear()
            self.ui.tree_info_equipo.setHeaderLabels(self.consulta[0].keys())
            item = QtWidgets.QTreeWidgetItem(self.ui.tree_info_equipo)
            for index, value in enumerate(self.consulta[0].values()):
                item.setText(index, str(value))
            self.ui.tree_info_equipo.addTopLevelItem(item)

            # Carga los datos de caché del equipo seleccionado
            self.cursordb.execute(f"SELECT * FROM cache_datos WHERE id_equipo = {self.consulta[0]['id_equipos']}")
            self.consulta = self.cursordb.fetchall()
            
            # Muestra los datos de caché en el árbol de información de datos
            self.ui.tree_info_datos.clear()
            if self.consulta:
                self.ui.tree_info_datos.setHeaderLabels(self.consulta[0].keys())
                for row in self.consulta:
                    item = QtWidgets.QTreeWidgetItem(self.ui.tree_info_datos)
                    for index, value in enumerate(row.values()):
                        item.setText(index, str(value))
                    self.ui.tree_info_datos.addTopLevelItem(item)
        else:
            # Limpia los árboles de información si no hay equipo seleccionado
            self.ui.tree_info_datos.clear()
            self.ui.tree_info_equipo.clear()