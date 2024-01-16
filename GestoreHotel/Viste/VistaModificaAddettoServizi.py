from PyQt5.QtWidgets import QWidget


class VistaModificaAddettoServizi(QWidget):
    def __init__(self, addetto_servizi, callback, vista_addetto_servizi):
        super(VistaModificaAddettoServizi, self).__init__()
        self.addetto_servizi = addetto_servizi
        self.callback = callback
        self.vista_addetto_servizi = vista_addetto_servizi
