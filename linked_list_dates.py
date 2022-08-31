#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#CLASE DE LA LISTA ENLAZADA PARA GUARGAR LOS PATRONES DE CADA PISO
class LinkedListDates:
    def __init__(self):
        self.dimension = 0
        self.periodo = 0
        self.head = None
        self.last = None

    # VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head
    
    # AGREGAMOS LOS DATOS AL FINAL
    def append(self, data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            nodo.prev = self.last
            self.last = nodo
    
    # RETORNAR EL NÚMERO DE ELEMENTOS
    def length(self):
        n = 0
        i = self.head
        while i:
            i = i.next
            n+=1
        return n

    def print(self):
        aux = self.head
        while aux:
            prev = aux.data
            print(prev.getPositionX(), prev.getPositionY(),prev.getValue())
            aux = aux.next

    # BUSCAMOS UN DATO EN ESPECIFICO POR SU POSICION
    def searchDate(self, selection):
        n = 1
        i = self.head
        while i:
            if selection == n:
                return i.data
            else:
                n +=1 
                i = i.next  
        return False
