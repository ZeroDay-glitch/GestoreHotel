import os
import pickle

from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QListView, QSpacerItem, QLabel, QMessageBox

from Viste.VistaAddettoServizi import VistaAddettoServizi
from Viste.VistaAggiungiAddettoServizi import VistaAggiungiAddettoServizi


class VistaGestioneAddettoServizi(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneAddettoServizi, self).__init__(parent)
        self.layout = QVBoxLayout()

        # Pulsanti per gestire i addetto_servizi
        self.layout.addWidget(self.get_generic_button("AGGIUNGI", self.aggiungi_addetto_servizi, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_addetto_servizi, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_addetto_servizi, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Addetti ai Servizi")
        self.layout.addWidget(label)

        # Lista dei addetto_servizi
        self.lista_addetto_servizi = QListView()
        self.layout.addWidget(self.lista_addetto_servizi)
        self.update_ui()

        # Spazio vuoto per distanziare
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
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


    def update_ui(self):
        self.addetti_servizi = []
        self.load_addetti_servizi()
        listview_model = QStandardItemModel(self.lista_addetto_servizi)
        for addetto_servizi in self.addetti_servizi:
            item = QStandardItem()
            item.setText(f"{addetto_servizi.nome} {addetto_servizi.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            listview_model.appendRow(item)
        self.lista_addetto_servizi.setModel(listview_model)

    def load_addetti_servizi(self):
        if os.path.isfile('Dati/AddettoServizi.pickle'):
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.addetti_servizi.extend(current.values())

    def aggiungi_addetto_servizi(self, callback=None):
        self.vista_aggiungi_addetto_servizi = VistaAggiungiAddettoServizi(callback=self.update_ui)
        self.vista_aggiungi_addetto_servizi.show()

    def apri_addetto_servizi(self):
        try:
            selected_index = self.lista_addetto_servizi.selectedIndexes()[0]
            if selected_index.isValid():
                # Ottieni il receptionist selezionato dalla lista
                selected_addetto_servizi = self.addetti_servizi[selected_index.row()]

                # Chiamata alla VistaReceptionist per visualizzare le informazioni del receptionist
                self.vista_addetto_servizi = VistaAddettoServizi(selected_addetto_servizi)
                self.vista_addetto_servizi.show()
        except IndexError:
            print("INDEX ERROR")

    def rimuovi_addetto_servizi(self):
        selected_index = self.lista_addetto_servizi.selectedIndexes()[0]

        if selected_index.isValid():
            selected_addetto_servizi = self.addetti_servizi[selected_index.row()]

            if selected_addetto_servizi:
                if selected_addetto_servizi.rimuovi_dipendente():
                    self.update_ui()
                else:
                    QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere l\' addetto ai servizi.', QMessageBox.Ok,
                                         QMessageBox.Ok)
