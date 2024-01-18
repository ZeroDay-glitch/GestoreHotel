import os
import pickle

from Attivita.Servizio import Servizio


class ServizioInCamera(Servizio):
    def __init__(self, tipo_servizio, costo_servizio, camera, addettoServizi, note=""):
        super().__init__(tipo_servizio, costo_servizio)
        self.camera = camera
        self.addettoServizi = addettoServizi
        self.note = note

        # Carica i servizi esistenti, aggiungi questo servizio e salva
        servizi_in_camera = self.carica_servizi()
        servizi_in_camera[self.tipo_servizio] = self
        self.salva_servizi(servizi_in_camera)

    def carica_servizi(self):
        if os.path.isfile('Dati/ServiziInCamera.pickle'):
            with open('Dati/ServiziInCamera.pickle', 'rb') as f:
                return pickle.load(f)
        return {}

    def salva_servizi(self, servizi_in_camera):
        with open('Dati/ServiziInCamera.pickle', 'wb') as f:
            pickle.dump(servizi_in_camera, f, pickle.HIGHEST_PROTOCOL)

    def get_info_servizio_in_camera(self):
        info = super().get_info_servizio()
        info.update({
            "camera": self.camera.get_info(),
            "addettoServizi": self.addettoServizi.get_info(),
            "note": self.note
        })
        return info

    def assegna_servizio(self):
        # Implementazione specifica: collega il servizio alla camera e all'addettoServizi
        pass

    def rimuovi_servizio(self):
        # Implementazione specifica: rimuove il servizio dalla camera e dall'addettoServizi
        servizi_in_camera = self.carica_servizi()
        if self.tipo_servizio in servizi_in_camera:
            del servizi_in_camera[self.tipo_servizio]
            self.salva_servizi(servizi_in_camera)
        pass
