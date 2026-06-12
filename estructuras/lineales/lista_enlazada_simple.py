from estructuras.lineales.nodo import nodo

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
          
    def insert_at_beginning(self, data):
        # paso 1 crear un nuevo nodo con el dato proporcionado
        new_node = None(data)
        
        #paso 2 verificar q la lista este vacia 
        if self.head is None and self.tail is None:
            #si la lista esta vacia el new nodo se convierte en el primero
            self.head = new_node
            self.tail = new_node
        else:
            #si la lista no esta vacia el new nodo apunta a la cabeza actual 
            new_node.next = self.head
            #la cabeza se actualiza para ser el 1 nodo
            self.head = new_node
            
    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next 
        print("<- Tail")
        
        
            