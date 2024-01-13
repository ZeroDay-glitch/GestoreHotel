import datetime
import pickle
import os.path


class Ricevuta:
    def __init__(self, assegnamento, data_emissione, costo_totale):
        self.assegnamento = assegnamento
        self.data_emissione = data_emissione
        self.costo_totale = costo_totale

        ricevute = {}
        if os.path.isfile('Dati/Ricevute.pickle'):
            with open('Dati/Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        ricevute[data_emissione] = self  # Assuming data_emissione is unique for each receipt
        with open('Dati/Ricevute.pickle', 'wb') as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

    def get_info_ricevuta(self):
        return {
            "assegnamento": self.assegnamento,
            "data_emissione": self.data_emissione,
            "costo_totale": self.costo_totale
        }

    def modifica_ricevuta(self, new_data):
        try:
            with open('Dati/Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)

            if self.data_emissione in ricevute:
                ricevute[self.data_emissione].__dict__.update(new_data)
                with open('Dati/Ricevute.pickle', 'wb') as f:
                    pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def elimina_ricevuta(self):
        try:
            with open('Dati/Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)

            if self.data_emissione in ricevute:
                del ricevute[self.data_emissione]
                with open('Dati/Ricevute.pickle', 'wb') as f:
                    pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False
