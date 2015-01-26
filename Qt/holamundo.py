# import sys

# import PySide
# from PySide.QtGui import QApplication
# from PySide.QtGui import QMessageBox

# app = QApplication(sys.argv)

# msgBox = QMessageBox()
# msgBox.setText("Hola mundo! - Version de PySide: " + PySide.__version__)
# msgBox.exec_()

#--------------------------------------------------------------------------

import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

#label = QLabel("Hola mundo!")
label = QLabel("<font color=red size=40>Hola mundo!</font>")
label.show()

sys.exit(app.exec_())