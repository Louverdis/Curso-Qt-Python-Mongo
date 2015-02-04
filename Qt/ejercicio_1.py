# -*- coding: UTF-8 -*-

'''
Creado el 31/01/2015

@autor: ----
'''
#===============================================================================
# Modulo ejercicio de formulario de articulos
#===============================================================================

from PySide import QtCore, QtGui
from pymongo import MongoClient

class Formulario(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Formulario, self).__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        #self.form = Form

        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.sku_lineEdit = QtGui.QLineEdit(Form)
        self.sku_lineEdit.setObjectName("sku_lineEdit")
        self.gridLayout.addWidget(self.sku_lineEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.descripcion_lineEdit = QtGui.QLineEdit(Form)
        self.descripcion_lineEdit.setObjectName("descripcion_lineEdit")
        self.gridLayout.addWidget(self.descripcion_lineEdit, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.precio_doubleSpinBox = QtGui.QDoubleSpinBox(Form)
        self.precio_doubleSpinBox.setMaximum(99999.99)
        self.precio_doubleSpinBox.setSingleStep(5.0)
        self.precio_doubleSpinBox.setObjectName("precio_doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.precio_doubleSpinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cantidad_spinBox = QtGui.QSpinBox(Form)
        self.cantidad_spinBox.setPrefix("")
        self.cantidad_spinBox.setObjectName("cantidad_spinBox")
        self.horizontalLayout_3.addWidget(self.cantidad_spinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.borrar_pushButton = QtGui.QPushButton(Form)
        self.borrar_pushButton.setObjectName("borrar_pushButton")
        self.horizontalLayout.addWidget(self.borrar_pushButton)

        self.aceptar_pushButton = QtGui.QPushButton(Form)
        self.aceptar_pushButton.setObjectName("aceptar_pushButton")
        self.horizontalLayout.addWidget(self.aceptar_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.borrar_pushButton.clicked.connect(self.on_click)
        self.aceptar_pushButton.clicked.connect(self.guardar_documento)

        lista_desc = self.crear_lista()
        desc_completer = QtGui.QCompleter(lista_desc, Form)
        desc_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.descripcion_lineEdit.setCompleter(desc_completer)
        #self.actualiazar_lista()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Nuevo Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nuevo Formulario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "SKU:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.precio_doubleSpinBox.setPrefix(QtGui.QApplication.translate("Form", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.cantidad_spinBox.setSuffix(QtGui.QApplication.translate("Form", " unidades", None, QtGui.QApplication.UnicodeUTF8))
        self.borrar_pushButton.setText(QtGui.QApplication.translate("Form", "&Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar_pushButton.setText(QtGui.QApplication.translate("Form", "&Guardar", None, QtGui.QApplication.UnicodeUTF8))

    #@QtCore.SLOT <-- Ayuda para los debugs
    def on_click(self):
        dialogo = BorrarDialogo()
        if dialogo.exec_() == dialogo.Accepted:
            self.borrar_datos()

    def borrar_datos(self):
        self.sku_lineEdit.setText('')
        self.descripcion_lineEdit.setText('')
        self.precio_doubleSpinBox.setValue(0.0)
        self.cantidad_spinBox.setValue(0)

    def guardar_documento(self):
        sku = self.sku_lineEdit.text()
        desc = self.descripcion_lineEdit.text()
        precio = self.precio_doubleSpinBox.value()
        cantidad = self.cantidad_spinBox.value()

        documento = {
            "codigo": sku,
            "descripcion": desc,
            "precio": precio,
            "cantidad": cantidad
        }

        client = MongoClient()
        db = client.mydb
        coleccion = db.articulos

        r = coleccion.insert(documento)
        print("Se inserto el documento: "+str(r)) # Debug

        client.close()
        self.borrar_datos()
        self.actualizar_lista()

    def crear_lista(self):
        client = MongoClient()
        db = client.mydb
        coleccion = db.articulos

        articulos = coleccion.find()

        lista = [doc["descripcion"] for doc in articulos]

        client.close()
        return lista

    def actualizar_lista(self):
        lista_desc = self.crear_lista()
        desc_completer = QtGui.QCompleter(lista_desc, self)
        desc_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.descripcion_lineEdit.setCompleter(desc_completer)

class BorrarDialogo(QtGui.QDialog):
    def __init__(self, parent=None):
        super(BorrarDialogo, self).__init__()
        self.setupUi(self)
        self.nombre_dialogo = "Conocido"

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 98)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.si_pushButton = QtGui.QPushButton(Dialog)
        self.si_pushButton.setObjectName("si_pushButton")
        self.horizontalLayout.addWidget(self.si_pushButton)
        self.no_pushButton = QtGui.QPushButton(Dialog)
        self.no_pushButton.setObjectName("no_pushButton")
        self.horizontalLayout.addWidget(self.no_pushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QtCore.QObject.connect(
            self.si_pushButton,
            QtCore.SIGNAL("clicked()"),
            Dialog.accept
        )
        QtCore.QObject.connect(
            self.no_pushButton,
            QtCore.SIGNAL("clicked()"),
            Dialog.reject
        )

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.si_pushButton, self.no_pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Eliminar datos", None, QtGui.QApplication.UnicodeUTF8))
        self.si_pushButton.setText(QtGui.QApplication.translate("Dialog", "Si", None, QtGui.QApplication.UnicodeUTF8))
        self.no_pushButton.setText(QtGui.QApplication.translate("Dialog", "No", None, QtGui.QApplication.UnicodeUTF8))

class ListadoArticulos(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ListadoArticulos, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 312)

        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.nuevo_pushButton = QtGui.QPushButton(Form)
        self.nuevo_pushButton.setObjectName("nuevo_pushButton")
        self.horizontalLayout.addWidget(self.nuevo_pushButton)

        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QtGui.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        client = MongoClient()
        coleccion = client.mydb.articulos
        self.modelo = ModeloArticulos(coleccion.find())
        self.tableView.setModel(self.modelo)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Listado de Articulos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Listado de Articulos", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevo_pushButton.setText(QtGui.QApplication.translate("Form", "Nuevo Articulo", None, QtGui.QApplication.UnicodeUTF8))

class ModeloArticulos(QtCore.QAbstractTableModel):
    """docstring for ModeloArticulos"""

    def __init__(self, cursor):
        super(ModeloArticulos, self).__init__()
        self.cursor = cursor
        self.filas = cursor.count()
        self.columnas = 4
        self.headers = ["SKU", "Descripcion", "Precio", "Cantidad"]

        self.matriz = self.crear_matriz()

    def crear_matriz(self):
        matriz = []
        for doc in self.cursor:
            matriz.append([
                doc["codigo"],
                doc["descripcion"],
                doc["precio"],
                doc["cantidad"]
            ])
        return matriz

    # Overrride de metodos virtuales
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """
        Override de headerData(), imprime los headers horizontales y
        verticales de la tabla.
        """
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Vertical:
                #return ">"
                return ">> "+str(section+1)
            else:
                return self.headers[section]
        else:
            return QtCore.QAbstractTableModel.headerData(
                        self,
                        section,
                        orientation,
                        role
                    )

    def rowCount(self, parent=QtCore.QModelIndex()):
        """
        Override de rowCount(), retorna el numero de filas.
        """
        return self.filas

    def columnCount(self, parent=QtCore.QModelIndex()):
        """
        Override de columnCount(), retorna el numero de columnas.
        """
        return self.columnas

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """Override de data(), a partir del indice, toma la Informacion
        correspondiente a la celda de la tabla.
        Es la funcion usada para poblar la tabla.
        """

        # Procesado del DisplayRole:
        #   Usado para definir el texto a desplegar dentro de las
        #   celdas.
        if role == QtCore.Qt.DisplayRole:
            fila = self.matriz[index.row()]

            if index.column() == 2:
                return "${0:.2f}".format(float(fila[index.column()]))

            if index.column() == 3:
                return str(fila[index.column()])

            else:
                return fila[index.column()]

        # Se retorna como default un None al resto de los roles sin definir
        else:
            return None

if __name__ == '__main__':
    app = QtGui.QApplication([])

    listado = ListadoArticulos()
    listado.show()

    app.exec_()


