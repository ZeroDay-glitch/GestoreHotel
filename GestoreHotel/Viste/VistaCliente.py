from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from Viste.VistaModificaCliente import VistaModificaCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.cliente = cliente
        self.setWindowTitle(f"Informazioni Cliente - {cliente.nome} {cliente.cognome}")

        main_layout = QVBoxLayout()

        # Crea l'header_layout come attributo dell'istanza
        self.header_layout = QVBoxLayout()  # Aggiunta chiave qui

        header_label = QLabel(f"{cliente.nome} {cliente.cognome}")
        header_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        self.header_layout.addWidget(header_label)

        # Aggiungi dettagli cliente sotto il nome e cognome
        for key, value in cliente.getInfoCliente().items():
            if key not in ['Nome', 'Cognome']:
                if key == 'prenotato':
                    value = "Sì" if value else "No"
                label = QLabel(f"{key}: {value}")
                self.header_layout.addWidget(label)

        main_layout.addLayout(self.header_layout)

        # Layout per i pulsanti
        buttons_layout = QHBoxLayout()
        btn_modifica = QPushButton("Modifica")
        btn_modifica.clicked.connect(self.show_modifica)
        buttons_layout.addWidget(btn_modifica)

        btn_chiudi = QPushButton("Chiudi")
        btn_chiudi.clicked.connect(self.close)
        buttons_layout.addWidget(btn_chiudi)

        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        self.vista_modifica_cliente = None

    def show_modifica(self):
        if self.vista_modifica_cliente is None or not self.vista_modifica_cliente.isVisible():
            self.vista_modifica_cliente = VistaModificaCliente(self.cliente, self.update_ui)
            self.vista_modifica_cliente.show()

    def update_ui(self):
        # Rimuove tutti i widget esistenti nel layout contenente i dettagli del cliente
        for i in reversed(range(self.header_layout.count())):
            self.header_layout.itemAt(i).widget().setParent(None)

        # Aggiorna il titolo della finestra con il nome e cognome aggiornati
        self.setWindowTitle(f"Informazioni Cliente - {self.cliente.nome} {self.cliente.cognome}")

        # Aggiorna il layout con i nuovi dettagli del cliente
        header_label = QLabel(f"{self.cliente.nome} {self.cliente.cognome}")
        header_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        self.header_layout.addWidget(header_label)

        for key, value in self.cliente.getInfoCliente().items():
            if key not in ['Nome', 'Cognome']:
                if key == 'prenotato':
                    value = "Sì" if value else "No"
                label = QLabel(f"{key}: {value}")
                self.header_layout.addWidget(label)
