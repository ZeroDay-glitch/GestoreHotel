from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from Attivita.Receptionist import Receptionist
from Viste.VistaModificaReceptionist import VistaModificaReceptionist


class VistaReceptionist(QWidget):
    def __init__(self, receptionist, modifica_callback=None):
        super(VistaReceptionist, self).__init__()
        self.modifica_callback = modifica_callback
        self.receptionist = receptionist

        self.v_layout = QVBoxLayout()

        # Inizializza le etichette
        self.label_nome = QLabel("")
        self.label_codice = QLabel("")
        self.label_data_nascita = QLabel("")
        self.label_luogo_nascita = QLabel("")
        self.label_cellulare = QLabel("")
        self.label_lingue = QLabel("")

        self.imposta_stile_e_aggiungi_etichette()

        self.carica_dettagli_receptionist()

        btn_modifica = QPushButton('MODIFICA')
        btn_modifica.clicked.connect(self.modifica_receptionist)
        btn_modifica.setStyleSheet("""
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
        self.v_layout.addWidget(btn_modifica)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Receptionist")
        self.setStyleSheet("background-color: lightgreen;")

    def imposta_stile_e_aggiungi_etichette(self):
        font_nome = self.label_nome.font()
        font_nome.setPointSize(14)
        self.label_nome.setFont(font_nome)

        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addWidget(self.label_codice)
        self.v_layout.addWidget(self.label_data_nascita)
        self.v_layout.addWidget(self.label_luogo_nascita)
        self.v_layout.addWidget(self.label_cellulare)
        self.v_layout.addWidget(self.label_lingue)
        self.v_layout.addItem(QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def carica_dettagli_receptionist(self):
        info = self.receptionist.get_info_receptionist() if isinstance(self.receptionist, Receptionist) else {}
        nome_completo = f"Receptionist {info.get('nome', '')} {info.get('cognome', '')}"
        self.label_nome.setText(nome_completo)
        self.label_codice.setText(f"Codice: {self.receptionist.codice}")
        self.label_data_nascita.setText(f"Data di Nascita: {info.get('data_nascita', '')}")
        self.label_luogo_nascita.setText(f"Luogo di Nascita: {info.get('luogo_nascita', '')}")
        self.label_cellulare.setText(f"Cellulare: {info.get('cellulare', '')}")
        self.label_lingue.setText(f"Lingue: {', '.join(info.get('lingue', []))}")

    def modifica_receptionist(self):
        vista_modifica = VistaModificaReceptionist(self.receptionist, self.callback_congiunto, self)
        vista_modifica.exec_()

    def callback_congiunto(self):
        # Chiama prima il proprio metodo di aggiornamento
        self.aggiorna_ui()
        # Poi chiama il callback di VistaGestioneReceptionist, se esiste
        if self.modifica_callback:
            self.modifica_callback()
    def ricarica_dati_receptionist(self):

        receptionist_aggiornato = self.receptionist.ricerca_dipendente_codice(self.receptionist.codice)
        if receptionist_aggiornato:
            self.receptionist = receptionist_aggiornato
        else:
            # Gestisci l'errore se il receptionist non viene trovato (ad esempio, mostrando un messaggio)
            pass

    def aggiorna_ui(self):
        self.ricarica_dati_receptionist()  # Aggiorna i dati del receptionist
        self.carica_dettagli_receptionist()  # Aggiorna l'interfaccia utente con i nuovi dati
