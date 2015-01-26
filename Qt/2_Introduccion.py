"""
Documentacion del API
http://pyside.github.io/docs/pyside/

Un ejemplo mas avanzado de hola mundo

"""
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
"""
-- Widgets Interactivos

-- Botones

"""
QPushButton(parent=None)
QPushButton(text, [parent=None])
QPushButton(icon, text, [parent=None])
"""

Ejemplo de Botones
"""
go_button = QPushButton('Go', some_form)
"""

-- LineEdits

"""
QLineEdit(parent=None)
QLineEdit(text, [parent=None])
"""

-- ComboBoxes
"""
QComboBox(parent)

# Metodo para agregar items a los botones
addItem(icon, text, [userData=None])
addItem(text, [userData=None])
"""

-- Aplicacion de ejemplo, usando posicion absoluta

"""
from PySide.QtCore import *
from PySide.QtGui import *
qt_app = QApplication(sys.argv)

class AbsolutePositioningExample(QWidget):
    ''' An example of PySide absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''
    def __init__(self):
        # Initialize the object as a QWidget
        QWidget.__init__(self)

        # We have to set the size of the main window
        # ourselves, since we control the entire layout
        self.setMinimumSize(400, 185)
        self.setWindowTitle('Dynamic Greeter')

        # Create the controls with this object as their parent and set
        # their position individually; each row is a label followed by
        # another control

        # Label for the salutation chooser
        self.salutation_lbl = QLabel('Salutation:', self)
        self.salutation_lbl.move(5, 5) # offset the first control 5px
                                       # from top and left
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']
        # Create and fill the combo box to choose the salutation
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)

        # Allow 100px for the label and 5px each for borders at the
        # far left, between the label and the combobox, and at the far
        # right
        self.salutation.setMinimumWidth(285)
        # Place it five pixels to the right of the end of the label
        self.salutation.move(110, 5)

        # The label for the recipient control
        self.recipient_lbl = QLabel('Recipient:', self)
        # 5 pixel indent, 25 pixels lower than last pair of widgets
        self.recipient_lbl.move(5, 30)

        # The recipient control is an entry textbox
        self.recipient = QLineEdit(self)
        # Add some ghost text to indicate what sort of thing to enter
        self.recipient.setPlaceholderText(&quot;e.g. 'world' or 'Matey'&quot;)
        # Same width as the salutation
        self.recipient.setMinimumWidth(285)
        # Same indent as salutation but 25 pixels lower
        self.recipient.move(110, 30)

        # The label for the greeting widget
        self.greeting_lbl = QLabel('Greeting:', self)
        # Same indent as the others, but 45 pixels lower so it has
        # physical separation, indicating difference of function
        self.greeting_lbl.move(5, 75)

        # The greeting widget is also a label
        self.greeting = QLabel('', self)
        # Same indent as the other controls
        self.greeting.move(110, 75)

        # The build button is a push button
        self.build_button = QPushButton('&amp;Build Greeting', self)

        # Place it at the bottom right, narrower than
        # the other interactive widgets
        self.build_button.setMinimumWidth(145)
        self.build_button.move(250, 150)

    def run(self):
        # Show the form
        self.show()
        # Run the Qt application
        qt_app.exec_()

# Create an instance of the application window and run it
app = AbsolutePositioningExample()
app.run()
"""

-- Layouts

QHBoxLayout

QVBoxLayout

QGridLayout

QStackedLayout

QFormLayout

Mismo programa haciendo uso de layouts

"""
from PySide.QtCore import *
from PySide.QtGui import *
qt_app = QApplication(sys.argv)

class LayoutExample(QWidget):
    ''' An example of PySide/PyQt absolute positioning; the main window
        inherits from QWidget, a convenient widget for an empty window. '''

    def __init__(self):
        # Initialize the object as a QWidget and
        # set its title and minimum width
        QWidget.__init__(self)
        self.setWindowTitle('Dynamic Greeter')
        self.setMinimumWidth(400)

        # Create the QVBoxLayout that lays out the whole form
        self.layout = QVBoxLayout()

        # Create the form layout that manages the labeled controls
        self.form_layout = QFormLayout()

        # The salutations that we want to make available
        self.salutations = ['Ahoy',
                            'Good day',
                            'Hello',
                            'Heyo',
                            'Hi',
                            'Salutations',
                            'Wassup',
                            'Yo']

        # Create and fill the combo box to choose the salutation
        self.salutation = QComboBox(self)
        self.salutation.addItems(self.salutations)

        # Add it to the form layout with a label
        self.form_layout.addRow('&amp;Salutation:', self.salutation)

        # Create the entry control to specify a recipient
        # and set its placeholder text
        self.recipient = QLineEdit(self)
        self.recipient.setPlaceholderText(&quot;e.g. 'world' or 'Matey'&quot;)

        # Add it to the form layout with a label
        self.form_layout.addRow('&amp;Recipient:', self.recipient)

        # Create and add the label to show the greeting text
        self.greeting = QLabel('', self)
        self.form_layout.addRow('Greeting:', self.greeting)

        # Add the form layout to the main VBox layout
        self.layout.addLayout(self.form_layout)

        # Add stretch to separate the form layout from the button
        self.layout.addStretch(1)

        # Create a horizontal box layout to hold the button
        self.button_box = QHBoxLayout()

        # Add stretch to push the button to the far right
        self.button_box.addStretch(1)

        # Create the build button with its caption
        self.build_button = QPushButton('&amp;Build Greeting', self)

        # Add it to the button box
        self.button_box.addWidget(self.build_button)

        # Add the button box to the bottom of the main VBox layout
        self.layout.addLayout(self.button_box)

        # Set the VBox layout as the window's main layout
        self.setLayout(self.layout)

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()

# Create an instance of the application window and run it
app = LayoutExample()
app.run()
"""


"""