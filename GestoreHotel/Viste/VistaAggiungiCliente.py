from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCalendarWidget
import os.path
import pickle
from Attivita.Cliente import Cliente


class VistaAggiungiCliente(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiCliente, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.load_existing_codes()
        self.add_info_text("codice", "Codice")
        self.qlines["codice"].setText(str(self.generate_unique_code()))
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_calendar("data_nascita", "Data di Nascita")
        self.add_info_text("luogo_nascita", "Luogo di Nascita")
        self.add_info_text("cellulare", "Cellulare")
        self.add_info_text("codice_fiscale", "Codice Fiscale")
        self.add_info_text("documento", "Documento")
        self.add_info_text("email", "Email")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_cliente)
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
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Cliente")
        self.setStyleSheet("background-color: lightgreen;")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.setStyleSheet("background-color: white;")
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)
        if nome == "codice":
            current_text.setReadOnly(True)  # Imposta il campo di testo come di sola lettura
            current_text.setMaximumHeight(30)
        self.qlines[nome] = current_text

    def add_calendar(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        self.calendar = QCalendarWidget(self)
        self.calendar.setStyleSheet("background-color: #87CEEB;")
        self.qlines[nome] = self.calendar
        self.v_layout.addWidget(self.calendar)

    def load_existing_codes(self):
        self.codici_esistenti = []
        file_path = 'Dati/codici_esistenti.pickle'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                self.codici_esistenti = pickle.load(f)

    def aggiungi_cliente(self):
        try:
            codice = int(self.qlines["codice"].text())
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            data_nascita = self.qlines["data_nascita"].selectedDate().toPyDate()
            luogo_nascita = self.qlines["luogo_nascita"].text()
            cellulare = self.qlines["cellulare"].text()
            codice_fiscale = self.qlines["codice_fiscale"].text()
            documento = self.qlines["documento"].text()
            email = self.qlines["email"].text()

            if not codice or not nome or not cognome or not data_nascita or not luogo_nascita or not cellulare:
                QMessageBox.critical(self, 'Errore', 'Compila tutti i campi obbligatori',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

            nuovo_cliente = Cliente(cellulare, codice, codice_fiscale, cognome, data_nascita, documento, email,
                                     luogo_nascita, nome)
            self.callback()  # Aggiorna la vista principale
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Errore', f'Errore durante l\'aggiunta del cliente: {e}',
                                 QMessageBox.Ok)

    def generate_unique_code(self):
        while True:
            timestamp = QDateTime.currentDateTime().toMSecsSinceEpoch()
            new_code = int(timestamp)
            if new_code not in self.codici_esistenti:
                return new_code
