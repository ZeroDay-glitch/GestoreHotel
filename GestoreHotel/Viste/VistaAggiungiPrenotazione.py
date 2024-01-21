import os.path
import pickle
import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QCalendarWidget, QSpinBox, QPushButton, QMessageBox
from PyQt5.QtCore import QDateTime

from Attivita.Prenotazione import Prenotazione


class VistaAggiungiPrenotazione(QWidget):
    def __init__(self, clienti, servizi, callback):
        super(VistaAggiungiPrenotazione, self).__init__()
        self.clienti = clienti
        self.servizi = servizi
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.setup_ui()
        self.setWindowTitle("Nuova Prenotazione")
        self.setStyleSheet("background-color: #393535;")

    def setup_ui(self):
        self.clienti_combobox = QComboBox(self)
        self.populate_clienti_combobox()
        self.v_layout.addWidget(self.clienti_combobox)
        self.data_inizio_calendar = QCalendarWidget()
        self.v_layout.addWidget(QLabel("Data di Inizio"))
        self.v_layout.addWidget(self.data_inizio_calendar)

        self.data_fine_calendar = QCalendarWidget()
        self.v_layout.addWidget(QLabel("Data di Fine"))
        self.v_layout.addWidget(self.data_fine_calendar)
        self.num_ospiti_spinbox = QSpinBox()
        self.num_ospiti_spinbox.setMinimum(1)
        self.v_layout.addWidget(QLabel("Numero di Ospiti"))
        self.v_layout.addWidget(self.num_ospiti_spinbox)

        btn_annulla = QPushButton("Annulla")
        btn_annulla.clicked.connect(self.close)
        self.v_layout.addWidget(btn_annulla)

        btn_annulla.setStyleSheet("""
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

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_prenotazione)
        self.v_layout.addWidget(btn_ok)

        btn_ok.setStyleSheet("""
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

        self.setLayout(self.v_layout)

    def populate_clienti_combobox(self):
        self.clienti_combobox.clear()
        for cliente in self.clienti.values():
            if not cliente.bloccato:
                self.clienti_combobox.addItem(f"{cliente.nome} {cliente.cognome}", cliente)

    def aggiungi_prenotazione(self):
        cliente_index = self.clienti_combobox.currentIndex()

        if cliente_index == -1:
            QMessageBox.critical(self, 'Errore', 'Seleziona un cliente', QMessageBox.Ok, QMessageBox.Ok)
            return

        cliente_selezionato = list(self.clienti.values())[cliente_index]

        if cliente_selezionato.bloccato:
            QMessageBox.critical(self, 'Errore', 'Questo cliente è bloccato e non può effettuare prenotazioni.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        data_inizio = self.data_inizio_calendar.selectedDate()
        data_fine = self.data_fine_calendar.selectedDate()

        data_inizio = datetime.datetime(data_inizio.year(), data_inizio.month(), data_inizio.day())
        data_fine = datetime.datetime(data_fine.year(), data_fine.month(), data_fine.day())

        numero_ospiti = self.num_ospiti_spinbox.value()

        if not cliente_selezionato or not data_inizio or not data_fine:
            QMessageBox.critical(self, 'Errore', 'Compila tutti i campi obbligatori', QMessageBox.Ok, QMessageBox.Ok)
            return

        servizi_selezionati = []

        codice = self.generate_unique_code()

        prenotazione = Prenotazione(cliente_selezionato, codice, data_inizio, data_fine, numero_ospiti, "Receptionist", servizi_selezionati)
        self.salva_prenotazione(prenotazione)
        self.callback()
        self.close()

    def generate_unique_code(self):
        while True:
            timestamp = QDateTime.currentDateTime().toMSecsSinceEpoch()
            new_code = int(timestamp)
            if not os.path.exists('Dati/Prenotazioni.pickle') or new_code not in pickle.load(open('Dati/Prenotazioni.pickle', 'rb')):
                return new_code

    def salva_prenotazione(self, prenotazione):
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        else:
            prenotazioni = {}
        prenotazioni[prenotazione.codice] = prenotazione
        with open('Dati/Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
