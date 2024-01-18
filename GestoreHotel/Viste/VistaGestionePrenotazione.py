import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel, QListView, QPushButton, QMessageBox

from Viste.VistaAggiungiPrenotazione import VistaAggiungiPrenotazione
from Attivita.Cliente import Cliente  # Assicurati di importare la classe Cliente da dove si trova
from Viste.VistaPrenotazioni import VistaPrenotazione


class VistaGestionePrenotazione(QWidget):

    def __init__(self, parent=None):
        super(VistaGestionePrenotazione, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.servizi = {}
        self.clienti = {}  # Aggiungi un dizionario per i clienti
        self.load_clienti()  # Carica i clienti
        self.layout.addWidget(self.get_generic_button("AGGIUNGI", self.aggiungi_prenotazione, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("APRI", self.apri_prenotazione, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.get_generic_button("RIMUOVI", self.rimuovi_prenotazione, 12))
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Etichetta per separare i pulsanti dalla lista
        label = QLabel("Lista Prenotazioni")
        self.layout.addWidget(label)

        self.lista_prenotazione = QListView()
        self.layout.addWidget(self.lista_prenotazione)
        self.update_ui()

        # Spazio vuoto per distanziare
        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Pulsante "Annulla" per tornare indietro
        self.layout.addWidget(self.get_generic_button("Annulla", self.close, 12))

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Prenotazioni")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightgreen;")

    def load_clienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                self.clienti = dict(pickle.load(f))

    def update_ui(self):
        listview_model = QStandardItemModel(self.lista_prenotazione)

        # Carica le prenotazioni
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

            for codice, prenotazione in prenotazioni.items():
                item = QStandardItem(
                    f"Cliente: {prenotazione.cliente.nome} {prenotazione.cliente.cognome} - Codice: {codice}")
                item.setEditable(False)
                item.setData(codice)  # Qui assicurati che 'codice' sia solo il numero, senza ulteriori informazioni
                listview_model.appendRow(item)

            self.lista_prenotazione.setModel(listview_model)

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
                background-color: white;
                color: black;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkgreen;
                color: white;
            }
        """)

        return button

    def aggiungi_prenotazione(self):
        self.vista_aggiungi_prenotazione = VistaAggiungiPrenotazione(self.clienti, self.servizi, callback=self.update_ui)
        self.vista_aggiungi_prenotazione.show()

    def apri_prenotazione(self):
        selected_indexes = self.lista_prenotazione.selectedIndexes()

        if not selected_indexes:
            QMessageBox.critical(self, 'Errore', 'Seleziona una prenotazione da aprire', QMessageBox.Ok, QMessageBox.Ok)
            return

        selected_index = selected_indexes[0]
        codice_prenotazione = self.extract_code(selected_index.data())  # Estrai il codice dalla stringa

        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

            if codice_prenotazione in prenotazioni:
                prenotazione_selezionata = prenotazioni[codice_prenotazione]
                self.vista_prenotazione = VistaPrenotazione(prenotazione_selezionata)
                self.vista_prenotazione.show()
            else:
                QMessageBox.critical(self, 'Errore', 'Prenotazione non trovata', QMessageBox.Ok, QMessageBox.Ok)

    def rimuovi_prenotazione(self):
        selected_indexes = self.lista_prenotazione.selectedIndexes()

        if not selected_indexes:
            QMessageBox.critical(self, 'Errore', 'Seleziona una prenotazione da rimuovere', QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        selected_index = selected_indexes[0]
        full_text = selected_index.data()  # Questo contiene il testo completo
        codice_prenotazione = self.extract_code(full_text)  # Estrai il codice dalla stringa

        print("ID prenotazione selezionato:", codice_prenotazione)

        # Chiedi conferma prima di procedere con la rimozione
        confirm = QMessageBox.question(self, 'Conferma rimozione',
                                       f'Sei sicuro di voler rimuovere la prenotazione con codice {codice_prenotazione}?',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # Carica le prenotazioni, rimuovi quella selezionata, e salva di nuovo
            if os.path.isfile('Dati/Prenotazioni.pickle'):
                with open('Dati/Prenotazioni.pickle', 'rb') as f:
                    prenotazioni = pickle.load(f)

                if codice_prenotazione in prenotazioni:
                    del prenotazioni[codice_prenotazione]

                    with open('Dati/Prenotazioni.pickle', 'wb') as f:
                        pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

                    self.update_ui()  # Aggiorna la lista delle prenotazioni
                    QMessageBox.information(self, 'Operazione completata', 'Prenotazione rimossa con successo',
                                            QMessageBox.Ok, QMessageBox.Ok)
                else:
                    print("Prenotazioni disponibili:", prenotazioni.keys())
                    QMessageBox.critical(self, 'Errore', 'Prenotazione non trovata', QMessageBox.Ok, QMessageBox.Ok)

    def extract_code(self, full_text):
        try:
            # Supponiamo che il codice sia sempre alla fine e preceduto da ': '
            codice_str = full_text.split(': ')[-1]
            return int(codice_str)  # Converti il codice in int
        except (ValueError, IndexError) as e:
            print("Errore durante l'estrazione del codice:", e)
            return None