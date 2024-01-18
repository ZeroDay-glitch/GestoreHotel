import os.path
import pickle

class Camera:
    def __init__(self, numero_camera, tipo_camera, num_posti_letto, prezzo, stato_camera="disponibile"):
        self.numero_camera = numero_camera
        self.tipo_camera = tipo_camera
        self.num_posti_letto = num_posti_letto
        self.prezzo = prezzo
        self.stato_camera = stato_camera
        self.prenotazione = None  # Inizialmente non c'è prenotazione associata

        camere = {}
        if os.path.isfile('Dati/Camere.pickle'):
            with open('Dati/Camere.pickle', 'rb') as f:
                camere = pickle.load(f)
        camere[numero_camera] = self
        with open('Dati/Camere.pickle', 'wb') as f:
            pickle.dump(camere, f, pickle.HIGHEST_PROTOCOL)

    def get_info_camera(self):
        return {
            "numero_camera": self.numero_camera,
            "tipo_camera": self.tipo_camera,
            "num_posti_letto": self.num_posti_letto,
            "prezzo": self.prezzo,
            "stato_camera": self.stato_camera,
            "prenotazione": self.prenotazione
        }

    def modifica_stato_camera(self, nuovo_stato):
        self.stato_camera = nuovo_stato

    def verifica_disponibilita(self):
        return self.stato_camera == "disponibile"
