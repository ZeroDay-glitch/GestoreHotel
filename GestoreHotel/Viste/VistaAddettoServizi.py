from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Attivita.AddettoServizi import AddettoServizi


class VistaAddettoServizi(QWidget):
    def __init__(self, addetto_servizi, modifica_callback=None):
        super(VistaAddettoServizi, self).__init__()
        self.modifica_callback = modifica_callback
        self.addetto_servizi = addetto_servizi

        v_layout = QVBoxLayout()
        nome = ""
        info = {}
        if isinstance(addetto_servizi, AddettoServizi):
            info = addetto_servizi.get_info_addetto_servizi()
            nome = f"Addetto {info['nome']} {info['cognome']}"
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(14)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addWidget(QLabel(f"Codice: {addetto_servizi.codice}"))
        v_layout.addWidget(QLabel(f"Data di Nascita: {info['data_nascita']}"))
        v_layout.addWidget(QLabel(f"Luogo di Nascita: {info['luogo_nascita']}"))
        v_layout.addWidget(QLabel(f"Cellulare: {info['cellulare']}"))

        v_layout.addItem(QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_modifica = QPushButton('MODIFICA')
        btn_modifica.clicked.connect(self.modifica_addetto_servizi)
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
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle("Addetto ai Servizi")
        self.setStyleSheet("background-color: lightgreen;")

    def modifica_addetto_servizi(self):
        vista_modifica = VistaModificaAddettoServizi(self.addetto_servizi, self.modifica_callback, self)
        vista_modifica.exec_()
