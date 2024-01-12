import datetime
import os.path
import pickle

from PyQt5.QtWidgets import QMessageBox


class Cliente:
    def __init__(self, cellulare, codice, codice_fiscale, cognome, data_nascita, documento, email, luogo_nascita, nome,
                 note):
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
            "note": self.note
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
        print("Prima della cancellazione")
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

            # Verifica se il cliente è presente nel dizionario
            if self.codice in clienti:
                # Rimuovi il cliente corrente dal dizionario
                del clienti[self.codice]

                # Sovrascrivi l'intero dizionario di clienti nel file
                with open('Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

                print("Cliente rimosso con successo")
            else:
                print("Cliente non trovato nel dizionario")
        else:
            print("File Dati/Clienti.pickle non trovato")

    def modifica_cliente(self):
        file_path = 'Dati/Clienti.pickle'

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                clienti = pickle.load(f)

            # Stampa di debug per la verifica
            print(f"Clienti prima dell'aggiornamento: {clienti}")

            if self.codice in clienti:
                clienti[self.codice] = self
                # Aggiungi questa stampa di debug
                print(f"Cliente modificato: {clienti[self.codice].__dict__}")
                with open(file_path, 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
                print("Cliente modificato con successo")

                with open(file_path, 'rb') as f:
                    clienti_aggiornati = pickle.load(f)
                    print(f"Clienti dopo l'aggiornamento: {clienti_aggiornati}")
            else:
                print("Cliente non trovato nel dizionario")
        else:
            print(f"File {file_path} non trovato. Creazione del file...")
            with open(file_path, 'wb') as f:
                pickle.dump({self.codice: self}, f, pickle.HIGHEST_PROTOCOL)
                print("File creato con successo")
