from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from Attivita.Receptionist import Receptionist
from Viste.VistaModificaReceptionist import VistaModificaReceptionist   # Assicurati di importare la classe VistaModificaReceptionist

class VistaReceptionist(QWidget):
    def __init__(self, receptionist, modifica_callback=None):
        super(VistaReceptionist, self).__init__()
        self.modifica_callback = modifica_callback
        self.receptionist = receptionist

        v_layout = QVBoxLayout()
        nome = ""
        info = {}
        if isinstance(receptionist, Receptionist):
            info = receptionist.get_info_receptionist()
            nome = f"Receptionist {info['nome']} {info['cognome']}"
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(14)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        # Mostra altre informazioni del receptionist
        v_layout.addWidget(QLabel(f"Codice: {receptionist.codice}"))
        v_layout.addWidget(QLabel(f"Data di Nascita: {info['data_nascita']}"))
        v_layout.addWidget(QLabel(f"Luogo di Nascita: {info['luogo_nascita']}"))
        v_layout.addWidget(QLabel(f"Cellulare: {info['cellulare']}"))
        v_layout.addWidget(QLabel(f"Lingue: {', '.join(info['lingue'])}"))

        # Aggiungi altre informazioni specifiche del receptionist qui
        # Ad esempio, le prenotazioni o altre informazioni aggiuntive

        v_layout.addItem(QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Sostituisci il pulsante "Elimina" con un pulsante "Modifica"
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
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle("Receptionist")
        self.setStyleSheet("background-color: lightgreen;")

    def modifica_receptionist(self):
        vista_modifica = VistaModificaReceptionist(self.receptionist, self.modifica_callback, self)
        vista_modifica.exec_()