from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from Viste.VistaModificaCliente import VistaModificaCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.cliente = cliente
        self.setWindowTitle(f"Informazioni Cliente - {cliente.nome} {cliente.cognome}")

        main_layout = QVBoxLayout()

        # Layout per il nome e cognome
        header_layout = QVBoxLayout()
        header_label = QLabel(f"{cliente.nome} {cliente.cognome}")
        header_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        header_layout.addWidget(header_label)

        # Aggiungi dettagli cliente sotto il nome e cognome
        for key, value in cliente.getInfoCliente().items():
            if key not in ['Nome', 'Cognome']:
                label = QLabel(f"{key}: {value}")
                header_layout.addWidget(label)

        main_layout.addLayout(header_layout)

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
        # Aggiorna la UI dopo la modifica del cliente
        # Inserisci qui la logica per l'aggiornamento della UI
        pass

    