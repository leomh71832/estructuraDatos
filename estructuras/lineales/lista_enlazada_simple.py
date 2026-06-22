from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacía, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            #Luego, la cabeza se actualiza para ser el nuevo nodo
            self.head = new_node
    
    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        while temp is not None:
            print(temp.data,"->", end="")
            temp = temp.next
        print("<- Tail")
        
        
        
    def insert_at_end(self,data):
        new_node = Node (data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
            
            
    def search (self, data):
        current_node = self.head 
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next 
        return False
    
    
    def delete_at_beginning(self,data):
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            
            
    def delete_at_end(self,data):
        if  self.head == None and self.tail == None:
            print("No hay nodos")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next=None
                self.tail = temp
