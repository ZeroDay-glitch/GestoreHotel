from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class VistaModificaCliente(QDialog):
    def __init__(self, cliente, callback, vista_cliente):
        super(VistaModificaCliente, self).__init__()
        self.cliente = cliente
        self.callback = callback
        self.vista_cliente = vista_cliente

        # Creiamo un nuovo QVBoxLayout per questa vista
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
        btn_salva.clicked.connect(self.salva_modifiche)  # Collega il pulsante Salva alla funzione salva_modifiche
        v_layout.addWidget(btn_salva)

        self.setWindowTitle("Modifica Cliente")
        self.setStyleSheet("background-color: lightgreen;")

    def add_info_text(self, nome, label, valore_iniziale=""):
        v_layout = self.layout()  # Otteniamo il layout corrente della vista

        label_widget = QLabel(label)
        v_layout.addWidget(label_widget)

        current_text = QLineEdit(valore_iniziale, self)
        current_text.setStyleSheet("background-color: white;")
        self.qlines[nome] = current_text
        v_layout.addWidget(current_text)

    def salva_modifiche(self):
        # Ottieni i nuovi valori dai campi di testo
        nuovo_nome = self.qlines["nome"].text()
        nuovo_cognome = self.qlines["cognome"].text()
        nuovo_data_nascita = self.qlines["dataNascita"].text()
        nuovo_luogo_nascita = self.qlines["luogoNascita"].text()
        nuovo_cellulare = self.qlines["cellulare"].text()
        nuovo_codice_fiscale = self.qlines["codice_fiscale"].text()
        nuovo_documento = self.qlines["documento"].text()
        nuovo_email = self.qlines["email"].text()
        nuovo_note = self.qlines["note"].text()

        # Crea un dizionario con i nuovi dati
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

        # Chiama il metodo per sovrascrivere i dati del cliente
        success = self.cliente.modifica_cliente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            # Gestisci il caso in cui la modifica non sia riuscita
            # Mostra un messaggio di errore o fai altro in base alle tue esigenze
            pass
