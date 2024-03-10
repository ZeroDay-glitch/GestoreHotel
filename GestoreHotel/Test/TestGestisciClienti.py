import os
import pickle
import unittest
from datetime import datetime, timedelta

from Attivita.Cliente import Cliente
from Attivita.Prenotazione import Prenotazione


class TestGestioneClienti(unittest.TestCase):

    def setUp(self):

        self.cellulare_cliente = "1234567890"
        self.codice_cliente = "CL123"
        self.codice_fiscale_cliente = "ABCDEF12G34H567I"
        self.cognome_cliente = "Rossi"
        self.data_nascita_cliente = datetime(1990, 1, 1)
        self.documento_cliente = "123456789"
        self.email_cliente = "rossi@example.com"
        self.luogo_nascita_cliente = "Roma"
        self.nome_cliente = "Mario"

        self.cliente = Cliente(self.cellulare_cliente, self.codice_cliente, self.codice_fiscale_cliente,
                                self.cognome_cliente, self.data_nascita_cliente, self.documento_cliente,
                                self.email_cliente, self.luogo_nascita_cliente, self.nome_cliente)

    def test_aggiungi_cliente(self):

        clienti = self.carica_clienti_da_file()
        self.assertIsNotNone(clienti)
        self.assertIn(self.codice_cliente, clienti)

    def test_rimuovi_cliente(self):

        self.assertTrue(self.cliente.rimuovi_cliente())
        clienti = self.carica_clienti_da_file()
        self.assertIsNotNone(clienti)
        self.assertNotIn(self.codice_cliente, clienti)

    def carica_clienti_da_file(self):
        clienti = None
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.pickle", "rb") as f:
                clienti = pickle.load(f)
        return clienti


class TestGestionePrenotazioni(unittest.TestCase):

    def setUp(self):

        self.cellulare_cliente = "1234567890"
        self.codice_cliente = "CL123"
        self.codice_fiscale_cliente = "ABCDEF12G34H567I"
        self.cognome_cliente = "Rossi"
        self.data_nascita_cliente = datetime(1990, 1, 1)
        self.documento_cliente = "123456789"
        self.email_cliente = "rossi@example.com"
        self.luogo_nascita_cliente = "Roma"
        self.nome_cliente = "Mario"

        self.cliente = Cliente(self.cellulare_cliente, self.codice_cliente, self.codice_fiscale_cliente,
                                self.cognome_cliente, self.data_nascita_cliente, self.documento_cliente,
                                self.email_cliente, self.luogo_nascita_cliente, self.nome_cliente)

    def test_aggiungi_prenotazione(self):

        data_ora_inizio = datetime.now()
        data_ora_fine = datetime.now() + timedelta(days=1)
        numero_ospiti = 2
        receptionist = "Giovanni"

        codice_prenotazione = "PR123"
        prenotazione = Prenotazione(self.cliente, codice_prenotazione, data_ora_inizio, data_ora_fine,
                                    numero_ospiti, receptionist)

        prenotazioni = self.carica_prenotazioni_da_file()
        self.assertIsNotNone(prenotazioni)
        self.assertIn(codice_prenotazione, prenotazioni)

    def test_rimuovi_prenotazione(self):

        data_ora_inizio = datetime.now()
        data_ora_fine = datetime.now() + timedelta(days=1)
        numero_ospiti = 2
        receptionist = "Giovanni"

        codice_prenotazione = "PR123"
        prenotazione = Prenotazione(self.cliente, codice_prenotazione, data_ora_inizio, data_ora_fine,
                                    numero_ospiti, receptionist)

        self.assertTrue(prenotazione.elimina_prenotazione())

        prenotazioni = self.carica_prenotazioni_da_file()
        self.assertIsNotNone(prenotazioni)
        self.assertNotIn(codice_prenotazione, prenotazioni)

    def test_verifica_scadenza_prenotazione(self):

        data_ora_inizio = datetime.now() - timedelta(days=2)
        data_ora_fine = datetime.now() - timedelta(days=1)
        numero_ospiti = 2
        receptionist = "Giovanni"

        codice_prenotazione = "PR456"
        prenotazione_scaduta = Prenotazione(self.cliente, codice_prenotazione, data_ora_inizio, data_ora_fine,
                                            numero_ospiti, receptionist)

        prenotazioni = self.carica_prenotazioni_da_file()
        self.assertIsNotNone(prenotazioni)
        self.assertIn(codice_prenotazione, prenotazioni)

        self.assertTrue(prenotazione_scaduta.verifica_scadenza())

    def carica_prenotazioni_da_file(self):
        prenotazioni = None
        if os.path.isfile("Dati/Prenotazioni.pickle"):
            with open("Dati/Prenotazioni.pickle", "rb") as f:
                prenotazioni = pickle.load(f)
        return prenotazioni
