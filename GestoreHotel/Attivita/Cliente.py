import datetime
import os.path
import pickle

from PyQt5.QtWidgets import QMessageBox


class Cliente:
    def __init__(self, codice, codiceFiscale, cognome, dataNascita, documentoValido, email, luogoNascita, nome, telefono, prenotazioni=None):
        self.codice = codice
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.documentoValido = documentoValido
        self.email = email
        self.luogoNascita = luogoNascita
        self.nome = nome
        self.telefono = telefono
        self.prenotazioni = prenotazioni if prenotazioni else []

        clienti = {}
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[codiceFiscale] = self
        with open('Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def getInfoCliente(self):
        return {
            "codice": self.codice,
            "codiceFiscale": self.codiceFiscale,
            "cognome": self.cognome,
            "dataNascita": self.dataNascita,
            "documentoValido": self.documentoValido,
            "email": self.email,
            "luogoNascita": self.luogoNascita,
            "nome": self.nome,
            "telefono": self.telefono,
            "prenotazioni": self.prenotazioni
        }

    def ricercaClienteNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None

    def ricercaClienteCodice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                try:
                    return clienti[codice]
                except:
                    return None
        else:
            return None

    def rimuoviCliente(self):
        print("Prima della cancellazione")
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)

            # Verifica se il cliente è presente nel dizionario
            if self.codiceFiscale in clienti:
                # Rimuovi il cliente corrente dal dizionario
                del clienti[self.codiceFiscale]

                # Sovrascrivi l'intero dizionario di clienti nel file
                with open('Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

                print("Cliente rimosso con successo")
            else:
                print("Cliente non trovato nel dizionario")
        else:
            print("File Dati/Clienti.pickle non trovato")

    def modificaCliente(self):
        file_path = 'Dati/Clienti.pickle'

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                clienti = pickle.load(f)

            # Stampa di debug per la verifica
            print(f"Clienti prima dell'aggiornamento: {clienti}")

            if self.codiceFiscale in clienti:
                clienti[self.codiceFiscale] = self
                # Aggiungi questa stampa di debug
                print(f"Cliente modificato: {clienti[self.codiceFiscale].__dict__}")
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
                pickle.dump({self.codiceFiscale: self}, f, pickle.HIGHEST_PROTOCOL)
                print("File creato con successo")
