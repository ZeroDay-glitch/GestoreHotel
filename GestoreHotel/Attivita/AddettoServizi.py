import os.path
import pickle

from Attivita.Dipendente import Dipendente


class AddettoServizi(Dipendente):
    def __init__(self, cellulare, codice, cognome, data_nascita, luogo_nascita, nome, camera, servizio_in_camera):
        super().__init__(cellulare, codice, cognome, data_nascita, luogo_nascita, nome, ruolo="addettoServizi")
        self.camera = camera
        self.servizio_in_camera = servizio_in_camera

        addetti = {}
        if os.path.isfile('Dati/AddettoServizi.pickle'):
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                addetti = pickle.load(f)
        addetti[codice] = self
        with open('Dati/AddettoServizi.pickle', 'wb') as f:
            pickle.dump(addetti, f, pickle.HIGHEST_PROTOCOL)


    def get_info_addetto(self):
        info = self.get_info_dipendente()
        info.update({
            "camera": self.camera,
            "servizio_in_camera": self.servizio_in_camera
        })
        return info

    def ricerca_dipendente_nome_cognome(self, nome, cognome):
        if os.path.isfile('Dati/AddettoServizi.pickle'):
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                addetti = dict(pickle.load(f))
                for addetto in addetti.values():
                    if addetto.nome == nome and addetto.cognome == cognome:
                        return addetto
                return None
        else:
            return None

    def ricerca_dipendente_codice(self, codice):
        if os.path.isfile('Dati/AddettoServizi.pickle'):
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                addetti = dict(pickle.load(f))
                return addetti.get(codice, None)
        else:
            return None

    def modifica_dipendente(self, new_data):
        try:
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                addetti = pickle.load(f)

            if self.codice in addetti:
                addetti[self.codice].__dict__.update(new_data)

                with open('Dati/AddettoServizi.pickle', 'wb') as f:
                    pickle.dump(addetti, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False

    def rimuovi_dipendente(self):
        try:
            with open('Dati/AddettoServizi.pickle', 'rb') as f:
                addetti = pickle.load(f)

            if self.codice in addetti:
                del addetti[self.codice]

                with open('Dati/AddettoServizi.pickle', 'wb') as f:
                    pickle.dump(addetti, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False
