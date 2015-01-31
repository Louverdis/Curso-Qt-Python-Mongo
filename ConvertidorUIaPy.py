'''
Created on 09/04/2014

@author: Luis Mario Reyes Moreno
'''
from subprocess import call
from PySide.QtGui import (  QApplication, QMainWindow, QWidget,
                            QFileDialog, QLabel, QPushButton,
                            QVBoxLayout, QGridLayout, QLineEdit,
                            QSpacerItem, QHBoxLayout, QSizePolicy
                          )

from PySide.QtCore import QMetaObject

import sys
import platform

Ruta_archivoUI = ''
Ruta_archivoPY = ''

#===============================================================================
# Clase generada automaticamente por medio de Pyside-uic
#===============================================================================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 96)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.UI_label = QLabel(self.centralwidget)
        self.UI_label.setObjectName("UI_label")
        self.gridLayout.addWidget(self.UI_label, 0, 0, 1, 1)

        self.seleccionarUI_pushButton = QPushButton(self.centralwidget)
        self.seleccionarUI_pushButton.setObjectName("seleccionarUI_pushButton")
        self.gridLayout.addWidget(self.seleccionarUI_pushButton, 0, 2, 1, 1)

        self.Py_label = QLabel(self.centralwidget)
        self.Py_label.setObjectName("Py_label")
        self.gridLayout.addWidget(self.Py_label, 1, 0, 1, 1)

        self.rutaSalida_pushButton = QPushButton(self.centralwidget)
        self.rutaSalida_pushButton.setObjectName("rutaSalida_pushButton")
        self.gridLayout.addWidget(self.rutaSalida_pushButton, 1, 2, 1, 1)

        self.rutaEntrada_lineEdit = QLineEdit(self.centralwidget)
        self.rutaEntrada_lineEdit.setEnabled(False)
        self.rutaEntrada_lineEdit.setObjectName("rutaEntrada_lineEdit")
        self.gridLayout.addWidget(self.rutaEntrada_lineEdit, 0, 1, 1, 1)

        self.rutaSalida_lineEdit = QLineEdit(self.centralwidget)
        self.rutaSalida_lineEdit.setObjectName("rutaSalida_lineEdit")
        self.gridLayout.addWidget(self.rutaSalida_lineEdit, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")

        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                    QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.convertir_pushButton = QPushButton(self.horizontalWidget)
        self.convertir_pushButton.setObjectName("convertir_pushButton")
        self.horizontalLayout.addWidget(self.convertir_pushButton)

        self.verticalLayout.addWidget(self.horizontalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QApplication.translate(
                "MainWindow",
                "Convertidor UI a Py",
                None,
                QApplication.UnicodeUTF8
                )
            )
        self.UI_label.setText(
            QApplication.translate(
                "MainWindow",
                "Seleccionar UI:",
                None,
                QApplication.UnicodeUTF8
                )
            )
        self.seleccionarUI_pushButton.setText(
            QApplication.translate(
                "MainWindow",
                "Abrir...",
                None,
                QApplication.UnicodeUTF8
                )
            )
        self.Py_label.setText(
            QApplication.translate(
                "MainWindow",
                "Archivo Py:",
                None,
                QApplication.UnicodeUTF8
                )
            )
        self.rutaSalida_pushButton.setText(
            QApplication.translate(
                "MainWindow",
                "...",
                None,
                QApplication.UnicodeUTF8
                )
            )
        self.convertir_pushButton.setText(
            QApplication.translate(
                "MainWindow",
                "Convertir",
                None,
                QApplication.UnicodeUTF8
                )
            )

        #Codigo agregado para ensamblar el GUI con el programa actual
        self.seleccionarUI_pushButton.clicked.connect(self.seleccionarUI)
        self.rutaSalida_pushButton.clicked.connect(self.seleccionarPY)
        self.convertir_pushButton.clicked.connect(convertir)


    #Funciones anexadas para la funcionalidad de los botones
    def seleccionarUI(self):
        dialogo = QFileDialog(None)
        dialogo.setFileMode(QFileDialog.ExistingFile)
        dialogo.setNameFilter('Interfaz(*.ui)')

        if dialogo.exec_():
            global Ruta_archivoUI
            Ruta_archivoUI = dialogo.selectedFiles()[0]
            self.rutaEntrada_lineEdit.setText(Ruta_archivoUI)

    def seleccionarPY(self):
        dialogo = QFileDialog(None)
        dialogo.setFileMode(QFileDialog.AnyFile)
        dialogo.setNameFilter('Archivo Python(*.py)')
        dialogo.setAcceptMode(QFileDialog.AcceptSave)
        dialogo.setDefaultSuffix('py')

        if dialogo.exec_():
            global Ruta_archivoPY
            Ruta_archivoPY = dialogo.selectedFiles()[0]
            self.rutaSalida_lineEdit.setText(Ruta_archivoPY)

#===============================================================================
# Clase para controlar e instanciar la ventana principal
# generada por Pyside-uic
#===============================================================================
class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#===============================================================================
# Grupo de funciones que realizan la conversion de .UI a .py
# mediente Pyside-uic
#===============================================================================
def convertir():
    if platform.system() == 'Windows':
        conversion_windows()
    conversion_linux()

def conversion_windows():
    cmd = 'C:/Python34/Scripts/pyside-uic.exe '+Ruta_archivoUI+' -o '+Ruta_archivoPY
    stout = call(cmd, shell = True)
    if stout == 0:
        print("Conversion completada con exito")

def conversion_linux():
    cmd = 'pyside-uic '+Ruta_archivoUI+' -o '+Ruta_archivoPY
    stout = call(cmd, shell=True)
    if stout == 0:
        print("Conversion completada con exito")
        ## Codigo para debian, donde UIC solo genera codigo de python 2.7
        # print("Transformando a Python3")
        # call('2to3 -w '+Ruta_archivoPY, shell=True)

if __name__ == '__main__':
    app = QApplication([])
    controlMW = ControlMainWindow()
    controlMW.show()
    app.exec_()
