import os.path
import pickle
import datetime


class Prenotazione:
    def __init__(self, cliente, codice, dataInizio, dataOraEmissione, dataScadenza, numeroOspiti, statoPrenotazione,
                 caparraVersata, servizio, receptionist):
        self.cliente = cliente
        self.codice = codice
        self.dataInizio = dataInizio
        self.dataOraEmissione = dataOraEmissione
        self.dataScadenza = dataScadenza
        self.numeroOspiti = numeroOspiti
        self.statoPrenotazione = statoPrenotazione
        self.caparraVersata = caparraVersata
        self.servizio = servizio
        self.receptionist = receptionist

        prenotazioni = {}
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[codice] = self
        with open('Dati\Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def getInfoPrenotazione(self):
        return {
            "Cliente": self.cliente.getInfoCliente(),
            "Codice": self.codice,
            "Data di Inizio": self.dataInizio,
            "Data e Ora di Emissione": self.dataOraEmissione,
            "Data di Scadenza": self.dataScadenza,
            "Numero Ospiti": self.numeroOspiti,
            "Stato Prenotazione": self.statoPrenotazione,
            "Caparra Versata": self.caparraVersata,
            "Receotionist": self.receptionist
        }

    def ricercaPrenotazione(self, codice):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
                return prenotazioni[codice]
        else:
            return None

    def rimuoviPrenotazione(self):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'wb+') as f:
                prenotazioni = pickle.load(f)
                del prenotazioni[self.codice]
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
        self.cliente = ""
        self.codice = ""
        self.dataInizio = None
        self.dataOraEmissione = None
        self.dataScadenza = None
        self.numeroOspiti = 0
        self.statoPrenotazione = ""
        self.caparraVersata = 0.0
        self.receptionist = ""
        del self

    def verificaScadenza(self):
        return datetime.datetime.now() > self.dataScadenza