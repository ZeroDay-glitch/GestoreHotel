from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QListWidget, QSpacerItem, QLabel


class VistaGestioneAddettoServizi(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneAddettoServizi, self).__init__(parent)
        layout = QVBoxLayout()

        # Pulsanti per gestire i addetto_servizi
        layout.addWidget(self.get_generic_button("AGGIUNGI", self.aggiungi_addetto_servizi, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.get_generic_button("APRI", self.apri_addetto_servizi, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_addetto_servizi, 12))
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Addetti ai Servizi")
        layout.addWidget(label)

        # Lista dei addetto_servizi
        self.lista_addetto_servizi = QListWidget()
        layout.addWidget(self.lista_addetto_servizi)

        # Spazio vuoto per distanziare
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(layout)
        self.setWindowTitle("Gestione Addetti ai Servizi")
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

    def aggiungi_addetto_servizi(self):
        # Funzione da implementare per aggiungere un nuovo addetto_servizi alla lista
        pass

    def apri_addetto_servizi(self):
        # Funzione da implementare per aprire il addetto_servizi selezionato
        pass

    def rimuovi_addetto_servizi(self):
        # Funzione da implementare per rimuovere il addetto_servizi selezionato
        pass
