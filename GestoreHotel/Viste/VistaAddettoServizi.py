from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from Attivita.AddettoServizi import AddettoServizi
from Viste.VistaModificaAddettoServizi import VistaModificaAddettoServizi


class VistaAddettoServizi(QWidget):
    def __init__(self, addetto_servizi, modifica_callback=None):
        super(VistaAddettoServizi, self).__init__()
        self.modifica_callback = modifica_callback
        self.addetto_servizi = addetto_servizi

        self.v_layout = QVBoxLayout()

        # Inizializza le etichette
        self.label_nome = QLabel("")
        self.label_codice = QLabel("")
        self.label_data_nascita = QLabel("")
        self.label_luogo_nascita = QLabel("")
        self.label_cellulare = QLabel("")
        self.label_password = QLabel("Password")

        self.imposta_stile_e_aggiungi_etichette()

        self.carica_dettagli_addetto_servizi()

        btn_modifica = QPushButton('MODIFICA')
        btn_modifica.clicked.connect(self.modifica_addetto_servizi)
        btn_modifica.setStyleSheet("""
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
        self.v_layout.addWidget(btn_modifica)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Addetto ai Servizi")
        self.setStyleSheet("background-color: #393535;")

    def imposta_stile_e_aggiungi_etichette(self):
        font_nome = self.label_nome.font()
        font_nome.setPointSize(14)
        self.label_nome.setFont(font_nome)

        etichette = [
            self.label_nome,
            self.label_codice,
            self.label_data_nascita,
            self.label_luogo_nascita,
            self.label_cellulare,
            self.label_password
        ]
        for etichetta in etichette:
            etichetta.setStyleSheet("color: white;")

        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addWidget(self.label_codice)
        self.v_layout.addWidget(self.label_data_nascita)
        self.v_layout.addWidget(self.label_luogo_nascita)
        self.v_layout.addWidget(self.label_cellulare)
        self.v_layout.addWidget(self.label_password)
        self.v_layout.addItem(QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def carica_dettagli_addetto_servizi(self):
        info = self.addetto_servizi.get_info_addetto_servizi() if isinstance(self.addetto_servizi, AddettoServizi) else {}
        nome_completo = f"Addetto {info.get('nome', '')} {info.get('cognome', '')}"
        self.label_nome.setText(nome_completo)
        self.label_codice.setText(f"Codice: {self.addetto_servizi.codice}")
        self.label_data_nascita.setText(f"Data di Nascita: {info.get('data_nascita', '')}")
        self.label_luogo_nascita.setText(f"Luogo di Nascita: {info.get('luogo_nascita', '')}")
        self.label_cellulare.setText(f"Cellulare: {info.get('cellulare', '')}")
        self.label_password.setText(f"Password: {self.addetto_servizi.password}")

    def modifica_addetto_servizi(self):
        vista_modifica = VistaModificaAddettoServizi(self.addetto_servizi, self.callback_congiunto, self)
        vista_modifica.exec_()

    def callback_congiunto(self):
        self.aggiorna_ui()
        if self.modifica_callback:
            self.modifica_callback()

    def ricarica_dati_addetto_servizi(self):
        addetto_servizi_aggiornato = self.addetto_servizi.ricerca_dipendente_codice(self.addetto_servizi.codice)
        if addetto_servizi_aggiornato:
            self.addetto_servizi = addetto_servizi_aggiornato
        else:
            pass

    def aggiorna_ui(self):
        self.ricarica_dati_addetto_servizi()
        self.carica_dettagli_addetto_servizi()