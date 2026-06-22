from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.dialog import VentanaLista

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/EstructurasMenu.ui", self)
        
        self.actionLista_Enlazada.triggered.connect(self.abrir_lista_enlazada_simple)
     
    def abrir_lista_enlazada_simple(self):
        ventana_lista = VentanaLista()
        ventana_lista.exec_()