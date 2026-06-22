from estructuras.lineales.lista_enlazada_simple import LinkedList

class MenuListaEnlazada(object):
    def __init__(self):
        self.lista_enlazada = LinkedList()

    def mostrar_menu(self):
        print("\n    MENÚ PRINCIPAL    ")
        print("1. Insertar Inicio")
        print("2. Insertar Final")
        print("3. Buscar")
        print("4. Mostrar Lista")
        print("5. Eliminar Inicio")
        print("6. Eliminar Final")
        print("7. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == "1":
            elemento = input("Ingrese elemento a agregar: ")
            self.lista_enlazada.insert_at_beginning(elemento)
            print(f"Elemento '{elemento}' agregado al inicio de la lista.")
            
        elif opcion == "2":
            elemento = input("Ingrese elemento a agregar al final: ")
            self.lista_enlazada.insert_at_end(elemento)
            print(f"Elemento '{elemento}' agregado al final de la lista.")
            
        elif opcion == "3":
            elemento = input("Ingrese elemento a buscar: ")
            encontrado = self.lista_enlazada.search(elemento)
            if encontrado:
                print(f"Elemento '{elemento}' encontrado en la lista.")
            else:
                print(f"Elemento '{elemento}' no encontrado en la lista.")
                 
        elif opcion == "4":
            print("Contenido de la lista enlazada:")
            self.lista_enlazada.print_linked_list()
            
        elif opcion == "5":
            elemento = input("¿Confirmar eliminar inicio?")
            self.lista_enlazada.delete_at_beginning(elemento) 
            print("Elemento inicial eliminado.")
            
        elif opcion == "6":
            elemento = input("¿Confirmar eliminar final?")
            self.lista_enlazada.delete_at_end(elemento)
            print("Elemento final eliminado.")
                
        elif opcion == "7":
            print("Saliendo del menú. ¡Hasta luego!")
            
        else:
            print("Opción inválida. Elige un número del 1 al 7.")
                
    def iniciar(self):
        while True:
            self.mostrar_menu()
            # Dejar la opción como string (texto) evita problemas de conversión
            opcion = input("Seleccione una opción: ")
            
            self.ejecutar_opcion(opcion)
            
            # Si el usuario eligió 7, rompemos el bucle While desde aquí
            if opcion == "7":
                break
