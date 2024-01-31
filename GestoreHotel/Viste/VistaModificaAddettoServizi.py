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
        self.add_info_text("password", "Password", addetto_servizi.password)

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

        self.setWindowTitle("Modifica Addetto ai Servizi")
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
        nuova_password = self.qlines["password"].text()

        # Crea un dizionario con i nuovi dati
        new_data = {
            "nome": nuovo_nome,
            "cognome": nuovo_cognome,
            "data_nascita": nuovo_data_nascita,
            "luogo_nascita": nuovo_luogo_nascita,
            "cellulare": nuovo_cellulare,
            "password": nuova_password,
        }

        success = self.addetto_servizi.modifica_dipendente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            pass
