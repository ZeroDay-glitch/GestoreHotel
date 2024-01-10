import os.path
import pickle

from Attivita.Dipendente import Dipendente


class Receptionist(Dipendente):
    def __init__(self, codice, codiceFiscale, cognome, dataNascita, email, luogoNascita, nome, telefono, lingue=None):
        super().__init__(codice, codiceFiscale, cognome, dataNascita, email, luogoNascita, nome, telefono,
                         mansione='Receptionist')
        self.lingue = lingue if lingue else []

        receptionists = {}
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = pickle.load(f)
        receptionists[codice] = self
        with open('Dati/Receptionist.pickle', 'wb') as f:
            pickle.dump(receptionists, f, pickle.HIGHEST_PROTOCOL)

    def getInfoReceptionist(self):
        info = self.getInfoDipendente()
        info['Lingue'] = self.lingue
        return info

    def ricercaDipendenteNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = dict(pickle.load(f))
                for receptionist in receptionists.values():
                    if receptionist.nome == nome and receptionist.cognome == cognome:
                        return receptionist
                return None
        else:
            return None

    def ricercaDipendenteCodice(self, codice):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = dict(pickle.load(f))
                try:
                    return receptionists[codice]
                except:
                    return None
        else:
            return None

    def ricercaDipendenteCF(self, codiceFiscale):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = dict(pickle.load(f))
                for receptionist in receptionists.values():
                    if receptionist.codiceFiscale == codiceFiscale:
                        return receptionist
                return None
        else:
            return None

    def rimuoviReceptionist(self):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = pickle.load(f)
                if self.codice in receptionists:
                    del receptionists[self.codice]
                    with open('Dati/Receptionist.pickle', 'wb') as f:
                        pickle.dump(receptionists, f, pickle.HIGHEST_PROTOCOL)

        # Chiamare il metodo della classe base per rimuovere il dipendente
        self.rimuoviDipendente()
        self.lingue = ""
        del self
