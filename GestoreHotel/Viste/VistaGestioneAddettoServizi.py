import os
import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QListView, QSpacerItem, QLabel, QMessageBox, \
    QLineEdit

from Viste.VistaAddettoServizi import VistaAddettoServizi
from Viste.VistaAggiungiAddettoServizi import VistaAggiungiAddettoServizi


class VistaGestioneAddettoServizi(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneAddettoServizi, self).__init__(parent)
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.get_generic_button("AGGIUNGI", lambda: self.aggiungi_addetto_servizi(self.update_ui), 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_addetto_servizi, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_addetto_servizi, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = QLabel("Lista Addetti ai Servizi:")
        label.setStyleSheet("QLabel { color : white; }")
        self.layout.addWidget(label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cerca addetto ai servizi...")
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

        self.lista_addetto_servizi = QListView()
        self.layout.addWidget(self.lista_addetto_servizi)
        self.update_ui()

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Addetti ai Servizi")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #393535;")

    def load_addetti_servizi(self):
        if os.path.isfile('Dati/AddettoServizi.pickle'):
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.addetti_servizi = list(current.values())

    def update_ui(self):
        self.load_addetti_servizi()
        search_text = self.search_bar.text().lower()
        filtered_addetti_servizi = [addetto_servizi for addetto_servizi in self.addetti_servizi if
                                    search_text in addetto_servizi.nome.lower() or search_text in addetto_servizi.cognome.lower()]

        listview_model = QStandardItemModel(self.lista_addetto_servizi)
        for addetto_servizi in filtered_addetti_servizi:
            item = QStandardItem()
            item.setText(f"{addetto_servizi.nome} {addetto_servizi.cognome}")
            item.setEditable(False)

            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            item.setForeground(Qt.white)
            listview_model.appendRow(item)
        self.lista_addetto_servizi.setModel(listview_model)

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

    def aggiungi_addetto_servizi(self, callback=None):
        self.vista_aggiungi_addetto_servizi = VistaAggiungiAddettoServizi(callback=self.update_ui)
        self.vista_aggiungi_addetto_servizi.show()

    def apri_addetto_servizi(self):
        try:
            selected_index = self.lista_addetto_servizi.selectedIndexes()[0]
            if selected_index.isValid():
                selected_addetto_servizi = self.addetti_servizi[selected_index.row()]
                self.vista_addetto_servizi = VistaAddettoServizi(selected_addetto_servizi, modifica_callback=self.update_ui)
                self.vista_addetto_servizi.show()
        except IndexError:
            print("INDEX ERROR")

    def rimuovi_addetto_servizi(self):
        selected_indexes = self.lista_addetto_servizi.selectedIndexes()

        if not selected_indexes:
            QMessageBox.critical(self, 'Errore', 'Seleziona un addetto ai servizi da rimuovere', QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        selected_index = selected_indexes[0]
        selected_addetto_servizi = self.addetti_servizi[selected_index.row()]

        if selected_addetto_servizi:
            success = selected_addetto_servizi.rimuovi_dipendente()
            if success:
                self.update_ui()
            else:
                QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere l\'addetto ai servizi.', QMessageBox.Ok,
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', 'Addetto ai servizi non trovato.', QMessageBox.Ok, QMessageBox.Ok)
