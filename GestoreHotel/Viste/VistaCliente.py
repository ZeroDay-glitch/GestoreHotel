from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from Attivita.Cliente import Cliente
from Viste.VistaModificaCliente import VistaModificaCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, modifica_callback=None):
        super(VistaCliente, self).__init__()
        self.modifica_callback = modifica_callback
        self.cliente = cliente

        self.v_layout = QVBoxLayout()

        # Inizializza le etichette
        self.label_nome = QLabel("")
        self.label_codice = QLabel("")
        self.label_data_nascita = QLabel("")
        self.label_luogo_nascita = QLabel("")
        self.label_cellulare = QLabel("")
        self.label_codice_fiscale = QLabel("")
        self.label_documento = QLabel("")
        self.label_email = QLabel("")
        self.label_note = QLabel("")

        self.imposta_stile_e_aggiungi_etichette()

        self.carica_dettagli_cliente()

        btn_modifica = QPushButton('MODIFICA')
        btn_modifica.clicked.connect(self.modifica_cliente)
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
        self.setWindowTitle("Cliente")
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
        self.v_layout.addWidget(self.label_codice_fiscale)
        self.v_layout.addWidget(self.label_documento)
        self.v_layout.addWidget(self.label_email)
        self.v_layout.addWidget(self.label_note)
        self.v_layout.addItem(QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def carica_dettagli_cliente(self):
        info = self.cliente.get_info_cliente() if isinstance(self.cliente, Cliente) else {}
        nome_completo = f"Cliente {info.get('nome', '')} {info.get('cognome', '')}"
        self.label_nome.setText(nome_completo)
        self.label_codice.setText(f"Codice: {self.cliente.codice}")
        self.label_data_nascita.setText(f"Data di Nascita: {info.get('data_nascita', '')}")
        self.label_luogo_nascita.setText(f"Luogo di Nascita: {info.get('luogo_nascita', '')}")
        self.label_cellulare.setText(f"Cellulare: {info.get('cellulare', '')}")
        self.label_codice_fiscale.setText(f"Codice Fiscale: {info.get('codice_fiscale', '')}")
        self.label_documento.setText(f"Documento: {info.get('documento', '')}")
        self.label_email.setText(f"Email: {info.get('email', '')}")
        self.label_note.setText(f"Note: {info.get('note', '')}")

    def modifica_cliente(self):
        vista_modifica = VistaModificaCliente(self.cliente, self.callback_congiunto, self)
        vista_modifica.exec_()

    def callback_congiunto(self):
        # Chiama prima il proprio metodo di aggiornamento
        self.aggiorna_ui()
        # Poi chiama il callback di VistaGestioneCliente, se esiste
        if self.modifica_callback:
            self.modifica_callback()

    def ricarica_dati_cliente(self):
        cliente_aggiornato = self.cliente.ricerca_cliente_codice(self.cliente.codice)
        if cliente_aggiornato:
            self.cliente = cliente_aggiornato
        else:
            # Gestisci l'errore se il cliente non viene trovato (ad esempio, mostrando un messaggio)
            pass

    def aggiorna_ui(self):
        self.ricarica_dati_cliente()  # Aggiorna i dati del cliente
        self.carica_dettagli_cliente()  # Aggiorna l'interfaccia utente con i nuovi dati
