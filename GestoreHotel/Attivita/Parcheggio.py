import os
import pickle

from Attivita.Servizio import Servizio


class Parcheggio(Servizio):
    def __init__(self, tipo_servizio, costo_servizio, posti_disponibili, tariffa_oraria):
        super().__init__(tipo_servizio, costo_servizio)
        self.posti_disponibili = posti_disponibili
        self.tariffa_oraria = tariffa_oraria

        parcheggi = {}
        if os.path.isfile('Dati/Parcheggi.pickle'):
            with open('Dati/Parcheggi.pickle', 'rb') as f:
                parcheggi = pickle.load(f)
        parcheggi[self.tipo_servizio] = self
        with open('Dati/Parcheggi.pickle', 'wb') as f:
            pickle.dump(parcheggi, f, pickle.HIGHEST_PROTOCOL)

    def get_info(self):
        info = super().get_info_servizio()
        info["posti_disponibili"] = self.posti_disponibili
        info["tariffa_oraria"] = self.tariffa_oraria
        return info

    def calcola_costo(self):
        # Implementa il calcolo del costo del parcheggio
        pass

    def verifica_disponibilita(self):
        # Implementa la verifica della disponibilità di posti auto nel parcheggio
        pass

    def assegna_servizio(self):
        # Implementa l'assegnamento del servizio alla camera e all'addettoServizi
        pass

    def rimuovi_servizio(self):
        # Implementa la rimozione del servizio dalla camera e dall'addettoServizi
        pass


