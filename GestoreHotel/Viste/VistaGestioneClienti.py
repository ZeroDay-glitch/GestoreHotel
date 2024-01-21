import os
import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QListView, QMessageBox, \
    QLineEdit

from Viste.VistaAggiungiCliente import VistaAggiungiCliente
from Viste.VistaCliente import VistaCliente


class VistaGestioneClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneClienti, self).__init__(parent)
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.get_generic_button("AGGIUNGI", lambda: self.aggiungi_cliente(self.update_ui), 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_cliente, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_cliente, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = QLabel("Lista Clienti:")
        label.setStyleSheet("QLabel { color : white; }")
        self.layout.addWidget(label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cerca cliente...")
        self.search_bar.textChanged.connect(self.update_ui)
        self.search_bar.setStyleSheet("""
                    QLineEdit {
                        color: white;
                        background-color: #555;
                        border: 2px solid #555;
                        border-radius: 10px;
                        padding: 5px;
                    }
                    QLineEdit:focus {
                        border: 2px solid #aaa;
                    }
                """)
        self.layout.addWidget(self.search_bar)

        self.lista_cliente = QListView()
        self.layout.addWidget(self.lista_cliente)
        self.update_ui()

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Clienti")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #393535;")

    def load_clienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.clienti = list(current.values())

    def update_ui(self):
        self.load_clienti()
        search_text = self.search_bar.text().lower()
        filtered_clienti = [cliente for cliente in self.clienti if
                            search_text in cliente.nome.lower() or search_text in cliente.cognome.lower()]

        listview_model = QStandardItemModel(self.lista_cliente)
        for cliente in filtered_clienti:
            item = QStandardItem()
            item.setText(f"{cliente.nome} {cliente.cognome}")
            item.setEditable(False)


            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            item.setForeground(Qt.white)

            listview_model.appendRow(item)
        self.lista_cliente.setModel(listview_model)

    def get_generic_button(self, titolo, on_click, font_size=None):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)

        if font_size is not None:
            font = QFont()
            font.setPointSize(font_size)
            button.setFont(font)

        button.setStyleSheet("""
            QPushButton {
                background-color: #C3D4C7;
                color: black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #707070;
                color: white;
            }
        """)

        return button

    def aggiungi_cliente(self, callback=None):
        self.vista_aggiungi_cliente = VistaAggiungiCliente(callback=self.update_ui)
        self.vista_aggiungi_cliente.show()

    def apri_cliente(self):
        try:
            selected_index = self.lista_cliente.selectedIndexes()[0]
            if selected_index.isValid():
                selected_cliente = self.clienti[selected_index.row()]
                self.vista_apri_cliente = VistaCliente(selected_cliente, modifica_callback=self.update_ui)
                self.vista_apri_cliente.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Nessun cliente selezionato.', QMessageBox.Ok, QMessageBox.Ok)

    def rimuovi_cliente(self):
        selected_index = self.lista_cliente.selectedIndexes()[0]

        if selected_index.isValid():
            selected_cliente = self.clienti[selected_index.row()]

            if selected_cliente:
                if selected_cliente.rimuovi_cliente():
                    self.update_ui()
                else:
                    QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere il cliente.', QMessageBox.Ok,
                                         QMessageBox.Ok)