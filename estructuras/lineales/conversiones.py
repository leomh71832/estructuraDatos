from estructuras.lineales.stack import Stack

class ConversorExpresion:
    def __init__(self):
        self.pila_operadores = Stack()
        
    def _obtener_precedencia(self, operador):
        """Asigna la jerarquía de operadores solicitada (+, -, *, /, $)."""
        if operador == '$':
            return 3
        elif operador in ('*', '/'):
            return 2
        elif operador in ('+', '-'):
            return 1
        return 0  

    def convertir_infija_a_posfija(self, expresion_infija):
        lista_posfija = []
        
        expresion_limpia = expresion_infija.replace(" ", "")
        
        for elemento in expresion_limpia:
            
            if elemento.isalnum():
                lista_posfija.append(elemento)
                
            elif elemento == '(':
                self.pila_operadores.push(elemento)
                
            elif elemento == ')':
                while (not self.pila_operadores.is_empty() and 
                       self.pila_operadores.top_of_stack() != '('):
                    lista_posfija.append(self.pila_operadores.pop())
                
                if not self.pila_operadores.is_empty():
                    self.pila_operadores.pop()
                    
            elif elemento in ('+', '-', '*', '/', '$'):
                while (not self.pila_operadores.is_empty() and 
                       self._obtener_precedencia(self.pila_operadores.top_of_stack()) >= self._obtener_precedencia(elemento)):
                    lista_posfija.append(self.pila_operadores.pop())
                
                self.pila_operadores.push(elemento)

        while not self.pila_operadores.is_empty():
            lista_posfija.append(self.pila_operadores.pop())
            
        return " ".join(lista_posfija)