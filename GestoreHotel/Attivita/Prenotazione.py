import os.path
import pickle
import datetime


class Prenotazione:
    def __init__(self, cliente, codice, dataInizio, dataEmissione, dataScadenza, numeroOspiti, statoPrenotazione,
                 caparraVersata, servizioCamera, parcheggio, receptionist):
        self.cliente = cliente
        self.codice = codice
        self.dataInizio = dataInizio
        self.dataEmissione = dataEmissione
        self.dataScadenza = dataScadenza
        self.numeroOspiti = numeroOspiti
        self.statoPrenotazione = statoPrenotazione
        self.caparraVersata = caparraVersata
        self.servizioCamera = servizioCamera
        self.parcheggio = parcheggio
        self.receptionist = receptionist
        self.cliente.prenotato = 1
        self.cliente.salva_cliente()

        prenotazioni = {}
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[codice] = self
        with open('Dati/Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def getInfoPrenotazione(self):
        return {
            "cliente": self.cliente.getInfoCliente(),
            "codice": self.codice,
            "dataInizio": self.dataInizio,
            "dataEmissione": self.dataEmissione,
            "dataScadenza": self.dataScadenza,
            "numeroOspiti": self.numeroOspiti,
            "statoPrenotazione": self.statoPrenotazione,
            "caparraVersata": self.caparraVersata,
            "ServizioCamera": self.servizioCamera,
            "parcheggio": self.parcheggio,
            "receotionist": self.receptionist
        }

    def ricercaPrenotazione(self, codice):
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
                if codice in prenotazioni:
                    return prenotazioni[codice]
                else:
                    print(f"Prenotazione con codice {codice} non trovata.")
                    return None
        else:
            print("File Dati/Prenotazioni.pickle non trovato.")
            return None

    def rimuoviPrenotazione(self):
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)

            if self.codice in prenotazioni:
                del prenotazioni[self.codice]

                # Sovrascrivi l'intero dizionario di prenotazioni nel file
                with open('Dati/Prenotazioni.pickle', 'wb') as f:
                    pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)

                print(f"Prenotazione con codice {self.codice} rimossa con successo.")

                self.cliente.prenotato = 0
                self.cliente.salva_cliente()
            else:
                print(f"Prenotazione con codice {self.codice} non trovata nel dizionario.")

        else:
            print("File Dati/Prenotazioni.pickle non trovato.")

        # Ora elimina l'istanza della prenotazione
        del self


    def verificaScadenza(self):
        if datetime.datetime.now() > self.dataScadenza:
            # Aggiorna lo stato 'prenotato' del cliente se la prenotazione è scaduta
            self.cliente.prenotato = 0
            self.cliente.salva_cliente()
            return True
        return False