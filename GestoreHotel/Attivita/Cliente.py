import datetime
import os.path
import pickle

from PyQt5.QtWidgets import QMessageBox


class Cliente:
    def __init__(self, cellulare, codice, codice_fiscale, cognome, data_nascita, documento, email, luogo_nascita,
                 nome, note="", bloccato=False):
        self.cellulare = cellulare
        self.codice = codice
        self.codice_fiscale = codice_fiscale
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.documento = documento
        self.email = email
        self.luogo_nascita = luogo_nascita
        self.nome = nome
        self.note = note
        self.prenotazioni = []
        self.bloccato = bloccato

        clienti = {}
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[codice] = self
        with open('Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def get_info_cliente(self):
        return {
            "codice": self.codice,
            "codice_fiscale": self.codice_fiscale,
            "cognome": self.cognome,
            "data_nascita": self.data_nascita,
            "documento": self.documento,
            "email": self.email,
            "luogo_nascita": self.luogo_nascita,
            "nome": self.nome,
            "cellulare": self.cellulare,
            "prenotazioni": self.prenotazioni,
            "note": self.note,
            "bloccato": self.bloccato
        }

    def ricerca_cliente_nome_cognome(self, nome, cognome):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None

    def ricerca_cliente_codice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                try:
                    return clienti[codice]
                except:
                    return None
        else:
            return None

    def rimuovi_cliente(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

            if self.codice in clienti:
                del clienti[self.codice]

                with open('Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

                print("Cliente rimosso con successo")
                return True
            else:
                print("Cliente non trovato nel dizionario")
        else:
            print("File Dati/Clienti.pickle non trovato")

    def modifica_cliente(self, new_data):
        try:
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

            if self.codice in clienti:
                clienti[self.codice].__dict__.update(new_data)

                with open('Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
                return True
            else:
                return False
        except FileNotFoundError:
            return False
