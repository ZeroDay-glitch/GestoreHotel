import os
import pickle

from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QListView, QMessageBox

from Viste.VistaAggiungiCliente import VistaAggiungiCliente
from Viste.VistaCliente import VistaCliente


class VistaGestioneClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneClienti, self).__init__(parent)
        self.layout = QVBoxLayout()

        # Pulsanti per gestire i clienti
        self.layout.addWidget(self.get_generic_button("AGGIUNGI", lambda: self.aggiungi_cliente(self.update_ui), 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_cliente, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_cliente, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Clienti")
        self.layout.addWidget(label)

        # Lista dei clienti
        self.lista_cliente = QListView()
        self.layout.addWidget(self.lista_cliente)
        self.update_ui()

        # Spazio vuoto per distanziare
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Clienti")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgreen;")

    def load_clienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.clienti.extend(current.values())

    def update_ui(self):
        # Carica l'elenco dei clienti e aggiorna la lista
        self.clienti = []  # Carica qui i dati dei clienti
        self.load_clienti()
        listview_model = QStandardItemModel(self.lista_cliente)
        for cliente in self.clienti:
            item = QStandardItem()
            # Modifica questa riga per visualizzare i dettagli del cliente
            item.setText(f"{cliente.nome} {cliente.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            listview_model.appendRow(item)
        self.lista_cliente.setModel(listview_model)

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

    def aggiungi_cliente(self, callback=None):
        self.vista_aggiungi_cliente = VistaAggiungiCliente(callback=self.update_ui)
        self.vista_aggiungi_cliente.show()

    def apri_cliente(self):
        try:
            selected_index = self.lista_cliente.selectedIndexes()[0]
            if selected_index.isValid():
                selected_cliente = self.clienti[selected_index.row()]
                self.vista_apri_cliente = VistaCliente(selected_cliente, modifica_callback=self.update_ui)
                self.vista_apri_cliente.show()
        except IndexError:
            print("INDEX ERROR")

    def rimuovi_cliente(self):
        # Ottieni l'indice dell'elemento selezionato nella lista dei clienti
        selected_index = self.lista_cliente.selectedIndexes()[0]

        if selected_index.isValid():
            # Identifica il cliente corrispondente all'elemento selezionato
            selected_cliente = self.clienti[selected_index.row()]

            # Rimuovi il cliente dai dati su disco
            if selected_cliente:
                if selected_cliente.rimuovi_cliente():
                    # Rimozione riuscita, aggiorna l'interfaccia utente
                    self.update_ui()
                else:
                    # Rimozione fallita, mostra un messaggio di errore
                    QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere il cliente.', QMessageBox.Ok,
                                         QMessageBox.Ok)
