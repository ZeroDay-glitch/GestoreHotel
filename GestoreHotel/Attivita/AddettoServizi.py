import os.path
import pickle

from Attivita.Dipendente import Dipendente


class AddettoServizi(Dipendente):
    def __init__(self, codice, codiceFiscale, cognome, dataNascita, email, luogoNascita, nome, telefono,
                 camere=None):
        super().__init__(codice, codiceFiscale, cognome, dataNascita, email, luogoNascita, nome, telefono,
                         mansione="AddettoServizi")
        self.camere = camere if camere else []

        addettiServizi = {}
        if os.path.isfile('Dati\AddettoServizi.pickle'):
            with open('Dati\AddettoServizi.pickle', 'rb') as f:
                addettiServizi = pickle.load(f)
        addettiServizi[codice] = self
        with open('Dati\AddettoServizi.pickle', 'wb') as f:
            pickle.dump(addettiServizi, f, pickle.HIGHEST_PROTOCOL)


    def getInfoAddettoServizi(self):
        info = self.getInfoDipendente()
        info["Camere"] = self.camere
        return info

    def ricercaDipendenteNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati\AddettoServizi.pickle'):
            with open('Dati\AddettoServizi.pickle', 'rb') as f:
                addettiServizi = dict(pickle.load(f))
                for addettoServizi in addettiServizi.values():
                    if addettoServizi.nome == nome and addettoServizi.cognome == cognome:
                        return addettoServizi
                return None
        else:
            return None

    def ricercaDipendenteCodice(self, codice):
        if os.path.isfile('Dati\AddettoServizi.pickle'):
            with open('Dati\AddettoServizi.pickle', 'rb') as f:
                addettiServizi = dict(pickle.load(f))
                try:
                    return addettiServizi[codice]
                except:
                    return None
        else:
            return None

    def ricercaDipendenteCF(self, codiceFiscale):
        if os.path.isfile('Dati\AddettoServizi.pickle'):
            with open('Dati\AddettoServizi.pickle', 'rb') as f:
                addettiServizi = dict(pickle.load(f))
                for addettoServizi in addettiServizi.values():
                    if addettoServizi.codiceFiscale == codiceFiscale:
                        return addettoServizi
                return None
        else:
            return None

    def rimuoviAddettoServizi(self):
        if os.path.isfile('Dati\AddettoServizi.pickle'):
            with open('Dati\AddettoServizi.pickle', 'rb') as f:
                addettiServizi = pickle.load(f)
                if self.codice in addettiServizi:
                    del addettiServizi[self.codice]
                    with open('Dati\AddettoServizi.pickle', 'wb') as f:
                        pickle.dump(addettiServizi, f, pickle.HIGHEST_PROTOCOL)

        # Chiamare il metodo della classe base per rimuovere il dipendente
        self.rimuoviDipendente()
        self.camere = ""
        del self

