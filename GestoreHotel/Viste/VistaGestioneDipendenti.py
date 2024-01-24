from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from Viste.VistaGestioneAddettoServizi import VistaGestioneAddettoServizi
from Viste.VistaGestioneReceptionist import VistaGestioneReceptionist


class VistaGestioneDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneDipendenti, self).__init__(parent)
        layout = QVBoxLayout()

        # Pulsanti per gestire i dipendenti
        layout.addWidget(self.get_generic_button("RECEPTIONIST", self.seleziona_receptionist, 12))
        layout.addWidget(self.get_generic_button("ADDETTO a SERVIZI", self.seleziona_addetto_servizi, 12))

        # Pulsante "Annulla" per tornare indietro
        layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(layout)
        self.setWindowTitle("Gestione Dipendenti")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgreen;")

    def get_generic_button(self, titolo, on_click, font_size=None):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)

        if font_size is not None:
            font = QFont()
            font.setPointSize(font_size)
            button.setFont(font)

        button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 10px; /* Arrotonda gli angoli a 10px */
            }
            QPushButton:hover {
                background-color: darkgreen;
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
