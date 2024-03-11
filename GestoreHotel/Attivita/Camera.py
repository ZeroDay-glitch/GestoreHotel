import os.path
import pickle

class Camera:
    CAMERE_FILE = 'Dati/Camere.pickle'

    def __init__(self, numero_camera, tipo_camera, num_posti_letto, prezzo, stato_camera="disponibile", assegnamento=None):
        self.numero_camera = numero_camera
        self.tipo_camera = tipo_camera
        self.num_posti_letto = num_posti_letto
        self.prezzo = prezzo
        self.stato_camera = stato_camera
        self.assegnamento = assegnamento

    def get_info_camera(self):
        return {
            "numero_camera": self.numero_camera,
            "tipo_camera": self.tipo_camera,
            "num_posti_letto": self.num_posti_letto,
            "prezzo": self.prezzo,
            "stato_camera": self.stato_camera,
            "assegnamento": self.assegnamento
        }

    def modifica_stato_camera(self, nuovo_stato):
        self.stato_camera = nuovo_stato
        Camera.salva_camere(Camera.carica_camere())

    def verifica_disponibilita(self):
        return self.stato_camera == "disponibile"

    @classmethod
    def carica_camere(cls):
        if os.path.isfile(cls.CAMERE_FILE):
            with open(cls.CAMERE_FILE, 'rb') as f:
                return pickle.load(f)
        else:
            return {}

    @classmethod
    def salva_camere(cls, camere):
        with open(cls.CAMERE_FILE, 'wb') as f:
            pickle.dump(camere, f, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def crea_camere(cls):
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
        cls.salva_camere(camere)
        return camere
