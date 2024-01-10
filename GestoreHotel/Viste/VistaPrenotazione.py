import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from Attivita.Prenotazione import Prenotazione
from Attivita.Receptionist import Receptionist

class VistaPrenotazione(QWidget):
    def __init__(self, cliente, callback=None, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.cliente = cliente
        self.callback = callback
        self.setWindowTitle(f"Aggiungi Prenotazione per {cliente.nome} {cliente.cognome}")

        layout = QVBoxLayout()

        # Codice
        self.codice_label = QLabel("Codice:")
        self.codice_edit = QLineEdit()
        layout.addWidget(self.codice_label)
        layout.addWidget(self.codice_edit)

        # Data di Inizio
        self.data_inizio_label = QLabel("Data di Inizio (YYYY-MM-DD HH:MM:SS):")
        self.data_inizio_edit = QLineEdit()
        layout.addWidget(self.data_inizio_label)
        layout.addWidget(self.data_inizio_edit)

        # Data di Scadenza
        self.data_scadenza_label = QLabel("Data di Scadenza (YYYY-MM-DD HH:MM:SS):")
        self.data_scadenza_edit = QLineEdit()
        layout.addWidget(self.data_scadenza_label)
        layout.addWidget(self.data_scadenza_edit)

        # Data di Emissione (mostrerà la data attuale)
        self.data_emissione_label = QLabel("Data di Emissione:")
        self.data_emissione_edit = QLineEdit()
        self.data_emissione_edit.setReadOnly(True)  # Per impedire l'editing manuale
        layout.addWidget(self.data_emissione_label)
        layout.addWidget(self.data_emissione_edit)

        # Numero Ospiti
        self.numero_ospiti_label = QLabel("Numero Ospiti:")
        self.numero_ospiti_edit = QLineEdit()
        layout.addWidget(self.numero_ospiti_label)
        layout.addWidget(self.numero_ospiti_edit)

        # Caparra Versata
        self.caparra_versata_label = QLabel("Caparra Versata:")
        self.caparra_versata_edit = QLineEdit()
        layout.addWidget(self.caparra_versata_label)
        layout.addWidget(self.caparra_versata_edit)

        # Receptionist
        self.receptionist_label = QLabel("Receptionist:")
        self.receptionist_edit = QLineEdit()
        layout.addWidget(self.receptionist_label)
        layout.addWidget(self.receptionist_edit)

        # Servizio in Camera (checkbox)
        self.servizio_in_camera_checkbox = QCheckBox("Servizio in Camera")
        layout.addWidget(self.servizio_in_camera_checkbox)

        # Parcheggio (checkbox)
        self.parcheggio_checkbox = QCheckBox("Parcheggio")
        layout.addWidget(self.parcheggio_checkbox)

        # Pulsante Conferma
        conferma_button = QPushButton("Conferma")
        conferma_button.clicked.connect(self.conferma_prenotazione)
        layout.addWidget(conferma_button)

        self.setLayout(layout)

        self.show()

    def conferma_prenotazione(self):
        codice = self.codice_edit.text()
        data_inizio_text = self.data_inizio_edit.text()
        data_scadenza_text = self.data_scadenza_edit.text()
        numero_ospiti_text = self.numero_ospiti_edit.text()
        caparra_versata_text = self.caparra_versata_edit.text()
        receptionist = self.receptionist_edit.text()

        # Verifica che nessun campo obbligatorio sia vuoto
        if not all(
                [codice, data_inizio_text, data_scadenza_text, numero_ospiti_text, caparra_versata_text, receptionist]):
            QMessageBox.warning(self, "Errore", "Tutti i campi sono obbligatori.", QMessageBox.Ok, QMessageBox.Ok)
            return

        # Verifica che le date siano nel formato corretto
        try:
            data_inizio = datetime.datetime.strptime(data_inizio_text, "%Y-%m-%d %H:%M:%S")
            data_scadenza = datetime.datetime.strptime(data_scadenza_text, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            QMessageBox.critical(self, "Errore", "Formato data non valido.", QMessageBox.Ok, QMessageBox.Ok)
            return

        # Verifica che il numero degli ospiti sia un intero valido
        try:
            numero_ospiti = int(numero_ospiti_text)
        except ValueError:
            QMessageBox.critical(self, "Errore", "Il numero degli ospiti deve essere un numero intero.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        # Verifica che la caparra versata sia un numero decimale valido
        try:
            caparra_versata = float(caparra_versata_text)
        except ValueError:
            QMessageBox.critical(self, "Errore", "La caparra versata deve essere un numero.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return
        receptionist = self.receptionist_edit.text()

        # Calcola lo stato della prenotazione in base alle date
        if data_inizio > datetime.datetime.now():
            stato_prenotazione = "Prenotata"
        else:
            stato_prenotazione = "Occupata"

        # Verifica se i checkbox sono selezionati
        servizio_in_camera = self.servizio_in_camera_checkbox.isChecked()
        parcheggio = self.parcheggio_checkbox.isChecked()

        # Crea un'istanza di Prenotazione con queste informazioni
        prenotazione = Prenotazione(self.cliente, codice, data_inizio, datetime.datetime.now(), data_scadenza,
                                    numero_ospiti, stato_prenotazione, caparra_versata, servizio_in_camera,
                                    parcheggio, receptionist)

        # Esegui il callback per aggiornare le liste nella vista principale, se definito
        if self.callback:
            self.callback()

        # Chiudi la finestra di prenotazione
        self.close()
