import os.path
import pickle
import datetime


class Assegnamento:
    def __init__(self, prenotazione, dataInizio, dataScadenza, servizio):
        self.codice = prenotazione.codice
        self.prenotazione = prenotazione
        self.dataInizio = dataInizio
        self.dataScadenza = dataScadenza
        self.servizio = servizio

        assegnamenti = {}
        if os.path.isfile('Dati\Assegnamenti.pickle'):
            with open('Dati\Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)
        assegnamenti[prenotazione.codice] = self
        with open('Dati\Assegnamenti.pickle', 'wb') as f:
            pickle.dump(assegnamenti, f, pickle.HIGHEST_PROTOCOL)

    def getInfoAssegnamento(self):
        return {
            "Codice": self.prenotazione.codice,
            "Prenotazione": self.prenotazione,
            "Data di Inizio": self.dataInizio,
            "Data di Scadenza": self.dataScadenza,
            "Servizio": self.servizio
        }

    def ricercaAssegnamento(self, codice):
        if os.path.isfile('Dati\Assegnamenti.pickle'):
            with open('Dati\Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)
                return assegnamenti[codice]
        else:
            return None

    def rimuoviAssegnamento(self):
        if os.path.isfile('Dati\Assegnamenti.pickle'):
            with open('Dati\Assegnamenti.pickle', 'wb+') as f:
                assegnamenti = pickle.load(f)
                del assegnamenti[self.prenotazione.codice]
                pickle.dump(assegnamenti, f, pickle.HIGHEST_PROTOCOL)
        self.codice = None
        self.prenotazione = None
        self.dataInizio = None
        self.dataScadenza = None
        self.servizio = None
        del self

    def verificaScadenza(self):
        return datetime.datetime.now() > self.dataScadenza
