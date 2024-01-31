from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class VistaPrenotazione(QWidget):
    def __init__(self, prenotazione, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.prenotazione = prenotazione
        self.layout = QVBoxLayout()

        font = QFont()
        font.setPointSize(12)

        def add_label(text):
            label = QLabel(text)
            label.setFont(font)
            label.setStyleSheet("color: white;")  # Aggiunta del colore bianco per il testo
            self.layout.addWidget(label)

        add_label(f"Cliente: {prenotazione.cliente.nome} {prenotazione.cliente.cognome}")
        add_label(f"Codice Prenotazione: {prenotazione.codice}")
        add_label(f"Data Inizio: {prenotazione.data_ora_inizio}")
        add_label(f"Data Fine: {prenotazione.data_ora_fine}")
        add_label(f"Numero Ospiti: {prenotazione.numero_ospiti}")

        servizio_in_camera = "Sì" if any(
            servizio.tipo_servizio == "Servizio in Camera" for servizio in prenotazione.servizi) else "No"
        parcheggio = "Sì" if any(servizio.tipo_servizio == "Parcheggio" for servizio in prenotazione.servizi) else "No"

        add_label(f"Servizio in Camera: {servizio_in_camera}")
        add_label(f"Parcheggio: {parcheggio}")

        btn_close = QPushButton("Chiudi")
        btn_close.clicked.connect(self.close)
        btn_close.setStyleSheet("""
            QPushButton {
                background-color: #C3D4C7;
                color: black;
                border-radius: 10px;
                padding: 10px 15px; /* Aggiunto padding più generoso */
                font-size: 16px; /* Aumentato la dimensione del font */
                border: 2px solid #555; /* Aggiunto bordo per coerenza */
                transition: background-color 0.3s, color 0.3s; /* Effetto transizione più fluido */
            }
            QPushButton:hover {
                background-color: #707070;
                color: white;
                border: 2px solid #707070; /* Bordo che cambia con il colore di sfondo */
            }
            QPushButton:pressed {
                background-color: #505050; /* Leggermente più scuro al click */
            }
        """)
        self.layout.addWidget(btn_close)

        self.setLayout(self.layout)
        self.setWindowTitle(f"Dettagli Prenotazione: {prenotazione.codice}")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #393535;")