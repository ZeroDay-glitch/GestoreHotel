from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from Viste.VistaGestioneAddettoServizi import VistaGestioneAddettoServizi
from Viste.VistaGestioneReceptionist import VistaGestioneReceptionist


class VistaGestioneDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)
        layout = QVBoxLayout()

        layout.addWidget(self.get_generic_button("RECEPTIONIST", self.seleziona_receptionist, 200, 60, 12))
        layout.addSpacing(10)
        layout.addWidget(self.get_generic_button("ADDETTO a SERVIZI", self.seleziona_addetto_servizi, 200, 60,12))
        layout.addSpacing(20)
        layout.addWidget(self.get_generic_button("Annulla", self.close, 200, 60,12))

        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle("Gestione Dipendenti")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #393535;")

    def get_generic_button(self, titolo, on_click, width=None, height=None, font_size=None):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)

        if width is not None and height is not None:
            button.setFixedSize(width, height)

        if font_size is not None:
            font = QFont()
            font.setPointSize(font_size)
            button.setFont(font)

        button.setStyleSheet("""
            QPushButton {
                background-color: #C3D4C7;
                color: black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #707070;
                color: white;
            }
        """)

        return button

    def seleziona_receptionist(self):
        self.vista_receptionist = VistaGestioneReceptionist()
        self.vista_receptionist.show()

    def seleziona_addetto_servizi(self):
        self.vista_addetto_servizi = VistaGestioneAddettoServizi()
        self.vista_addetto_servizi.show()
