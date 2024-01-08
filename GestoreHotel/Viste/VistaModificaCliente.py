import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
import pickle
import os

class VistaModificaCliente(QWidget):
    def __init__(self, cliente, callback, parent=None):
        super(VistaModificaCliente, self).__init__(parent)
        self.cliente = cliente
        self.callback = callback
        self.valori_originali = cliente.getInfoCliente().copy()
        self.setWindowTitle(f"Modifica Cliente - {cliente.nome} {cliente.cognome}")

        layout = QVBoxLayout()

        for key, value in self.valori_originali.items():
            if key not in ['Nome', 'Cognome', 'Lista Prenotazioni']:
                label = QLabel(f"{key}:")
                layout.addWidget(label)

                if key == "documentoValido":
                    # Crea un QComboBox per il campo documentoValido
                    combo_box = QComboBox()
                    combo_box.addItems(["Carta d'identità", "Patente"])
                    combo_box.setCurrentText(str(value))
                    layout.addWidget(combo_box)
                    setattr(self, f"{key}_edit", combo_box)
                else:
                    # Crea un QLineEdit per gli altri campi
                    edit_line = QLineEdit(str(value))
                    layout.addWidget(edit_line)
                    setattr(self, f"{key}_edit", edit_line)

        btn_conferma = QPushButton("Conferma Modifiche")
        btn_conferma.clicked.connect(self.conferma_modifiche)
        layout.addWidget(btn_conferma)

        self.setLayout(layout)

    def conferma_modifiche(self):
        try:
            for key, value in self.valori_originali.items():
                if key not in ['Nome', 'Cognome', 'Lista Prenotazioni']:
                    widget = getattr(self, f"{key}_edit")
                    if isinstance(widget, QComboBox):
                        new_value = widget.currentText()  # Usa currentText per QComboBox
                    else:
                        new_value = widget.text()  # Usa text per QLineEdit

                    # Conversione dei tipi di valore, se necessario
                    if isinstance(value, int):
                        setattr(self.cliente, key, int(new_value))
                    elif isinstance(value, datetime.datetime):
                        if new_value < value.strftime("%Y-%m-%d %H:%M:%S"):
                            raise ValueError("La nuova data deve essere maggiore della data originale.")
                        setattr(self.cliente, key, datetime.datetime.strptime(new_value, "%Y-%m-%d %H:%M:%S"))
                    else:
                        setattr(self.cliente, key, new_value)

            self.cliente.modificaCliente()
            self.close()
            self.callback()

        except ValueError as e:
            QMessageBox.critical(self, "Errore", str(e), QMessageBox.Ok, QMessageBox.Ok)



