#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#CLASE DE LA LISTA ENLAZADA PARA GUARGAR LOS PATRONES DE CADA PISO
class LinkedList:
    def __init__(self):
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
    
    def compararDatos(self, matriz_1):
        aux = self.head
        while aux:
            matriz_2 = aux.data
            value = self.compareDates(matriz_1, matriz_2)
            if value:
                return matriz_2.periodo
            aux = aux.next
        return None

    def compareDates(self, matriz_1, matriz_2):
        valor = True
        m = matriz_1.length()
        for i in range(m):
                for j in range(m):
                    a = matriz_1.searchDate(i+1, j+1)
                    b = matriz_2.searchDate(i+1, j+1)
                    if a != b:
                        valor = False
                        break
        return valor
