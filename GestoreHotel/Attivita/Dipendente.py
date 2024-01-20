from abc import abstractmethod
import datetime


class Dipendente:
    def __init__(self, cellulare, codice, cognome, data_nascita, luogo_nascita, nome, ruolo, password):
        self.cellulare = cellulare
        self.codice = codice
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.nome = nome
        self.ruolo = ruolo
        self.password = password

    def get_info_dipendente(self):
        return {
            "codice": self.codice,
            "cognome": self.cognome,
            "data_nascita": self.data_nascita,
            "luogo_nascita": self.luogo_nascita,
            "nome": self.nome,
            "cellulare": self.cellulare,
            "ruolo": self.ruolo,
            "password": self.password
        }

    @abstractmethod
    def ricerca_dipendente_nome_cognome(self, nome, cognome):
        pass

    @abstractmethod
    def ricerca_dipendente_codice(self, codice):
        pass

    @abstractmethod
    def modifica_dipendente(self, new_data):
        pass

    @abstractmethod
    def rimuovi_dipendente(self):
        pass
