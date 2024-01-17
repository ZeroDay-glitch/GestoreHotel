from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QLineEdit, QDialog


class VistaModificaAddettoServizi(QDialog):
    def __init__(self, addetto_servizi, callback, vista_addetto_servizi):
        super(VistaModificaAddettoServizi, self).__init__()
        self.addetto_servizi = addetto_servizi
        self.callback = callback
        self.vista_addetto_servizi = vista_addetto_servizi

        v_layout = QVBoxLayout(self)

        self.qlines = {}

        self.add_info_text("nome", "Nome", addetto_servizi.nome)
        self.add_info_text("cognome", "Cognome", addetto_servizi.cognome)
        self.add_info_text("dataNascita", "Data Nascita", str(addetto_servizi.data_nascita))
        self.add_info_text("luogoNascita", "Luogo Nascita", addetto_servizi.luogo_nascita)
        self.add_info_text("cellulare", "Cellulare", addetto_servizi.cellulare)

        btn_salva = QPushButton("Salva")
        btn_salva.clicked.connect(self.salva_modifiche)
        v_layout.addWidget(btn_salva)

        self.setWindowTitle("Modifica Addetto ai Servizi")
        self.setStyleSheet("background-color: lightgreen;")

    def add_info_text(self, nome, label, valore_iniziale=""):
        v_layout = self.layout()

        label_widget = QLabel(label)
        v_layout.addWidget(label_widget)

        current_text = QLineEdit(valore_iniziale, self)
        current_text.setStyleSheet("background-color: white;")
        self.qlines[nome] = current_text
        v_layout.addWidget(current_text)

    def salva_modifiche(self):
        nuovo_nome = self.qlines["nome"].text()
        nuovo_cognome = self.qlines["cognome"].text()
        nuovo_data_nascita = self.qlines["dataNascita"].text()
        nuovo_luogo_nascita = self.qlines["luogoNascita"].text()
        nuovo_cellulare = self.qlines["cellulare"].text()

        # Crea un dizionario con i nuovi dati
        new_data = {
            "nome": nuovo_nome,
            "cognome": nuovo_cognome,
            "data_nascita": nuovo_data_nascita,
            "luogo_nascita": nuovo_luogo_nascita,
            "cellulare": nuovo_cellulare,
        }

        success = self.addetto_servizi.modifica_dipendente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            pass