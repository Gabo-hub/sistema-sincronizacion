# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipos_detallesSfHRLk.ui'
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
    QLabel, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Equipos_Detalles(object):
    def setupUi(self, Equipos_Detalles):
        if not Equipos_Detalles.objectName():
            Equipos_Detalles.setObjectName(u"Equipos_Detalles")
        Equipos_Detalles.resize(770, 526)
        self.verticalLayout_2 = QVBoxLayout(Equipos_Detalles)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo_equipos = QLabel(Equipos_Detalles)
        self.titulo_equipos.setObjectName(u"titulo_equipos")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titulo_equipos.setFont(font)

        self.verticalLayout.addWidget(self.titulo_equipos)

        self.combo_equipos = QComboBox(Equipos_Detalles)
        self.combo_equipos.setObjectName(u"combo_equipos")

        self.verticalLayout.addWidget(self.combo_equipos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Equipos_Detalles)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.tree_info_equipo = QTreeWidget(Equipos_Detalles)
        self.tree_info_equipo.setObjectName(u"tree_info_equipo")

        self.verticalLayout_3.addWidget(self.tree_info_equipo)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Equipos_Detalles)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.tree_info_datos = QTreeWidget(Equipos_Detalles)
        self.tree_info_datos.setObjectName(u"tree_info_datos")

        self.verticalLayout_4.addWidget(self.tree_info_datos)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Equipos_Detalles)

        QMetaObject.connectSlotsByName(Equipos_Detalles)
    # setupUi

    def retranslateUi(self, Equipos_Detalles):
        Equipos_Detalles.setWindowTitle(QCoreApplication.translate("Equipos_Detalles", u"Detalle Equipos", None))
        self.titulo_equipos.setText(QCoreApplication.translate("Equipos_Detalles", u"Equipos", None))
        self.label_2.setText(QCoreApplication.translate("Equipos_Detalles", u"Informacion del Equipo", None))
        ___qtreewidgetitem = self.tree_info_equipo.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Equipos_Detalles", u"equipos", None));
        self.label_3.setText(QCoreApplication.translate("Equipos_Detalles", u"Datos Tratados", None))
        ___qtreewidgetitem1 = self.tree_info_datos.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Equipos_Detalles", u"datos", None));
    # retranslateUi

