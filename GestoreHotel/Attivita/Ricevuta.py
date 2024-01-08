import datetime
import pickle
import os.path

class Ricevuta:
    def __init__(self, assegnamento, costoTotale, dataEmissione=None):
        self.assegnamento = assegnamento
        self.costoTotale = costoTotale
        self.dataEmissione = dataEmissione if dataEmissione else datetime.datetime.now()

        ricevute = {}
        if os.path.isfile('Dati\Ricevute.pickle'):
            with open('Dati\Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        ricevute[self.assegnamento] = self
        with open('Dati\Ricevute.pickle', 'wb') as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

    def getInfoRicevuta(self):
        return {
            "CodiceAssegnamento": self.assegnamento,
            "CostoTotale": self.costoTotale,
            "DataEmissione": self.dataEmissione
        }

    def eliminaRicevuta(self):
        if os.path.isfile('Dati\Ricevute.pickle'):
            with open('Dati\Ricevute.pickle', 'wb+') as f:
                ricevute = dict(pickle.load(f))
                del ricevute[self.assegnamento.codice]
                pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
        self.costoTotale = 0.0
        self.dataEmissione = None
        self.assegnamento = None
        del self
