import json, time   
from PySide6 import QtWidgets, QtCore, QtGui
from views.main_windows import Ui_MainWindow

from connection.conexion_db import db_conexion
from connection.service_taquilla import ServiceTaquilla
from connection.service_entrada import ServiceEntrada
from connection.service_salida import ServiceSalida

from controllers.buscar_dato import Buscar_dato
from controllers.equipos_detalles import Equipos_Detalles

config = json.load(open("./config/config.json"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.icono = QtGui.QIcon()
        self.icono.addFile("./assets/icon_kparking.png")
        self.setWindowIcon(self.icono)

        # Iniciar Y detener servicios 
        self.ui.button_iniciarT.clicked.connect(self.iniciar_servicios)
        self.ui.button_detenerT.clicked.connect(self.detener_servicios)
        self.ui.button_iniciarE.clicked.connect(self.iniciar_servicios)
        self.ui.button_detenerE.clicked.connect(self.detener_servicios)
        self.ui.button_iniciarS.clicked.connect(self.iniciar_servicios)
        self.ui.button_detenerS.clicked.connect(self.detener_servicios)

        # Estatus de los hilos/Trabajadores
        self.trabajador = None
        self.is_ejecutando = False

        # Limpiar consolas
        self.ui.button_limpiarE.clicked.connect(lambda: self.limpiar_consola("entrada"))
        self.ui.button_limpiarS.clicked.connect(lambda: self.limpiar_consola("salida"))
        self.ui.button_limpiarT.clicked.connect(lambda: self.limpiar_consola("taquilla"))

        #Cargar Equipos de la tabla de equipos
        self.db = db_conexion(config["host"], config["database"])
        self.cursordb = self.db.cursor(dictionary=True, buffered=True)
        self.cursordb.execute("SELECT * FROM equipos")
        equipos = self.cursordb.fetchall()
        self.cargarEquiposTabla(equipos)
        self.ui.tree_tabla_equipos.header().setStretchLastSection(False)
        self.ui.tree_tabla_equipos.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.ui.tree_tabla_equipos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.tree_tabla_equipos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ui.tree_tabla_equipos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # Mostrar Ventanas
        self.ui.menu_Datos.actions()[0].triggered.connect(lambda: self.buscarDato(self.obtener_tablas()))
        self.ui.menu_Equipos.actions()[0].triggered.connect(lambda: self.equiposDetalles())
        self.ui.actionEntradas.triggered.connect(lambda: self.exportarDatos(1))
        self.ui.actionSalidas.triggered.connect(lambda: self.exportarDatos(2))
        self.ui.actionTaquillas.triggered.connect(lambda: self.exportarDatos(3))

        # Iniciar servicios automáticamente
        self.iniciar_servicios()

    def exportarDatos(self, tipo):
        # Crear un diálogo para mostrar el progreso de la exportación
        dialogo = QtWidgets.QDialog(self)
        dialogo.setWindowTitle("Exportando datos")
        diseno = QtWidgets.QVBoxLayout(dialogo)
        barra_progreso = QtWidgets.QProgressBar(dialogo)
        barra_progreso.setRange(0, 100)
        diseno.addWidget(barra_progreso)
        etiqueta_estado = QtWidgets.QLabel("Exportando...", dialogo)
        diseno.addWidget(etiqueta_estado)
        caja_botones = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        caja_botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
        caja_botones.accepted.connect(dialogo.accept)
        caja_botones.rejected.connect(dialogo.reject)
        diseno.addWidget(caja_botones)

        dialogo.setLayout(diseno)
        dialogo.setFixedSize(300, 150)

        def tarea_exportacion():
            # Seleccionar el texto y la ruta del archivo según el tipo de exportación
            if tipo == 1:
                texto = self.ui.text_console_entradas.toPlainText()
                ruta_archivo = './export/entradas.log'
            elif tipo == 2:
                texto = self.ui.text_console_salidas.toPlainText()
                ruta_archivo = './export/salidas.log'
            elif tipo == 3:
                texto = self.ui.text_console_taquillas.toPlainText()
                ruta_archivo = './export/taquillas.log'
            
            total_caracteres = len(texto)
            caracteres_por_paso = max(1, total_caracteres // 100)
            
            # Escribir el archivo y actualizar la barra de progreso
            with open(ruta_archivo, 'w') as archivo:
                duracion_total = min(2000, max(500, total_caracteres * 2000 // 500))  # Entre 0.5 y 2 segundos
                pasos = 100
                tiempo_por_paso = duracion_total // pasos
                for i in range(0, total_caracteres, caracteres_por_paso):
                    archivo.write(texto[i:i+caracteres_por_paso])
                    progreso = min(100, int((i + caracteres_por_paso) / total_caracteres * 100))
                    barra_progreso.setValue(progreso)
                    etiqueta_estado.setText(f"Exportando... {progreso}%")
                    QtWidgets.QApplication.processEvents()
                    QtCore.QThread.msleep(tiempo_por_paso)
            
            # Actualizar el estado final
            etiqueta_estado.setText("Exportación completada")
            barra_progreso.setValue(100)
            caja_botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
            caja_botones.button(QtWidgets.QDialogButtonBox.Cancel).setEnabled(False)

        # Usar QTimer para iniciar la tarea de exportación después de que se muestre el diálogo
        QtCore.QTimer.singleShot(100, tarea_exportacion)

        dialogo.exec_()
        

    def equiposDetalles(self):
        # Mostrar la ventana de detalles de equipos
        self.equipos_detalles = Equipos_Detalles()
        self.equipos_detalles.show()

    def buscarDato(self, tablas):
        # Mostrar la ventana de búsqueda de datos
        self.buscar_dato = Buscar_dato(tablas)
        self.buscar_dato.show()
    
    def obtener_tablas(self):
        # Obtener la lista de tablas de la base de datos
        self.cursordb.execute("SHOW TABLES")
        tablas = [tabla['Tables_in_kparking3'] for tabla in self.cursordb.fetchall()]
        return tablas
    
    def limpiar_consola(self, tipo):
        # Limpiar la consola según el tipo especificado
        if tipo == "taquilla":
            self.ui.text_console_taquillas.clear()
        elif tipo == "entrada":
            self.ui.text_console_entradas.clear()
        elif tipo == "salida":
            self.ui.text_console_salidas.clear()

    def cargarEquiposTabla(self, equipos):
        # Cargar los equipos en la tabla de la interfaz
        for i, equipo in enumerate(equipos):
            self.ui.tree_tabla_equipos.insertTopLevelItems(i, [QtWidgets.QTreeWidgetItem([str(equipo["id_equipos"]),equipo["numero"],equipo["nombre"],equipo["ubicacion"],equipo["ip"], str(equipo["id_estatus"])])])
            self.ui.tree_tabla_equipos.resizeColumnToContents(i)

    def iniciar_servicios(self):
        # Iniciar los servicios si no están en ejecución
        if not self.is_ejecutando:
            self.trabajador = ServiceTrabajo()
            self.trabajador.update_signal.connect(self.actualizar_texto)
            self.trabajador.start()
            self.is_ejecutando = True
            # Actualizar el estado de los botones
            self.ui.button_detenerT.setEnabled(True)
            self.ui.button_iniciarT.setEnabled(False)
            self.ui.button_detenerE.setEnabled(True)
            self.ui.button_iniciarE.setEnabled(False)
            self.ui.button_detenerS.setEnabled(True)
            self.ui.button_iniciarS.setEnabled(False)

    def detener_servicios(self):
        # Detener los servicios si están en ejecución
        if self.trabajador:
            self.trabajador.stop()
            self.trabajador.wait()
            self.trabajador = None
        self.is_ejecutando = False
        # Actualizar el estado de los botones
        self.ui.button_detenerT.setEnabled(False)
        self.ui.button_iniciarT.setEnabled(True)
        self.ui.button_detenerE.setEnabled(False)
        self.ui.button_iniciarE.setEnabled(True)
        self.ui.button_detenerS.setEnabled(False)
        self.ui.button_iniciarS.setEnabled(True)
        # Mostrar mensajes de detención en las consolas
        self.actualizar_texto(("taquilla", "Todos los procesos detenidos."))
        self.actualizar_texto(("entrada", "Todos los procesos detenidos."))
        self.actualizar_texto(("salida", "Todos los procesos detenidos."))

    def actualizar_texto(self, texto):
        # Actualizar el texto en la consola correspondiente
        tipo, mensaje = texto
        if tipo == "entrada":
            self.ui.text_console_entradas.append(mensaje)
        elif tipo == "taquilla":
            self.ui.text_console_taquillas.append(mensaje)
        elif tipo == "salida":
            self.ui.text_console_salidas.append(mensaje)

class ServiceTrabajo(QtCore.QThread):
    update_signal = QtCore.Signal(tuple)

    def __init__(self):
        super().__init__()
        self.is_ejecutando = True
        self.services = [
            ("entrada", ServiceEntrada()),
            ("taquilla", ServiceTaquilla()),
            ("salida", ServiceSalida())
        ]

    def run(self):
        # Ejecutar los servicios en un bucle mientras is_ejecutando sea True
        while self.is_ejecutando:
            for tipo, service in self.services:
                try:
                    if hasattr(service, 'refresh_database'):
                        service.refresh_database()
                    for message in service.run():
                        if not self.is_ejecutando:
                            return
                        self.update_signal.emit((tipo, message))
                    if hasattr(service, 'update_moved_data'):
                        service.update_moved_data()
                    time.sleep(config[f"tiempo_{tipo}"])
                except Exception as e:
                    self.update_signal.emit((tipo, f"Error en {tipo}: {str(e)}"))

    def stop(self):
        # Detener la ejecución de los servicios
        self.is_ejecutando = False
        for _, service in self.services:
            if hasattr(service, '_stop'):
                service._stop()

    def refresh(self):
        # Actualizar los datos de los servicios
        for _, service in self.services:
            if hasattr(service, 'refresh_database'):
                service.refresh_database()
            if hasattr(service, 'update_moved_data'):
                service.update_moved_data()