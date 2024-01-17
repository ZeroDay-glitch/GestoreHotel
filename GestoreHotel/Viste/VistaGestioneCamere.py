import pickle
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

from Attivita.Camera import Camera


class VistaGestioneCamere(QWidget):
    def __init__(self):
        super().__init__()

        # Carica le camere dal file o crea un esempio se il file non esiste
        self.camere = self.carica_o_crea_camere()

        # Layout principale
        self.layout = QGridLayout()

        # Raggruppa le camere per tipo
        camere_per_tipo = {
            "Standard": [],
            "Premium": [],
            "Suite Deluxe": []
        }
        for numero_camera, camera in self.camere.items():
            tipo = camera.tipo_camera  # Assumi che tipo_camera sia una stringa come "Standard", "Premium" o "Suite Deluxe"
            if tipo in camere_per_tipo:
                camere_per_tipo[tipo].append((numero_camera, camera))
            else:
                camere_per_tipo[tipo] = [(numero_camera, camera)]

        riga = 0
        for tipo, camere in camere_per_tipo.items():
            if camere:  # Se ci sono camere di questo tipo
                # Aggiungi un mini titolo per il tipo di camera
                tipo_label = QLabel(tipo)
                tipo_label.setAlignment(Qt.AlignCenter)
                tipo_label.setStyleSheet("font-size: 20px; font-weight: bold;")
                self.layout.addWidget(tipo_label, riga, 0, 1, 5)
                riga += 1  # Incrementa la riga per i pulsanti delle camere

                # Aggiungi i pulsanti per le camere di questo tipo
                colonna = 0
                for numero_camera, camera in camere:
                    button = QPushButton(f"Camera {numero_camera}")
                    button.setStyleSheet(self.get_stile_camera(camera))
                    button.clicked.connect(lambda _, nc=numero_camera: self.handle_camera_clicked(nc))
                    self.layout.addWidget(button, riga, colonna)

                    colonna += 1
                    if colonna == 5:  # Resetta la colonna e vai alla riga successiva dopo 5 pulsanti
                        colonna = 0
                        riga += 1
                riga += 1  # Incrementa la riga per il prossimo tipo di camera

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Camere")
        self.setStyleSheet("background-color: lightgreen;")

    def carica_o_crea_camere(self):
        file_path = 'Dati/Camere.pickle'
        camere = {}

        # Carica le camere esistenti dal file, se il file esiste
        if QFile.exists(file_path):
            with open(file_path, 'rb') as f:
                camere = pickle.load(f)
        # Creazione camere
        camere = {
            101: Camera(101, "Standard", 1, 100),
            102: Camera(102, "Standard", 2, 150),
            103: Camera(103, "Premium", 3, 200),
            104: Camera(104, "Suite Deluxe", 1, 100),
            105: Camera(105, "Standard", 2, 150),
            106: Camera(106, "Premium", 3, 200),
            107: Camera(107, "Standard", 1, 100),
            108: Camera(108, "Suite Deluxe", 2, 150),
            109: Camera(109, "Premium", 3, 200),
            201: Camera(201, "Premium", 1, 100),
            202: Camera(202, "Premium", 2, 150),
            203: Camera(203, "Standard", 3, 200),
            204: Camera(204, "Suite Deluxe", 1, 100),
            205: Camera(205, "Standard", 2, 150),
            206: Camera(206, "Premium", 3, 200),
            207: Camera(207, "Suite Deluxe", 1, 100),
            208: Camera(208, "Standard", 2, 150),
            209: Camera(209, "Premium", 3, 200),
        }

        # Aggiungi le nuove camere se non sono già presenti
        for numero, nuova_camera in camere.items():
            if numero not in camere:
                camere[numero] = nuova_camera

        # Salva le camere aggiornate nel file
        with open(file_path, 'wb') as f:
            pickle.dump(camere, f, pickle.HIGHEST_PROTOCOL)

        return camere

    def handle_camera_clicked(self, numero_camera):
        # Questa funzione gestisce il clic su un pulsante camera
        def on_button_clicked():
            camera = self.camere[numero_camera]
            if camera.stato_camera == "disponibile":
                # Assumi che una prenotazione sia associata quando la camera viene contrassegnata come "occupata"
                camera.modifica_stato_camera("occupata")
                camera.prenotazione = "Prenotazione123"  # Sostituisci con l'oggetto prenotazione effettivo
            else:
                camera.modifica_stato_camera("disponibile")
                camera.prenotazione = None

            # Aggiorna lo stile del pulsante
            button = self.findChild(QPushButton, f"Camera {numero_camera}")
            button.setStyleSheet(self.get_stile_camera(camera))

            # Dopo aver apportato modifiche, salva le camere nel file
            self.salva_camere()

        return on_button_clicked

    def get_stile_camera(self, camera):
        # Stile di base per i pulsanti
        base_style = """
            QPushButton {{
                background-color: {base_color};
                color: black;
                border-radius: 10px;
                border: 1px solid #555;
                padding: 5px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
                color: white;
            }}
        """

        # Imposta i colori in base allo stato della camera
        if camera.stato_camera == "disponibile":
            base_color = "green"
            hover_color = "darkgreen"
        else:
            base_color = "red"
            hover_color = "darkred"

        # Restituisce lo stile con i colori impostati
        return base_style.format(base_color=base_color, hover_color=hover_color)

    def salva_camere(self):
        file_path = 'Dati/Camere.pickle'
        with open(file_path, 'wb') as f:
            pickle.dump(self.camere, f, pickle.HIGHEST_PROTOCOL)