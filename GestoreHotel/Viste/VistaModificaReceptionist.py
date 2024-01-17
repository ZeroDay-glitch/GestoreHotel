from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from Attivita.Receptionist import Receptionist


class VistaModificaReceptionist(QDialog):
    def __init__(self, receptionist, callback, vista_receptionist):
        super(VistaModificaReceptionist, self).__init__()
        self.receptionist = receptionist
        self.callback = callback
        self.vista_receptionist = vista_receptionist

        # Creiamo un nuovo QVBoxLayout per questa vista
        v_layout = QVBoxLayout(self)

        self.qlines = {}

        self.add_info_text("nome", "Nome", receptionist.nome)
        self.add_info_text("cognome", "Cognome", receptionist.cognome)
        self.add_info_text("dataNascita", "Data Nascita", str(receptionist.data_nascita))
        self.add_info_text("luogoNascita", "Luogo Nascita", receptionist.luogo_nascita)
        self.add_info_text("cellulare", "Cellulare", receptionist.cellulare)
        self.add_info_text("lingue", "Lingue (separate da virgola)", ', '.join(receptionist.lingue))

        btn_salva = QPushButton("Salva")
        btn_salva.clicked.connect(self.salva_modifiche)  # Collega il pulsante Salva alla funzione salva_modifiche
        v_layout.addWidget(btn_salva)

        self.setWindowTitle("Modifica Receptionist")
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
        nuovo_lingue = self.qlines["lingue"].text().split(", ")

        # Crea un dizionario con i nuovi dati
        new_data = {
            "nome": nuovo_nome,
            "cognome": nuovo_cognome,
            "data_nascita": nuovo_data_nascita,
            "luogo_nascita": nuovo_luogo_nascita,
            "cellulare": nuovo_cellulare,
            "lingue": nuovo_lingue
        }

        # Chiama il metodo per sovrascrivere i dati del receptionist
        success = self.receptionist.modifica_dipendente(new_data)
        if success:
            self.accept()
            if self.callback:
                self.callback()
        else:
            # Gestisci il caso in cui la modifica non sia riuscita
            # Mostra un messaggio di errore o fai altro in base alle tue esigenze
            pass
