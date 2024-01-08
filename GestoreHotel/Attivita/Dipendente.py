from abc import abstractmethod
import datetime


class Dipendente:
    def __init__(self, codice, codiceFiscale, cognome, dataNascita, email, luogoNascita, nome, telefono, mansione=None):
        self.codice = codice
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.luogoNascita = luogoNascita
        self.nome = nome
        self.telefono = telefono
        self.mansione = mansione

    def getInfoDipendente(self):
        return {
            "Nome": self.nome,
            "Cognome": self.cognome,
            "CodiceFiscale": self.codiceFiscale,
            "DataNascita": self.dataNascita,
            "Email": self.email,
            "LuogoNascita": self.luogoNascita,
            "Telefono": self.telefono,
            "Mansione": self.mansione
        }

    @abstractmethod
    def ricercaDipendenteNomeCognome(self, nome, cognome):
        pass

    @abstractmethod
    def ricercaDipendenteCodice(self, codice):
        pass

    @abstractmethod
    def ricercaDipendenteCF(self, codiceFiscale):
        pass

    def rimuoviDipendente(self):
        self.codice = -1
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = datetime.datetime(1900, 1, 1)
        self.email = ""
        self.luogoNascita = ""
        self.nome = ""
        self.telefono = 0
        self.mansione = ""
