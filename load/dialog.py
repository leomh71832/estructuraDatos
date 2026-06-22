from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.lista_enlazada_simple import LinkedList 

class VentanaLista(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialog.ui", self)
        
        self.lista = LinkedList()
         
        self.inicio.clicked.connect(self.accionInsertarInicio)
        self.final_2.clicked.connect(self.accionInsertarFin)
        self.buscar.clicked.connect(self.accionBuscar)
        self.eliminar.clicked.connect(self.accionEliminarInicio)
        self.borrar.clicked.connect(self.accionEliminarFin)
        
    def actualizarPantalla(self):
        """Método auxiliar para redibujar la lista en la interfaz cada vez que cambie"""
        temp = self.lista.head
        texto_lista = "Head -> "
        while temp is not None:
            texto_lista += f"{temp.data} -> "
            temp = temp.next
        texto_lista += "<- Tail"
        
        self.respuesta.setText(texto_lista)
        
    def accionInsertarInicio(self):
        dato = self.dato.text()
        self.lista.insert_at_beginning(dato)
        self.actualizarPantalla()
        
    def accionInsertarFin(self):
        dato = self.dato.text()
        self.lista.insert_at_end(dato)
        self.actualizarPantalla()
        
    def accionBuscar(self):
        dato = self.dato.text()
        encontrado = self.lista.search(dato)
        
        if encontrado:
            self.respuesta.setText(f"¡El dato '{dato}' sí está en la lista!")
        else:
            self.respuesta.setText(f"El dato '{dato}' no se encontró.")
            
    def accionEliminarInicio(self):
        self.lista.delete_at_beginning(None)
        self.actualizarPantalla()
        
    def accionEliminarFin(self):
        self.lista.delete_at_end(None)
        self.actualizarPantalla()