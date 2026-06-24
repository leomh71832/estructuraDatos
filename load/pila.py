from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.stack import Stack 

class pilaLista(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/pila.ui", self)
        
        self.lista = Stack()
         
        self.push_1.clicked.connect(self.metodo_push)
        self.pop_2.clicked.connect(self.metodo_pop)
        self.top.clicked.connect(self.metodo_top)
        self.imprimir.clicked.connect(self.metodo_print)
        
    def metodo_push(self):
        dato = self.dato.text() 
        
        if dato.strip() == "":
            QMessageBox.warning(self, "Error")
            return
            
        self.lista.push(dato)
        
        self.respuesta.setText(dato)

    def metodo_pop(self):
        valor_eliminado = self.lista.pop()
        
        if valor_eliminado is None:
            QMessageBox.information(self, "Pila Vacía", "No hay elementos para eliminar.")
        else:
            self.respuesta.setText(f"Eliminado: {valor_eliminado}")

    def metodo_top(self):
        valor_tope = self.lista.top_of_stack()
        
        if valor_tope is None:
            QMessageBox.information(self, "Pila Vacía", "La pila está vacía.")
        else:
            self.respuesta.setText(f"En el tope: {valor_tope}")

    def metodo_print(self):
        if self.lista.top is None:
            self.respuesta.setText("La pila está vacía.")
            return

        texto_pila = "la Pila es de:\n"
        temp = self.lista.top
        
        while temp is not None:
            texto_pila += f"[ {temp.data} ]\n" 
            temp = temp.next

        self.respuesta.setText(texto_pila)