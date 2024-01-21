import pickle

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox


class VistaNoteCliente(QDialog):
    def __init__(self, cliente, callback_aggiornamento, parent=None):
        super(VistaNoteCliente, self).__init__(parent)
        self.cliente = cliente
        self.callback_aggiornamento = callback_aggiornamento

        self.v_layout = QVBoxLayout()

        self.label_note = QLabel("Note:")
        self.v_layout.addWidget(self.label_note)

        self.text_edit_note = QTextEdit(self)
        self.text_edit_note.setText(cliente.note)
        self.v_layout.addWidget(self.text_edit_note)

        self.btn_blocca = QPushButton("Blocca Cliente")
        self.btn_blocca.clicked.connect(self.blocca_cliente)
        self.v_layout.addWidget(self.btn_blocca)

        self.btn_sblocca = QPushButton("Sblocca Cliente")
        self.btn_sblocca.clicked.connect(self.sblocca_cliente)
        self.v_layout.addWidget(self.btn_sblocca)

        if self.cliente.bloccato:
            self.btn_blocca.hide()
        else:
            self.btn_sblocca.hide()

        self.btn_messaggio = QPushButton("Invia Messaggio")
        self.btn_messaggio.clicked.connect(self.invia_messaggio)
        self.v_layout.addWidget(self.btn_messaggio)

        self.btn_salva = QPushButton("Salva")
        self.btn_salva.clicked.connect(self.salva_note)
        self.v_layout.addWidget(self.btn_salva)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Note Cliente")

    def blocca_cliente(self):
        self.cliente.bloccato = True
        try:
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
            clienti[self.cliente.codice] = self.cliente
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            QMessageBox.critical(self, 'Errore', f'Errore: {e}', QMessageBox.Ok)
        self.aggiorna_pulsanti_blocco()
        self.callback_aggiornamento()
        QMessageBox.information(self, "Blocca Cliente", "Il cliente è stato bloccato con successo.")

    def sblocca_cliente(self):
        self.cliente.bloccato = False
        try:
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
            clienti[self.cliente.codice] = self.cliente
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            QMessageBox.critical(self, 'Errore', f'Errore: {e}', QMessageBox.Ok)
        self.aggiorna_pulsanti_blocco()
        self.callback_aggiornamento()
        QMessageBox.information(self, "Sblocca Cliente", "Il cliente è stato sbloccato con successo.")

    def aggiorna_pulsanti_blocco(self):
        if self.cliente.bloccato:
            self.btn_blocca.hide()
            self.btn_sblocca.show()
        else:
            self.btn_blocca.show()
            self.btn_sblocca.hide()

    def invia_messaggio(self):
        # Implementa la logica per inviare un messaggio al cliente
        QMessageBox.information(self, "Invia Messaggio", "Messaggio inviato (implementa la logica appropriata).")

    def salva_note(self):
        self.cliente.note = self.text_edit_note.toPlainText()
        try:
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
            clienti[self.cliente.codice] = self.cliente
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            QMessageBox.critical(self, 'Errore', f'Errore durante il salvataggio delle note: {e}', QMessageBox.Ok)
        self.callback_aggiornamento()
        self.accept()
