from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QListWidget, QSpacerItem, QLabel

class VistaGestioneReceptionist(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneReceptionist, self).__init__(parent)
        layout = QVBoxLayout()

        # Pulsanti per gestire i receptionist
        layout.addWidget(self.get_generic_button("AGGIUNGI", self.aggiungi_receptionist, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.get_generic_button("APRI", self.apri_receptionist, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_receptionist, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Receptionist")
        layout.addWidget(label)

        # Lista dei receptionist
        self.lista_receptionist = QListWidget()
        layout.addWidget(self.lista_receptionist)

        # Spazio vuoto per distanziare
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(layout)
        self.setWindowTitle("Gestione Receptionist")
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
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkgreen;
                color: white;
            }
        """)

        return button

    def aggiungi_receptionist(self):
        # Funzione da implementare per aggiungere un nuovo receptionist alla lista
        pass

    def apri_receptionist(self):
        # Funzione da implementare per aprire il receptionist selezionato
        pass

    def rimuovi_receptionist(self):
        # Funzione da implementare per rimuovere il receptionist selezionato
        pass
