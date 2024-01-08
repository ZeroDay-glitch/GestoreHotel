from datetime import datetime
import traceback
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from Attivita.Cliente import Cliente


class VistaInserisciCliente(QWidget):

    def __init__(self, callback):
        super(VistaInserisciCliente, self).__init__()
        self.callback = callback
        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("codice", "Codice")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("codiceFiscale", "Codice Fiscale")
        self.add_info_text("dataNascita", "Data di Nascita")
        self.add_info_text("documentoValido", "Documento Valido")
        self.add_info_text("email", "Email")
        self.add_info_text("telefono", "Telefono")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.aggiungi_cliente)  # Collega il pulsante al nuovo metodo
        self.qlines["btn_ok"] = btn_ok
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Cliente")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def aggiungi_cliente(self):
        try:
            codice = int(self.qlines["codice"].text())
        except ValueError:
            QMessageBox.critical(self, "Errore", "Il codice non sembra un numero valido.", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, "Errore", "Per favore inserisci tutte le informazioni richieste",
                                         QMessageBox.Ok, QMessageBox.Ok)
                    return

        try:
            nome = self.qlines["nome"].text()
            cognome = self.qlines["cognome"].text()
            codiceFiscale = self.qlines["codiceFiscale"].text()
            dataNascita = datetime.strptime(self.qlines["dataNascita"].text(), "%d/%m/%Y")
            documentoValido = self.qlines["documentoValido"].text()
            email = self.qlines["email"].text()
            telefono = int(self.qlines["telefono"].text())
        except ValueError:
            QMessageBox.critical(self, "Errore", "I dati inseriti non sono validi.", QMessageBox.Ok, QMessageBox.Ok)
            return

        # Crea un nuovo cliente
        nuovo_cliente = Cliente(codice, codiceFiscale, cognome, dataNascita, documentoValido, email, "", nome, telefono)

        # Debug: Stampa informazioni prima della callback
        print("Prima della callback")

        try:
            # Chiama la callback con il nuovo cliente
            self.callback(nuovo_cliente)

            # Debug: Stampa informazioni dopo la callback
            print("Dopo la callback")

            # Chiudi la finestra dopo l'aggiunta del cliente
            self.close()

        except Exception as e:
            # Debug: Stampa informazioni in caso di errore nella callback
            print(f"Errore durante l'invocazione della callback: {e}")
            traceback.print_exc()
            QMessageBox.critical(self, "Errore", "Si è verificato un errore durante l'aggiunta del cliente.",
                                 QMessageBox.Ok, QMessageBox.Ok)