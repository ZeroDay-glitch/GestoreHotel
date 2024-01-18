from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.prenotazione = prenotazione
        self.layout = QVBoxLayout()

        # Imposta un font più grande per i dettagli
        font = QFont()
        font.setPointSize(12)

        # Funzione per aggiungere le etichette con un font personalizzato
        def add_label(text):
            label = QLabel(text)
            label.setFont(font)
            self.layout.addWidget(label)

        add_label(f"Cliente: {prenotazione.cliente.nome} {prenotazione.cliente.cognome}")
        add_label(f"Codice Prenotazione: {prenotazione.codice}")
        add_label(f"Data Inizio: {prenotazione.data_ora_inizio}")
        add_label(f"Data Fine: {prenotazione.data_ora_fine}")
        add_label(f"Numero Ospiti: {prenotazione.numero_ospiti}")

        # Verifica e mostra lo stato dei servizi
        servizio_in_camera = "Sì" if any(
            servizio.tipo_servizio == "Servizio in Camera" for servizio in prenotazione.servizi) else "No"
        parcheggio = "Sì" if any(servizio.tipo_servizio == "Parcheggio" for servizio in prenotazione.servizi) else "No"

        add_label(f"Servizio in Camera: {servizio_in_camera}")
        add_label(f"Parcheggio: {parcheggio}")

        # ... altro codice ...

        btn_close = QPushButton("Chiudi")
        btn_close.clicked.connect(self.close)
        self.layout.addWidget(btn_close)

        self.setLayout(self.layout)
        self.setWindowTitle(f"Dettagli Prenotazione: {prenotazione.codice}")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgreen;")