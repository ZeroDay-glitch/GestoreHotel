import os
import pickle
import datetime


class Prenotazione:
    def __init__(self, cliente, codice, data_ora_inizio, data_ora_fine, numero_ospiti, receptionist, servizi=None):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.numero_ospiti = numero_ospiti
        self.receptionist = receptionist
        self.servizi = servizi if servizi is not None else []

        prenotazioni = {}
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[self.codice] = self
        with open('Dati/Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def get_info_prenotazione(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "numero_ospiti": self.numero_ospiti,
            "receptionist": self.receptionist,
            "servizi": [servizio.get_info_servizio() for servizio in self.servizi]
        }

    def modifica_prenotazione(self, new_data):
        try:
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

            if self.codice in prenotazioni:
                prenotazioni[self.codice].__dict__.update(new_data)
                with open('Dati/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def elimina_prenotazione(self):
        try:
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

            if self.codice in prenotazioni:
                del prenotazioni[self.codice]
                with open('Dati/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def verifica_scadenza(self):
        if datetime.datetime.now() > self.data_ora_fine:
            return True
        return False
