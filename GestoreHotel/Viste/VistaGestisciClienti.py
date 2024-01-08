import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox

from Viste.VistaCliente import VistaCliente
from Viste.VistaInserisciCliente import VistaInserisciCliente


class VistaGestisciClienti(QWidget):

    def __init__(self, callback=None, parent=None):
        super(VistaGestisciClienti, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)

        delete_button = QPushButton("Elimina")
        delete_button.clicked.connect(self.show_delete)
        buttons_layout.addWidget(delete_button)

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Clienti")

        self.vista_cliente = None

    def load_clienti(self):
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.pickle", "rb") as f:
                current = dict(pickle.load(f))
                self.clienti.extend(current.values())

    def update_ui(self, nuovo_cliente = None):
        self.clienti = []
        self.load_clienti()
        listview_model = QStandardItemModel(self.list_view)
        for cliente in self.clienti:
            item = QStandardItem()
            nome = f"{cliente.nome} {cliente.cognome} - {type(cliente).__name__}{cliente.codice}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    def show_selected_info(self):
        # Ottieni l'elemento selezionato nella lista
        selected_item = self.list_view.selectedIndexes()

        if not selected_item:
            # Nessun elemento selezionato
            return

        # Estrai l'indice dell'elemento selezionato
        index = selected_item[0].row()

        # Ottieni il cliente corrispondente all'indice
        cliente_selezionato = self.clienti[index]

        # Verifica se l'istanza di VistaCliente è già aperta
        if self.vista_cliente is None or not self.vista_cliente.isVisible():
            # Apri la VistaCliente solo se non è già aperta
            self.vista_cliente = VistaCliente(cliente_selezionato)
            self.vista_cliente.show()

    def show_new(self):
        self.inserisci_cliente = VistaInserisciCliente(callback=self.update_ui)
        self.inserisci_cliente.show()

    def show_delete(self):
        # Ottieni l'elemento selezionato nella lista
        selected_item = self.list_view.selectedIndexes()

        if not selected_item:
            # Nessun elemento selezionato
            return

        # Estrai l'indice dell'elemento selezionato
        index = selected_item[0].row()

        # Ottieni il cliente corrispondente all'indice
        cliente_selezionato = self.clienti[index]

        # Chiedi conferma prima di eliminare il cliente
        conferma = QMessageBox.question(self, "Conferma eliminazione",
                                        f"Sei sicuro di voler eliminare il cliente {cliente_selezionato.nome} "
                                        f"{cliente_selezionato.cognome}?", QMessageBox.Yes | QMessageBox.No)

        if conferma == QMessageBox.Yes:
            # Prova a rimuovere il cliente
            cliente_selezionato.rimuoviCliente()

            # Aggiorna l'interfaccia utente dopo l'eliminazione
            self.update_ui()