from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class VistaModificaCliente(QDialog):
    def __init__(self, cliente, callback, vista_cliente):
        super(VistaModificaCliente, self).__init__()
        self.cliente = cliente
        self.callback = callback
        self.vista_cliente = vista_cliente

        v_layout = QVBoxLayout(self)

        self.qlines = {}

        self.add_info_text("nome", "Nome", cliente.nome)
        self.add_info_text("cognome", "Cognome", cliente.cognome)
        self.add_info_text("dataNascita", "Data Nascita", str(cliente.data_nascita))
        self.add_info_text("luogoNascita", "Luogo Nascita", cliente.luogo_nascita)
        self.add_info_text("cellulare", "Cellulare", cliente.cellulare)
        self.add_info_text("codice_fiscale", "Codice Fiscale", cliente.codice_fiscale)
        self.add_info_text("documento", "Documento", cliente.documento)
        self.add_info_text("email", "Email", cliente.email)
        self.add_info_text("note", "Note", cliente.note)

        btn_salva = QPushButton("Salva")
        btn_salva.clicked.connect(self.salva_modifiche)
        btn_salva.setStyleSheet("""
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
        v_layout.addWidget(btn_salva)

        self.setWindowTitle("Modifica Cliente")
        self.setStyleSheet("background-color: #393535;")

    def add_info_text(self, nome, label, valore_iniziale=""):
        v_layout = self.layout()

        label_widget = QLabel(label)
        label_widget.setStyleSheet("color: white;")
        v_layout.addWidget(label_widget)

        current_text = QLineEdit(valore_iniziale, self)
        current_text.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: white;
                border: 1px solid #555;
                border-radius: 10px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #aaa;
            }
        """)
        self.qlines[nome] = current_text
        v_layout.addWidget(current_text)

    def salva_modifiche(self):
        nuovo_nome = self.qlines["nome"].text()
        nuovo_cognome = self.qlines["cognome"].text()
        nuovo_data_nascita = self.qlines["dataNascita"].text()
        nuovo_luogo_nascita = self.qlines["luogoNascita"].text()
        nuovo_cellulare = self.qlines["cellulare"].text()
        nuovo_codice_fiscale = self.qlines["codice_fiscale"].text()
        nuovo_documento = self.qlines["documento"].text()
        nuovo_email = self.qlines["email"].text()
        nuovo_note = self.qlines["note"].text()

        new_data = {
            "nome": nuovo_nome,
            "cognome": nuovo_cognome,
            "data_nascita": nuovo_data_nascita,
            "luogo_nascita": nuovo_luogo_nascita,
            "cellulare": nuovo_cellulare,
            "codice_fiscale": nuovo_codice_fiscale,
            "documento": nuovo_documento,
            "email": nuovo_email,
            "note": nuovo_note
        }

        success = self.cliente.modifica_cliente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            pass
