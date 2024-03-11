from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class VistaCamere(QDialog):
    def __init__(self, camera, parent=None):
        super(VistaCamere, self).__init__(parent)
        self.camera = camera

        self.layout = QVBoxLayout()

        self.label_numero_camera = QLabel(f"Numero Camera: {camera.numero_camera}")
        self.label_tipo_camera = QLabel(f"Tipo Camera: {camera.tipo_camera}")
        self.label_num_posti_letto = QLabel(f"Numero di Posti Letto: {camera.num_posti_letto}")
        self.label_prezzo = QLabel(f"Prezzo: €{camera.prezzo}")
        self.label_stato_camera = QLabel(f"Stato Camera: {camera.stato_camera}")

        for label in [self.label_numero_camera, self.label_tipo_camera, self.label_num_posti_letto, self.label_prezzo, self.label_stato_camera]:
            label.setStyleSheet("color: white;")

        self.layout.addWidget(self.label_numero_camera)
        self.layout.addWidget(self.label_tipo_camera)
        self.layout.addWidget(self.label_num_posti_letto)
        self.layout.addWidget(self.label_prezzo)
        self.layout.addWidget(self.label_stato_camera)

        btn_chiudi = QPushButton("Chiudi")
        btn_chiudi.clicked.connect(self.close)
        btn_chiudi.setStyleSheet("""
            QPushButton {
                background-color: #C3D4C7;
                color: black;
                border-radius: 10px;
                padding: 10px 15px; 
                font-size: 16px; /* dimensione del font */
                border: 2px solid #555; 
                transition: background-color 0.3s, color 0.3s; /* Effetto transizione più fluido? */
            }
            QPushButton:hover {
                background-color: #707070;
                color: white;
                border: 2px solid #707070; /* Bordo che cambia con il colore di sfondo */
            }
            QPushButton:pressed {
                background-color: #505050; /* più scuro al click */
            }
        """)
        self.layout.addWidget(btn_chiudi)

        self.setLayout(self.layout)
        self.setWindowTitle(f"Dettagli Camera: {camera.numero_camera}")
        self.setStyleSheet("background-color: #393535;")
