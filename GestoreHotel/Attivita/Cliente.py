import datetime
import os.path
import pickle

from PyQt5.QtWidgets import QMessageBox


class Cliente:
    def __init__(self, codice, codiceFiscale, cognome, dataNascita, documentoValido, email, luogoNascita, nome, telefono,
                 prenotazioni=None):
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
            "Codice": self.codice,
            "Codice Fiscale": self.codiceFiscale,
            "Cognome": self.cognome,
            "Data di Nascita": self.dataNascita,
            "Documento Valido": self.documentoValido,
            "Email": self.email,
            "Luogo di Nascita": self.luogoNascita,
            "Nome": self.nome,
            "Telefono": self.telefono,
            "Prenotazioni": self.prenotazioni
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

            # Verifica se il cliente è presente nel dizionario
            if self.codiceFiscale in clienti:
                # Aggiorna il cliente corrente nel dizionario
                clienti[self.codiceFiscale] = self

                # Sovrascrivi l'intero dizionario di clienti nel file
                with open(file_path, 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

                print("Cliente modificato con successo")
            else:
                print("Cliente non trovato nel dizionario")
        else:
            print(f"File {file_path} non trovato. Creazione del file...")

            # Crea il file pickle con il cliente corrente
            with open(file_path, 'wb') as f:
                pickle.dump({self.codiceFiscale: self}, f, pickle.HIGHEST_PROTOCOL)

                print("File creato con successo")





