# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscar_datoSNmnaZ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Buscar_dato(object):
    def setupUi(self, Buscar_dato):
        if not Buscar_dato.objectName():
            Buscar_dato.setObjectName(u"Buscar_dato")
        Buscar_dato.resize(562, 439)
        self.verticalLayout = QVBoxLayout(Buscar_dato)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.titulo_dato = QLabel(Buscar_dato)
        self.titulo_dato.setObjectName(u"titulo_dato")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo_dato.sizePolicy().hasHeightForWidth())
        self.titulo_dato.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titulo_dato.setFont(font)

        self.horizontalLayout_3.addWidget(self.titulo_dato)

        self.titulo_tabla = QLabel(Buscar_dato)
        self.titulo_tabla.setObjectName(u"titulo_tabla")
        self.titulo_tabla.setMinimumSize(QSize(150, 0))
        self.titulo_tabla.setFont(font)

        self.horizontalLayout_3.addWidget(self.titulo_tabla)

        self.titulo_columna = QLabel(Buscar_dato)
        self.titulo_columna.setObjectName(u"titulo_columna")
        self.titulo_columna.setMinimumSize(QSize(150, 0))
        self.titulo_columna.setFont(font)

        self.horizontalLayout_3.addWidget(self.titulo_columna)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.linea_buscar = QLineEdit(Buscar_dato)
        self.linea_buscar.setObjectName(u"linea_buscar")
        self.linea_buscar.setMinimumSize(QSize(0, 30))
        self.linea_buscar.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.linea_buscar)

        self.combob_tabla = QComboBox(Buscar_dato)
        self.combob_tabla.setObjectName(u"combob_tabla")
        self.combob_tabla.setMinimumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.combob_tabla)

        self.combob_columna = QComboBox(Buscar_dato)
        self.combob_columna.setObjectName(u"combob_columna")
        self.combob_columna.setEnabled(False)
        self.combob_columna.setMinimumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.combob_columna)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tree_tabla_busqueda = QTreeWidget(Buscar_dato)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"datos");
        self.tree_tabla_busqueda.setHeaderItem(__qtreewidgetitem)
        self.tree_tabla_busqueda.setObjectName(u"tree_tabla_busqueda")

        self.verticalLayout.addWidget(self.tree_tabla_busqueda)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_Buscar = QPushButton(Buscar_dato)
        self.button_Buscar.setObjectName(u"button_Buscar")
        font1 = QFont()
        font1.setPointSize(11)
        self.button_Buscar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_Buscar)

        self.button_Limpiar = QPushButton(Buscar_dato)
        self.button_Limpiar.setObjectName(u"button_Limpiar")
        self.button_Limpiar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_Limpiar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Buscar_dato)
        self.linea_buscar.returnPressed.connect(self.button_Buscar.click)

        self.combob_tabla.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Buscar_dato)
    # setupUi

    def retranslateUi(self, Buscar_dato):
        Buscar_dato.setWindowTitle(QCoreApplication.translate("Buscar_dato", u"Buscar Datos", None))
        self.titulo_dato.setText(QCoreApplication.translate("Buscar_dato", u"Valor a Buscar", None))
        self.titulo_tabla.setText(QCoreApplication.translate("Buscar_dato", u"Tabla", None))
        self.titulo_columna.setText(QCoreApplication.translate("Buscar_dato", u"Columna", None))
        self.linea_buscar.setPlaceholderText(QCoreApplication.translate("Buscar_dato", u"Indique el dato a rastrear...", None))
        self.button_Buscar.setText(QCoreApplication.translate("Buscar_dato", u"Buscar", None))
        self.button_Limpiar.setText(QCoreApplication.translate("Buscar_dato", u"Limpiar", None))
    # retranslateUi

