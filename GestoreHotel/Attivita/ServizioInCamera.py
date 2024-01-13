import os
import pickle

from Attivita.Servizio import Servizio


class ServizioInCamera(Servizio):
    def __init__(self, tipo_servizio, costo_servizio, camera, addettoServizi, note=""):
        super().__init__(tipo_servizio, costo_servizio)
        self.camera = camera
        self.addettoServizi = addettoServizi
        self.note = note

        servizi_in_camera = {}
        if os.path.isfile('Dati/ServiziInCamera.pickle'):
            with open('Dati/ServiziInCamera.pickle', 'rb') as f:
                servizi_in_camera = pickle.load(f)
        servizi_in_camera[self.tipo_servizio] = self
        with open('Dati/ServiziInCamera.pickle', 'wb') as f:
            pickle.dump(servizi_in_camera, f, pickle.HIGHEST_PROTOCOL)


    def get_info_servizio_in_camera(self):
        info = super().get_info_servizio()
        info["camera"] = self.camera.get_info()
        info["addettoServizi"] = self.addettoServizi.get_info()
        info["note"] = self.note
        return info

    def assegna_servizio(self):
        # Implementa l'assegnamento del servizio alla camera e all'addettoServizi
        pass

    def rimuovi_servizio(self):
        # Implementa la rimozione del servizio dalla camera e dall'addettoServizi
        pass






