from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class VistaModificaReceptionist(QDialog):
    def __init__(self, receptionist, callback, vista_receptionist):
        super(VistaModificaReceptionist, self).__init__()
        self.receptionist = receptionist
        self.callback = callback
        self.vista_receptionist = vista_receptionist

        v_layout = QVBoxLayout(self)

        self.qlines = {}

        self.add_info_text("nome", "Nome", receptionist.nome)
        self.add_info_text("cognome", "Cognome", receptionist.cognome)
        self.add_info_text("dataNascita", "Data Nascita", str(receptionist.data_nascita))
        self.add_info_text("luogoNascita", "Luogo Nascita", receptionist.luogo_nascita)
        self.add_info_text("cellulare", "Cellulare", receptionist.cellulare)
        self.add_info_text("lingue", "Lingue", ', '.join(receptionist.lingue))
        self.add_info_text("password", "Password", receptionist.password)

        btn_salva = QPushButton("Salva")
        btn_salva.clicked.connect(self.salva_modifiche)
        btn_salva.setStyleSheet("""
                   QPushButton {
                       background-color: #C3D4C7;
                       color: black;
                       border-radius: 10px;
                       padding: 10px 15px; 
                       font-size: 16px; 
                       border: 2px solid #555;
                       transition: background-color 0.3s, color 0.3s; 
                   }
                   QPushButton:hover {
                       background-color: #707070;
                       color: white;
                       border: 2px solid #707070; 
                   }
                   QPushButton:pressed {
                       background-color: #505050; 
                   }
               """)
        v_layout.addWidget(btn_salva)

        self.setWindowTitle("Modifica Receptionist")
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
        nuovo_lingue = self.qlines["lingue"].text().split(", ")
        nuova_password = self.qlines["password"].text()

        new_data = {
            "nome": nuovo_nome,
            "cognome": nuovo_cognome,
            "data_nascita": nuovo_data_nascita,
            "luogo_nascita": nuovo_luogo_nascita,
            "cellulare": nuovo_cellulare,
            "lingue": nuovo_lingue,
            "password": nuova_password
        }

        success = self.receptionist.modifica_dipendente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            pass
