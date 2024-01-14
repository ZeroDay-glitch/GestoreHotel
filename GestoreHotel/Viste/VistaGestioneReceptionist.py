import os
import pickle

from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QListWidget, QSpacerItem, QLabel, QListView, \
    QMessageBox

from Viste.VistaAggiungiReceptionist import VistaAggiungiReceptionist
from Viste.VistaReceptionist import VistaReceptionist


class VistaGestioneReceptionist(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneReceptionist, self).__init__(parent)
        self.layout = QVBoxLayout()

        # Pulsanti per gestire i receptionist
        self.layout.addWidget(self.get_generic_button("AGGIUNGI", lambda: self.aggiungi_receptionist(self.update_ui), 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_receptionist, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_receptionist, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Receptionists")
        self.layout.addWidget(label)

        # Lista dei receptionist
        self.lista_receptionist = QListView()
        self.layout.addWidget(self.lista_receptionist)
        self.update_ui()

        # Spazio vuoto per distanziare
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Receptionist")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgreen;")


    def load_receptionists(self):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.receptionists.extend(current.values())

    def update_ui(self):
        # Carica l'elenco dei receptionist e aggiorna la lista
        self.receptionists = [] # Carica qui i dati dei receptionist
        self.load_receptionists()
        listview_model = QStandardItemModel(self.lista_receptionist)
        for receptionist in self.receptionists:
            item = QStandardItem()
            # Modifica questa riga per visualizzare i dettagli del receptionist
            item.setText(f"{receptionist.nome} {receptionist.cognome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            listview_model.appendRow(item)
        self.lista_receptionist.setModel(listview_model)

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

    def aggiungi_receptionist(self, callback=None):
        self.vista_aggiungi_receptionist = VistaAggiungiReceptionist(callback=self.update_ui )
        self.vista_aggiungi_receptionist.show()

    def apri_receptionist(self):
        try:
            selected_index = self.lista_receptionist.selectedIndexes()[0]
            if selected_index.isValid():
                # Ottieni il receptionist selezionato dalla lista
                selected_receptionist = self.receptionists[selected_index.row()]

                # Chiamata alla VistaReceptionist per visualizzare le informazioni del receptionist
                self.vista_receptionist = VistaReceptionist(selected_receptionist)
                self.vista_receptionist.show()
        except IndexError:
            print("INDEX ERROR")

    def rimuovi_receptionist(self):
        # Ottieni l'indice dell'elemento selezionato nella lista dei receptionist
        selected_index = self.lista_receptionist.selectedIndexes()[0]

        if selected_index.isValid():
            # Identifica il receptionist corrispondente all'elemento selezionato
            selected_receptionist = self.receptionists[selected_index.row()]

            # Rimuovi il receptionist dai dati su disco
            if selected_receptionist:
                if selected_receptionist.rimuovi_dipendente():
                    # Rimozione riuscita, aggiorna l'interfaccia utente
                    self.update_ui()
                else:
                    # Rimozione fallita, mostra un messaggio di errore
                    QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere il receptionist.', QMessageBox.Ok,
                                         QMessageBox.Ok)
