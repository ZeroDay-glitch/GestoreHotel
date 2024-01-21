from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestioneCamere import VistaGestioneCamere
from Viste.VistaGestioneClienti import VistaGestioneClienti
from Viste.VistaGestioneDipendenti import VistaGestioneDipendenti
from Viste.VistaGestionePrenotazione import VistaGestionePrenotazione


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("SERVIZI", self.go_servizi, 160, 60, 12), 1, 0)
        grid_layout.addWidget(self.get_generic_button("PRENOTAZIONI", self.go_prenotazioni, 160, 60,12), 1, 1)
        grid_layout.addWidget(self.get_generic_button("DIPENDENTI", self.go_dipendenti, 160, 60,12), 0, 0)
        grid_layout.addWidget(self.get_generic_button("CLIENTI", self.go_clienti, 160, 60, 12), 0, 1)
        grid_layout.addWidget(self.get_generic_button("SISTEMA", self.go_sistema, 160, 60,12), 2, 0)
        grid_layout.addWidget(self.get_generic_button("CAMERE", self.go_camere, 160, 60,12), 2, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Hotel BETA")
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

    def go_servizi(self):
        pass

    def go_prenotazioni(self):
        self.vista_gestione_prenotazione = VistaGestionePrenotazione()
        self.vista_gestione_prenotazione.show()

    def go_clienti(self):
        self.vista_clienti = VistaGestioneClienti()
        self.vista_clienti.show()

    def go_dipendenti(self):
        self.vista_dipendenti = VistaGestioneDipendenti()
        self.vista_dipendenti.show()

    def go_sistema(self):
        pass

    def go_camere(self):
        self.vista_gestione_camere = VistaGestioneCamere()
        self.vista_gestione_camere.show()
