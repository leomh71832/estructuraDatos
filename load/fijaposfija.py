from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.lineales.conversiones import ConversorExpresion

class VentanaConversor(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/conversion.ui", self) 
        
        self.logica = ConversorExpresion()
        self.boton.clicked.connect(self.ejecutar_conversion)

    def ejecutar_conversion(self):
        infija = self.fija.text()
        
        if not infija.strip():
            QMessageBox.warning(self, "Error", "Por favor ingrese una expresión.")
            return
            
        try:
            resultado = self.logica.convertir_infija_a_posfija(infija)
            self.resultado.setText(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error en la conversión: {str(e)}")