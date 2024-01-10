from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestisciClienti import VistaGestisciClienti
from Viste.VistaGestisciPrenotazione import VistaGestisciPrenotazione


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self.get_generic_button("gestisci Servizi", self.go_servizi), 0, 0)
        grid_layout.addWidget(self.get_generic_button("gestisci Clienti", self.go_clienti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("gestisci Dipendenti", self.go_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("gestisci Prenotazioni", self.go_prenotazioni), 1, 1)
        grid_layout.addWidget(self.get_generic_button("gestisci Sistema", self.go_sistema), 2, 0)
        grid_layout.addWidget(self.get_generic_button("gestisci Camere", self.go_camere), 2, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Hotel")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo, self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_servizi(self):
        pass

    def go_clienti(self):
        self.vista_gestisci_clienti = VistaGestisciClienti()
        self.vista_gestisci_clienti.show()

    def go_dipendenti(self):
        pass

    def go_prenotazioni(self):
        self.vista_gestisci_prenotazioni = VistaGestisciPrenotazione()
        self.vista_gestisci_prenotazioni.show()

    def go_sistema(self):
        pass

    def go_camere(self):
        pass