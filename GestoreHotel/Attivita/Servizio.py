from abc import abstractmethod


class Servizio:
    def __init__(self, tipo_servizio, costo_servizio):
        self.tipo_servizio = tipo_servizio
        self.costo_servizio = costo_servizio


    def get_info_servizio(self):
        return {
            "tipo_servizio": self.tipo_servizio,
            "costo_servizio": self.costo_servizio
        }

    @abstractmethod
    def ricerca_servizio(self):
        pass

    @abstractmethod
    def assegna_servizio(self):
        pass

    @abstractmethod
    def rimuovi_servizio(self):
        pass



