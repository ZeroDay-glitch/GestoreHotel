import os
import pickle

from Attivita.Servizio import Servizio


class Parcheggio(Servizio):
    def __init__(self, tipo_servizio, costo_servizio, posti_disponibili, tariffa_oraria):
        super().__init__(tipo_servizio, costo_servizio)
        self.posti_disponibili = posti_disponibili
        self.tariffa_oraria = tariffa_oraria

        parcheggi = {}
        if os.path.isfile('Dati/ServiziInCamera.pickle'):
            with open('Dati/ServiziInCamera.pickle', 'rb') as f:
                parcheggi = pickle.load(f)
        parcheggi[tipo_servizio] = self
        with open('Dati/Camere.pickle', 'wb') as f:
            pickle.dump(parcheggi, f, pickle.HIGHEST_PROTOCOL)

    def get_info(self):
        info = super().get_info_servizio()
        info.update({
            "posti_disponibili": self.posti_disponibili,
            "tariffa_oraria": self.tariffa_oraria
        })
        return info

    def verifica_disponibilita(self):
        pass

    def assegna_servizio(self):
        pass

    def rimuovi_servizio(self):
        pass
