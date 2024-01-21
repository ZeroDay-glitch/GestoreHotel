import pickle
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

from Attivita.Camera import Camera


class VistaGestioneCamere(QWidget):
    def __init__(self):
        super().__init__()

        self.camere = self.carica_o_crea_camere()

        self.layout = QGridLayout()

        camere_per_tipo = {
            "Standard": [],
            "Premium": [],
            "Suite Deluxe": []
        }
        for numero_camera, camera in self.camere.items():
            tipo = camera.tipo_camera
            if tipo in camere_per_tipo:
                camere_per_tipo[tipo].append((numero_camera, camera))
            else:
                camere_per_tipo[tipo] = [(numero_camera, camera)]

        riga = 0
        for tipo, camere in camere_per_tipo.items():
            if camere:
                tipo_label = QLabel(tipo)
                tipo_label.setAlignment(Qt.AlignCenter)
                tipo_label.setStyleSheet("font-size: 20px; font-weight: bold;")
                self.layout.addWidget(tipo_label, riga, 0, 1, 5)
                riga += 1
                colonna = 0
                for numero_camera, camera in camere:
                    button = QPushButton(f"Camera {numero_camera}")
                    button.setStyleSheet(self.get_stile_camera(camera))
                    button.clicked.connect(lambda _, nc=numero_camera: self.handle_camera_clicked(nc))
                    self.layout.addWidget(button, riga, colonna)

                    colonna += 1
                    if colonna == 5:
                        colonna = 0
                        riga += 1
                riga += 1

        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Camere")
        self.setStyleSheet("background-color: #393535;")

    def carica_o_crea_camere(self):
        file_path = 'Dati/Camere.pickle'
        camere = {}

        if QFile.exists(file_path):
            with open(file_path, 'rb') as f:
                camere = pickle.load(f)
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

        for numero, nuova_camera in camere.items():
            if numero not in camere:
                camere[numero] = nuova_camera

        with open(file_path, 'wb') as f:
            pickle.dump(camere, f, pickle.HIGHEST_PROTOCOL)

        return camere

    def handle_camera_clicked(self, numero_camera):
        def on_button_clicked():
            camera = self.camere[numero_camera]
            if camera.stato_camera == "disponibile":
                camera.modifica_stato_camera("occupata")
                camera.prenotazione = "Prenotazione123"
            else:
                camera.modifica_stato_camera("disponibile")
                camera.prenotazione = None

            button = self.findChild(QPushButton, f"Camera {numero_camera}")
            button.setStyleSheet(self.get_stile_camera(camera))

            self.salva_camere()

        return on_button_clicked

    def get_stile_camera(self, camera):
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

        if camera.stato_camera == "disponibile":
            base_color = "green"
            hover_color = "darkgreen"
        else:
            base_color = "red"
            hover_color = "darkred"

        return base_style.format(base_color=base_color, hover_color=hover_color)

    def salva_camere(self):
        file_path = 'Dati/Camere.pickle'
        with open(file_path, 'wb') as f:
            pickle.dump(self.camere, f, pickle.HIGHEST_PROTOCOL)
