from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.dialog import VentanaLista
from load.pila import pilaLista

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/EstructurasMenu.ui", self)
        
        self.actionLista_Enlazada.triggered.connect(self.abrir_lista_enlazada_simple)
        self.Pila.triggered.connect(self.abrir_stack)     
        
        
    def abrir_lista_enlazada_simple(self):
        ventana_lista = VentanaLista()
        ventana_lista.exec_()
        
    def abrir_stack(self):
        self.ventana_stack = pilaLista()
        self.ventana_stack.exec_()