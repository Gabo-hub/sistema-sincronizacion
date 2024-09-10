# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowsONeKLb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 608)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.actionEntradas = QAction(MainWindow)
        self.actionEntradas.setObjectName(u"actionEntradas")
        self.actionTaquillas = QAction(MainWindow)
        self.actionTaquillas.setObjectName(u"actionTaquillas")
        self.actionSalidas = QAction(MainWindow)
        self.actionSalidas.setObjectName(u"actionSalidas")
        self.actionBuscar_Datos = QAction(MainWindow)
        self.actionBuscar_Datos.setObjectName(u"actionBuscar_Datos")
        self.actionDetalle_Equipos = QAction(MainWindow)
        self.actionDetalle_Equipos.setObjectName(u"actionDetalle_Equipos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.container_consoles = QVBoxLayout()
        self.container_consoles.setObjectName(u"container_consoles")
        self.container_Entradas = QVBoxLayout()
        self.container_Entradas.setObjectName(u"container_Entradas")
        self.label_titulo_entradas = QLabel(self.centralwidget)
        self.label_titulo_entradas.setObjectName(u"label_titulo_entradas")
        font = QFont()
        font.setPointSize(11)
        self.label_titulo_entradas.setFont(font)

        self.container_Entradas.addWidget(self.label_titulo_entradas)

        self.text_console_entradas = QTextEdit(self.centralwidget)
        self.text_console_entradas.setObjectName(u"text_console_entradas")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(29, 29, 29, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(43, 43, 43, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(36, 36, 36, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(14, 14, 14, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(19, 19, 19, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(17, 17, 17, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush9 = QBrush(QColor(255, 255, 255, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush10 = QBrush(QColor(14, 14, 14, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(20, 20, 20, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.text_console_entradas.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(10)
        self.text_console_entradas.setFont(font1)
        self.text_console_entradas.setUndoRedoEnabled(True)
        self.text_console_entradas.setReadOnly(True)

        self.container_Entradas.addWidget(self.text_console_entradas)

        self.container_botonesE = QHBoxLayout()
        self.container_botonesE.setObjectName(u"container_botonesE")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.container_botonesE.addItem(self.horizontalSpacer_3)

        self.button_iniciarE = QPushButton(self.centralwidget)
        self.button_iniciarE.setObjectName(u"button_iniciarE")
        self.button_iniciarE.setFont(font)

        self.container_botonesE.addWidget(self.button_iniciarE)

        self.button_detenerE = QPushButton(self.centralwidget)
        self.button_detenerE.setObjectName(u"button_detenerE")
        self.button_detenerE.setEnabled(False)
        self.button_detenerE.setFont(font)

        self.container_botonesE.addWidget(self.button_detenerE)

        self.button_limpiarE = QPushButton(self.centralwidget)
        self.button_limpiarE.setObjectName(u"button_limpiarE")
        self.button_limpiarE.setFont(font)

        self.container_botonesE.addWidget(self.button_limpiarE)


        self.container_Entradas.addLayout(self.container_botonesE)


        self.container_consoles.addLayout(self.container_Entradas)

        self.container_Taquillas = QVBoxLayout()
        self.container_Taquillas.setObjectName(u"container_Taquillas")
        self.label_titulo_taquillas = QLabel(self.centralwidget)
        self.label_titulo_taquillas.setObjectName(u"label_titulo_taquillas")
        self.label_titulo_taquillas.setFont(font)

        self.container_Taquillas.addWidget(self.label_titulo_taquillas)

        self.text_console_taquillas = QTextEdit(self.centralwidget)
        self.text_console_taquillas.setObjectName(u"text_console_taquillas")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.text_console_taquillas.setPalette(palette1)
        self.text_console_taquillas.setFont(font1)
        self.text_console_taquillas.setReadOnly(True)

        self.container_Taquillas.addWidget(self.text_console_taquillas)

        self.container_botonesT = QHBoxLayout()
        self.container_botonesT.setObjectName(u"container_botonesT")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.container_botonesT.addItem(self.horizontalSpacer)

        self.button_iniciarT = QPushButton(self.centralwidget)
        self.button_iniciarT.setObjectName(u"button_iniciarT")
        self.button_iniciarT.setFont(font)

        self.container_botonesT.addWidget(self.button_iniciarT)

        self.button_detenerT = QPushButton(self.centralwidget)
        self.button_detenerT.setObjectName(u"button_detenerT")
        self.button_detenerT.setEnabled(False)
        self.button_detenerT.setFont(font)

        self.container_botonesT.addWidget(self.button_detenerT)

        self.button_limpiarT = QPushButton(self.centralwidget)
        self.button_limpiarT.setObjectName(u"button_limpiarT")
        self.button_limpiarT.setFont(font)

        self.container_botonesT.addWidget(self.button_limpiarT)


        self.container_Taquillas.addLayout(self.container_botonesT)


        self.container_consoles.addLayout(self.container_Taquillas)

        self.container_Salidas = QVBoxLayout()
        self.container_Salidas.setObjectName(u"container_Salidas")
        self.label_titulo_taquillas_2 = QLabel(self.centralwidget)
        self.label_titulo_taquillas_2.setObjectName(u"label_titulo_taquillas_2")
        self.label_titulo_taquillas_2.setFont(font)

        self.container_Salidas.addWidget(self.label_titulo_taquillas_2)

        self.text_console_salidas = QTextEdit(self.centralwidget)
        self.text_console_salidas.setObjectName(u"text_console_salidas")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.text_console_salidas.setPalette(palette2)
        self.text_console_salidas.setFont(font1)
        self.text_console_salidas.setReadOnly(True)

        self.container_Salidas.addWidget(self.text_console_salidas)

        self.container_botonesS = QHBoxLayout()
        self.container_botonesS.setObjectName(u"container_botonesS")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.container_botonesS.addItem(self.horizontalSpacer_2)

        self.button_iniciarS = QPushButton(self.centralwidget)
        self.button_iniciarS.setObjectName(u"button_iniciarS")
        self.button_iniciarS.setFont(font)

        self.container_botonesS.addWidget(self.button_iniciarS)

        self.button_detenerS = QPushButton(self.centralwidget)
        self.button_detenerS.setObjectName(u"button_detenerS")
        self.button_detenerS.setEnabled(False)
        self.button_detenerS.setFont(font)

        self.container_botonesS.addWidget(self.button_detenerS)

        self.button_limpiarS = QPushButton(self.centralwidget)
        self.button_limpiarS.setObjectName(u"button_limpiarS")
        self.button_limpiarS.setFont(font)

        self.container_botonesS.addWidget(self.button_limpiarS)


        self.container_Salidas.addLayout(self.container_botonesS)


        self.container_consoles.addLayout(self.container_Salidas)


        self.horizontalLayout_4.addLayout(self.container_consoles)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.tree_tabla_equipos = QTreeWidget(self.centralwidget)
        self.tree_tabla_equipos.setObjectName(u"tree_tabla_equipos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree_tabla_equipos.sizePolicy().hasHeightForWidth())
        self.tree_tabla_equipos.setSizePolicy(sizePolicy1)
        self.tree_tabla_equipos.setMinimumSize(QSize(400, 0))
        self.tree_tabla_equipos.setFrameShape(QFrame.Shape.StyledPanel)
        self.tree_tabla_equipos.setFrameShadow(QFrame.Shadow.Sunken)
        self.tree_tabla_equipos.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tree_tabla_equipos.setAlternatingRowColors(True)
        self.tree_tabla_equipos.setRootIsDecorated(False)
        self.tree_tabla_equipos.setUniformRowHeights(True)
        self.tree_tabla_equipos.setItemsExpandable(False)
        self.tree_tabla_equipos.setSortingEnabled(False)
        self.tree_tabla_equipos.setAnimated(False)
        self.tree_tabla_equipos.setHeaderHidden(False)
        self.tree_tabla_equipos.setExpandsOnDoubleClick(True)
        self.tree_tabla_equipos.header().setVisible(True)
        self.tree_tabla_equipos.header().setCascadingSectionResizes(False)
        self.tree_tabla_equipos.header().setHighlightSections(False)
        self.tree_tabla_equipos.header().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.tree_tabla_equipos)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 33))
        self.menu_Equipos = QMenu(self.menubar)
        self.menu_Equipos.setObjectName(u"menu_Equipos")
        self.menuExportar_Datos = QMenu(self.menubar)
        self.menuExportar_Datos.setObjectName(u"menuExportar_Datos")
        self.menu_Datos = QMenu(self.menubar)
        self.menu_Datos.setObjectName(u"menu_Datos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Datos.menuAction())
        self.menubar.addAction(self.menu_Equipos.menuAction())
        self.menubar.addAction(self.menuExportar_Datos.menuAction())
        self.menu_Equipos.addAction(self.actionDetalle_Equipos)
        self.menuExportar_Datos.addAction(self.actionEntradas)
        self.menuExportar_Datos.addAction(self.actionTaquillas)
        self.menuExportar_Datos.addAction(self.actionSalidas)
        self.menu_Datos.addAction(self.actionBuscar_Datos)

        self.retranslateUi(MainWindow)
        self.button_limpiarE.clicked.connect(self.text_console_entradas.clear)
        self.button_limpiarT.clicked.connect(self.text_console_taquillas.clear)
        self.button_limpiarS.clicked.connect(self.text_console_salidas.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SISTEMA DE SINCRONIZACION", None))
        self.actionEntradas.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.actionTaquillas.setText(QCoreApplication.translate("MainWindow", u"Taquillas", None))
        self.actionSalidas.setText(QCoreApplication.translate("MainWindow", u"Salidas", None))
        self.actionBuscar_Datos.setText(QCoreApplication.translate("MainWindow", u"Buscar Datos", None))
        self.actionDetalle_Equipos.setText(QCoreApplication.translate("MainWindow", u"Detalle Equipos", None))
        self.label_titulo_entradas.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.text_console_entradas.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_iniciarE.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.button_detenerE.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.button_limpiarE.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_titulo_taquillas.setText(QCoreApplication.translate("MainWindow", u"Taquillas", None))
        self.text_console_taquillas.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_iniciarT.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.button_detenerT.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.button_limpiarT.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_titulo_taquillas_2.setText(QCoreApplication.translate("MainWindow", u"Salidas", None))
        self.text_console_salidas.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_iniciarS.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.button_detenerS.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.button_limpiarS.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tabla de Equipos", None))
        ___qtreewidgetitem = self.tree_tabla_equipos.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Estatus", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Ip", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Ubicacion", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"ID", None));
        self.menu_Equipos.setTitle(QCoreApplication.translate("MainWindow", u"Equipos", None))
        self.menuExportar_Datos.setTitle(QCoreApplication.translate("MainWindow", u"Exportar Datos", None))
        self.menu_Datos.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
    # retranslateUi

