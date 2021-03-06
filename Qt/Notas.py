Validar entradas

exp_alpha_espacios = QtCore.QRegExp('[a-zA-Z\\s]]+')

exp_numerica = QtCore.QRegExp('[0-9]+')

exp_alphanumerica = QtCore.QRegExp('[a-zA-Z0-9]+')

validator = QtGui.QRegExpValidator(exp_<...>)

lineEdit.setValidator(validator)

----------------------------------------------------------

AutoCompletar Entradas

completer = QtGui.QCompleter(<lista_elementos>, <parent>)
# Ignorar mayusculas y minuscualas
completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
lineEdit.setCompleter(completer)

----------------------------------------------------------



TableView Models


#---- Creacion y configuracion del modelo para TableView

# Conexion a mongo
# Crear y asignar el modelo
self.modelo = Modelos.ModeloTablaArticulos(coleccion_mongo.find())
self.tableView.setModel(self.modelo)

# Configuracion para aceptar llamadas a un menu contextual
self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
self.tableView.customContextMenuRequested.connect(
	self.menu_contextual)

self.tableView.setSelectionBehavior(
	QtGui.QAbstractItemView.SelectRows)




# Configuracion manual del tamaño de los headers
header_view = self.tableView.horizontalHeader()
largo = header_view.length()
header_view.resizeSection(0, int(largo*0.20)*2)
header_view.resizeSection(1, int(largo*0.30)*2)
header_view.resizeSection(2, int(largo*0.08)*2)
header_view.resizeSection(3, int(largo*0.10)*2)
header_view.resizeSection(4, int(largo*0.06)*2)
header_view.resizeSection(5, int(largo*0.10)*2)
header_view.resizeSection(6, int(largo*0.03)*2 + 10)

#Configuracion automatica del tamaño de los headers
header_view = self.tableView.horizontalHeader()
#header_view.setResizeMode(QtGui.QHeaderView.ResizeToContents)
header_view.setResizeMode(QtGui.QHeaderView.Stretch)
#header_view.setStretchLastSection(True)


# Funciones para usar un menu contextual que elimina elementos
def menu_contextual(self, position):
	menu = QtGui.QMenu()
	eliminar_action = menu.addAction("Eliminar")

	action = menu.exec_(self.tableView.mapToGlobal(position))
	if action == eliminar_action:
		self.elimnar_menu_contextual()

def elimnar_menu_contextual(self):
	fila = self.tableView.currentIndex().row()

	# Logica para conectarse a mongoDB

	# Obteniendo el sku desde el modelo.
	index = self.modelo.index(fila , 0)
	sku = index.data()

	# Se manda hacer un
	# 'update', el campo modificado es el utilizado para marcar
	# elementos eliminados. Esto es la eliminacion logica.
	resultado_update = coleccion_mongo.update(
		{'de_codigoBarras':sku},
		{
			"$set":{
				'sn_eliminado': True
			}
		}
	)
	print(resultado_update) #-Debug
	#Actualizar tabla
	#Cerrar conexion

Definicion de un Modelo

class <Modelo>(QtCore.QAbstractTableModel):
"""Doc String de <Modelo>
"""
def __init__(self, <datos>):
super(<Modelo>, self).__init__()
self.filas = <datos>.count()
self.columnas = <columnas>
self.<datos> = self.crear_matriz(<datos>)
self.headers = [<headers>]
self.headers_enum = enum(<headers>)

def crear_matriz(self, posts):
	"""Toma el objeto Cursor que retorna el query al mongoDB, y crea
	una matriz con los datos, acelerando y aligerando el proceso de
	leer e imprimir los datos en la tabla.
	"""
	matriz = []
	for dic in posts:
		matriz.append([<Datos_coleccion>])
	return matriz
