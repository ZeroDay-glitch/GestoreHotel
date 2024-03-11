import os.path
import pickle
import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QCalendarWidget, QSpinBox, QPushButton, \
    QMessageBox, QCompleter
from PyQt5.QtCore import QDateTime, Qt, QDate

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
        self.clienti_combobox.setStyleSheet("background-color: white; color: black;")
        self.populate_clienti_combobox()
        self.v_layout.addWidget(self.clienti_combobox)

        self.add_label_with_style("Data di Inizio")
        self.data_inizio_calendar = QCalendarWidget()
        self.data_inizio_calendar.setStyleSheet("background-color: #C3D4C7;")
        self.v_layout.addWidget(self.data_inizio_calendar)

        self.add_label_with_style("Data di Fine")
        self.data_fine_calendar = QCalendarWidget()
        self.data_fine_calendar.setStyleSheet("background-color: #C3D4C7;")
        self.v_layout.addWidget(self.data_fine_calendar)

        self.add_label_with_style("Numero di Ospiti")
        self.num_ospiti_spinbox = QSpinBox()
        self.num_ospiti_spinbox.setStyleSheet("background-color: white; color: black;")
        self.num_ospiti_spinbox.setMinimum(1)
        self.v_layout.addWidget(self.num_ospiti_spinbox)

        btn_annulla = QPushButton("Annulla")
        btn_annulla.clicked.connect(self.close)
        btn_annulla.setStyleSheet("""
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
        self.v_layout.addWidget(btn_annulla)

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_prenotazione)
        btn_ok.setStyleSheet("""
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
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)

    def add_label_with_style(self, text):
        label = QLabel(text)
        label.setStyleSheet("color: white;")
        self.v_layout.addWidget(label)

    def populate_clienti_combobox(self):
        self.clienti_combobox.clear()
        clienti_nomi = []

        for cliente in self.clienti.values():
            if not cliente.bloccato:
                nome_cliente = f"{cliente.nome} {cliente.cognome}"
                self.clienti_combobox.addItem(nome_cliente, cliente)
                clienti_nomi.append(nome_cliente)

        completer = QCompleter(clienti_nomi, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.clienti_combobox.setCompleter(completer)

        self.clienti_combobox.setEditable(True)
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

        if not data_inizio or not data_fine:
            QMessageBox.critical(self, 'Errore', 'Compila tutti i campi obbligatori', QMessageBox.Ok, QMessageBox.Ok)
            return

        if data_fine <= data_inizio:
            QMessageBox.critical(self, 'Errore', 'La data di fine deve essere successiva alla data di inizio',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        oggi = QDate.currentDate()
        if data_inizio <= oggi.addDays(1):
            QMessageBox.critical(self, 'Errore', 'La prenotazione deve essere effettuata almeno un giorno di anticipo',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        numero_ospiti = self.num_ospiti_spinbox.value()

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
