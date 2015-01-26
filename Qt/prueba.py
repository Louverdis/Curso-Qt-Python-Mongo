import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Se crea el objeto application
qt_app = QApplication(sys.argv)

class HelloWorldApp(QLabel):
    ''' A Qt application that displays the text, "Hello, world!" '''
    def __init__(self):
        # Se inicializa la clase padre
        QLabel.__init__(self, "Hola mundo!")

        # Se configura el tamaño, alineacion y titulo
        self.setMinimumSize(QSize(600, 400))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('Hello, world!')

    def run(self):
        ''' Show the application window and start the main event loop '''
        self.show()
        qt_app.exec_()

# Finalmente se crea una instancia de la aplicacion y se ejecuta
HelloWorldApp().run()