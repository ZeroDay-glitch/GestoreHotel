import pickle
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy

from Attivita.Camera import Camera
from Viste.VistaCamere import VistaCamere


class VistaGestioneCamere(QWidget):
    def __init__(self):
        super().__init__()
        self.camere = Camera.carica_camere()
        if not self.camere:
            self.camere = Camera.crea_camere()

        self.pulsanti_camera = {}

        self.layout = QGridLayout()
        self.init_ui()
        self.setLayout(self.layout)
        self.setWindowTitle("Gestione Camere")
        self.setStyleSheet("background-color: #393535;")

    def init_ui(self):
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
                tipo_label.setStyleSheet("""
                    QLabel {
                        font-size: 20px; 
                        font-weight: bold; 
                        color: white; 
                    }
                """)
                self.layout.addWidget(tipo_label, riga, 0, 1, 5)
                riga += 1
                colonna = 0
                for numero_camera, camera in camere:
                    button = QPushButton(f"Camera {numero_camera}")
                    button.setStyleSheet(self.get_stile_camera(camera))
                    button.clicked.connect(self.handle_camera_clicked(camera))
                    self.layout.addWidget(button, riga, colonna)

                    colonna += 1
                    if colonna == 5:
                        colonna = 0
                        riga += 1
                    self.pulsanti_camera[numero_camera] = button
                riga += 1

    def handle_camera_clicked(self, camera):
        def on_button_clicked():
            vista_camera = VistaCamere(camera)
            vista_camera.exec_()
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

        if camera.verifica_disponibilita():
            base_color = "green"
            hover_color = "darkgreen"
        else:
            base_color = "red"
            hover_color = "darkred"

        return base_style.format(base_color=base_color, hover_color=hover_color)