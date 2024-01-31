import pickle

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox


class VistaNoteCliente(QDialog):
    def __init__(self, cliente, callback_aggiornamento, parent=None):
        super(VistaNoteCliente, self).__init__(parent)
        self.cliente = cliente
        self.callback_aggiornamento = callback_aggiornamento

        self.v_layout = QVBoxLayout()

        self.label_note = QLabel("Note:")
        self.label_note.setStyleSheet("color: white;")
        self.v_layout.addWidget(self.label_note)

        self.text_edit_note = QTextEdit(self)
        self.text_edit_note.setText(cliente.note)
        self.text_edit_note.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: black;
                border: 1px solid #555;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.v_layout.addWidget(self.text_edit_note)

        # Inizializza i pulsanti come attributi della classe
        self.btn_blocca = QPushButton()
        self.btn_sblocca = QPushButton()
        self.btn_messaggio = QPushButton()
        self.btn_salva = QPushButton()

        self.create_button(self.btn_blocca, "Blocca Cliente", self.blocca_cliente)
        self.create_button(self.btn_sblocca, "Sblocca Cliente", self.sblocca_cliente)
        self.create_button(self.btn_messaggio, "Invia Messaggio", self.invia_messaggio)
        self.create_button(self.btn_salva, "Salva", self.salva_note)

        if self.cliente.bloccato:
            self.btn_blocca.hide()
        else:
            self.btn_sblocca.hide()

        self.setLayout(self.v_layout)
        self.setWindowTitle("Gestione Note Cliente")
        self.setStyleSheet("background-color: #393535;")

    def create_button(self, button, text, on_click):
        button = QPushButton(text)
        button.clicked.connect(on_click)
        button.setStyleSheet("""
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
        self.v_layout.addWidget(button)

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
        self.callback_aggiornamento()
        QMessageBox.information(self, "Sblocca Cliente", "Il cliente è stato sbloccato con successo.")

    def invia_messaggio(self):
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
