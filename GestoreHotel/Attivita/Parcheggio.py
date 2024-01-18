import os
import pickle

from Attivita.Servizio import Servizio


class Parcheggio(Servizio):
    def __init__(self, tipo_servizio, costo_servizio, posti_disponibili, tariffa_oraria):
        super().__init__(tipo_servizio, costo_servizio)
        self.posti_disponibili = posti_disponibili
        self.tariffa_oraria = tariffa_oraria

        # Carica i parcheggi esistenti, aggiungi questo parcheggio e salva
        parcheggi = self.carica_parcheggi()
        parcheggi[self.tipo_servizio] = self
        self.salva_parcheggi(parcheggi)

    def carica_parcheggi(self):
        if os.path.isfile('Dati/Parcheggi.pickle'):
            with open('Dati/Parcheggi.pickle', 'rb') as f:
                return pickle.load(f)
        return {}

    def salva_parcheggi(self, parcheggi):
        with open('Dati/Parcheggi.pickle', 'wb') as f:
            pickle.dump(parcheggi, f, pickle.HIGHEST_PROTOCOL)

    def get_info(self):
        info = super().get_info_servizio()
        info.update({
            "posti_disponibili": self.posti_disponibili,
            "tariffa_oraria": self.tariffa_oraria
        })
        return info

    def verifica_disponibilita(self):
        # Implementazione specifica: verifica la disponibilità di posti nel parcheggio
        pass

    def assegna_servizio(self):
        # Implementazione specifica: assegna un posto auto
        pass

    def rimuovi_servizio(self):
        # Implementazione specifica: libera un posto auto
        pass
