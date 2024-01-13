import os.path
import pickle
import datetime


class Assegnamento:
    def __init__(self, cliente, codice, data_ora_inizio, data_ora_fine, servizio, camera):
        self.cliente = cliente
        self.codice = codice
        self.data_ora_inizio = data_ora_inizio
        self.data_ora_fine = data_ora_fine
        self.servizio = servizio
        self.camera = camera

        assegnamenti = {}
        if os.path.isfile('Dati/Assegnamenti.pickle'):
            with open('Dati/Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)
        assegnamenti[codice] = self
        with open('Dati/Assegnamenti.pickle', 'wb') as f:
            pickle.dump(assegnamenti, f, pickle.HIGHEST_PROTOCOL)

    def get_info_assegnamento(self):
        return {
            "cliente": self.cliente,
            "codice": self.codice,
            "data_ora_inizio": self.data_ora_inizio,
            "data_ora_fine": self.data_ora_fine,
            "servizio": self.servizio,
            "camera": self.camera
        }

    def modifica_assegnamento(self, new_data):
        try:
            with open('Dati/Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)

            if self.codice in assegnamenti:
                assegnamenti[self.codice].__dict__.update(new_data)
                with open('Dati/Assegnamenti.pickle', 'wb') as f:
                    pickle.dump(assegnamenti, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def elimina_assegnamento(self):
        try:
            with open('Dati/Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)

            if self.codice in assegnamenti:
                del assegnamenti[self.codice]
                with open('Dati/Assegnamenti.pickle', 'wb') as f:
                    pickle.dump(assegnamenti, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def verifica_scadenza(self):
        if datetime.datetime.now() > self.data_ora_fine:
            return True
        return False
