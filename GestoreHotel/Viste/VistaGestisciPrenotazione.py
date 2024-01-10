import os
import pickle

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListView, QPushButton, QLabel

from Viste.VistaPrenotazione import VistaPrenotazione


class VistaGestisciPrenotazione(QWidget):
    def __init__(self, parent=None):
        super(VistaGestisciPrenotazione, self).__init__(parent)
        self.setWindowTitle("Gestisci Prenotazioni")

        main_layout = QVBoxLayout()

        # Aggiungi un titolo per la lista dei clienti senza prenotazioni
        senza_prenotazione_label = QLabel("Senza Prenotazione")
        main_layout.addWidget(senza_prenotazione_label)

        # Elenco dei clienti senza prenotazioni
        self.clienti_senza_prenotazioni_view = QListView()
        main_layout.addWidget(self.clienti_senza_prenotazioni_view)

        # Aggiungi un titolo per la lista dei clienti con prenotazioni
        con_prenotazione_label = QLabel("Con Prenotazione")
        main_layout.addWidget(con_prenotazione_label)

        # Elenco dei clienti con prenotazioni
        self.clienti_con_prenotazioni_view = QListView()
        main_layout.addWidget(self.clienti_con_prenotazioni_view)

        # Pulsante "Apri" sulla destra
        button_layout = QVBoxLayout()
        open_button = QPushButton("Aggiungi Prenotazione")
        open_button.clicked.connect(self.apri_cliente_selezionato)
        button_layout.addWidget(open_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Carica la lista dei clienti disponibili
        self.lista_clienti = self.carica_clienti_disponibili()

        # Chiamata ai metodi per popolare l'elenco dei clienti senza e con prenotazioni
        self.aggiungi_clienti_senza_prenotazioni()
        self.aggiungi_clienti_con_prenotazioni()

        self.vista_prenotazione = None

    def carica_clienti_disponibili(self):
        # Carica i clienti dal file "Dati/Clienti.pickle" o inizializza una lista vuota
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                return list(clienti.values())
        else:
            return []

    def aggiungi_clienti_senza_prenotazioni(self):
        clienti_senza_prenotazioni = [cliente for cliente in self.lista_clienti if cliente.prenotato == 0]

        clienti_senza_prenotazioni_model = QStandardItemModel()
        for cliente in clienti_senza_prenotazioni:
            item = QStandardItem(f"{cliente.nome} {cliente.cognome}")
            clienti_senza_prenotazioni_model.appendRow(item)

        self.clienti_senza_prenotazioni_view.setModel(clienti_senza_prenotazioni_model)

    def apri_cliente_selezionato(self):
        selected_index = self.clienti_senza_prenotazioni_view.selectedIndexes()

        if not selected_index:
            # Nessun cliente selezionato
            print("Nessun cliente selezionato")
            return

        # Estrai l'indice del cliente selezionato
        index = selected_index[0].row()

        # Recupera l'oggetto QStandardItem corrispondente all'indice
        cliente_selezionato_item = self.clienti_senza_prenotazioni_view.model().item(index)

        if cliente_selezionato_item:
            # Ottieni il testo dell'elemento QStandardItem, che contiene il nome completo del cliente
            nome_completo = cliente_selezionato_item.text()

            # Cerca il cliente corrispondente nella lista dei clienti
            for cliente in self.lista_clienti:
                if f"{cliente.nome} {cliente.cognome}" == nome_completo:
                    # Crea una nuova finestra per la prenotazione e passa il cliente selezionato a essa
                    print(f"Apertura di VistaPrenotazione per il cliente {cliente.nome} {cliente.cognome}")
                    self.vista_prenotazione = VistaPrenotazione(cliente, self.aggiorna_liste_clienti)
                    self.vista_prenotazione.show()
                    return

    def aggiungi_clienti_con_prenotazioni(self):
        clienti_con_prenotazioni = [cliente for cliente in self.lista_clienti if cliente.prenotato == 1]

        clienti_con_prenotazioni_model = QStandardItemModel()
        for cliente in clienti_con_prenotazioni:
            item = QStandardItem(f"{cliente.nome} {cliente.cognome}")
            clienti_con_prenotazioni_model.appendRow(item)

        self.clienti_con_prenotazioni_view.setModel(clienti_con_prenotazioni_model)

    def aggiorna_liste_clienti(self):
        # Ricarica la lista dei clienti disponibili
        self.lista_clienti = self.carica_clienti_disponibili()

        # Aggiorna l'elenco dei clienti senza prenotazioni
        self.aggiungi_clienti_senza_prenotazioni()

        # Aggiorna l'elenco dei clienti con prenotazioni
        self.aggiungi_clienti_con_prenotazioni()
