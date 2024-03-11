import os.path
import pickle

from Attivita.Dipendente import Dipendente


class Receptionist(Dipendente):
    def __init__(self, cellulare, codice, cognome, data_nascita, luogo_nascita, nome, lingue, password):
        super().__init__(cellulare, codice, cognome, data_nascita, luogo_nascita, nome, ruolo="receptionist", password=password)
        self.lingue = lingue
        self.prenotazioni = []

        receptionists = {}
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = pickle.load(f)
        receptionists[codice] = self
        with open('Dati/Receptionist.pickle', 'wb') as f:
            pickle.dump(receptionists, f, pickle.HIGHEST_PROTOCOL)

    def get_info_receptionist(self):
        info = self.get_info_dipendente()
        info.update({
            "lingue": self.lingue,
            "prenotazioni": self.prenotazioni
        })
        return info

    def ricerca_dipendente_nome_cognome(self, nome, cognome):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = dict(pickle.load(f))
                for receptionist in receptionists.values():
                    if receptionist.nome == nome and receptionist.cognome == cognome:
                        return receptionist
                return None
        else:
            return None

    def ricerca_dipendente_codice(self, codice):
        if os.path.isfile('Dati/Receptionist.pickle'):
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = dict(pickle.load(f))
                try:
                    return receptionists[codice]
                except:
                    return None
        else:
            return None

    def modifica_dipendente(self, new_data):
        try:
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = pickle.load(f)

            if self.codice in receptionists:
                receptionists[self.codice].__dict__.update(new_data)

                with open('Dati/Receptionist.pickle', 'wb') as f:
                    pickle.dump(receptionists, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def rimuovi_dipendente(self):
        try:
            with open('Dati/Receptionist.pickle', 'rb') as f:
                receptionists = pickle.load(f)

            if self.codice in receptionists:
                del receptionists[self.codice]

                with open('Dati/Receptionist.pickle', 'wb') as f:
                    pickle.dump(receptionists, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False