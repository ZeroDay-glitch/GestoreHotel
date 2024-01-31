import os
import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QLabel, QListView, \
    QMessageBox, QLineEdit

from Viste.VistaAggiungiReceptionist import VistaAggiungiReceptionist
from Viste.VistaReceptionist import VistaReceptionist


class VistaGestioneReceptionist(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneReceptionist, self).__init__(parent)
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.get_generic_button("AGGIUNGI", lambda: self.aggiungi_receptionist(self.update_ui), 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_receptionist, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_receptionist, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = QLabel("Lista Receptionist:")
        label.setStyleSheet("QLabel { color : white; }")
        self.layout.addWidget(label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cerca receptionist...")
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

        self.lista_receptionist = QListView()
        self.layout.addWidget(self.lista_receptionist)
        self.update_ui()

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Receptionist")
        self.resize(400, 300)
        self.setStyleSheet("background-color: #393535;")

    def load_receptionists(self):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.receptionists = list(current.values())

    def update_ui(self):
        self.load_receptionists()
        search_text = self.search_bar.text().lower()
        filtered_receptionists = [receptionist for receptionist in self.receptionists if
                                  search_text in receptionist.nome.lower() or search_text in receptionist.cognome.lower()]

        listview_model = QStandardItemModel(self.lista_receptionist)
        for receptionist in filtered_receptionists:
            item = QStandardItem()
            item.setText(f"{receptionist.nome} {receptionist.cognome}")
            item.setEditable(False)

            font = item.font()
            font.setPointSize(10)
            item.setFont(font)
            item.setForeground(Qt.white)

            listview_model.appendRow(item)
        self.lista_receptionist.setModel(listview_model)

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

    def aggiungi_receptionist(self, callback=None):
        self.vista_aggiungi_receptionist = VistaAggiungiReceptionist(callback=self.update_ui)
        self.vista_aggiungi_receptionist.show()

    def apri_receptionist(self):
        try:
            selected_index = self.lista_receptionist.selectedIndexes()[0]
            if selected_index.isValid():
                selected_receptionist = self.receptionists[selected_index.row()]
                self.vista_receptionist = VistaReceptionist(selected_receptionist, modifica_callback=self.update_ui)
                self.vista_receptionist.show()
        except IndexError:
            print("INDEX ERROR")

    def rimuovi_receptionist(self):
        selected_indexes = self.lista_receptionist.selectedIndexes()

        if not selected_indexes:
            QMessageBox.critical(self, 'Errore', 'Seleziona un receptionist da rimuovere', QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        selected_index = selected_indexes[0]
        selected_receptionist = self.receptionists[selected_index.row()]

        if selected_receptionist:
            success = selected_receptionist.rimuovi_dipendente()
            if success:
                self.update_ui()
            else:
                QMessageBox.critical(self, 'Errore', 'Impossibile rimuovere il receptionist.', QMessageBox.Ok,
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', 'Receptionist non trovato.', QMessageBox.Ok, QMessageBox.Ok)
