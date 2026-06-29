from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    #Inserta un elemento
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node       


    def pop(self):
        if self.top is None:     
            return None          
        else:
            popped_value = self.top.data  
            self.top = self.top.next     
            return popped_value          

    def top_of_stack(self):
        if self.top is None:     
            return None
        valor = self.top.data   
        return valor

    def print_stack(self):
        temp = self.top
        while temp is not None:   
            print(temp.data)
            temp = temp.next      
        
        
        
