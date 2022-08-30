#CABEZA PRINCIPAL
class Nodo_Head():
    def __init__(self, position):
        #DEFINE LA POSICION EN LA FILA O COLUMNA
        self.position= position
        self.nref = None
        self.pref = None
        #APUNTA A LOS NODOS DE LA MATRIZ
        self.access = None

#LISTA QUE CONTEDRA LOS ENCABEZADOS DE LA FILA Y COLUMNA DE LA MATRIZ
class Lista_Encabezado():
    def __init__(self):
        self.start_node: Nodo_Head = None
        self.final_node: Nodo_Head = None

    def insert_node(self, node: Nodo_Head):
        #SE VERIFICA SI LA LISTA ESTA VACÍA
        if self.start_node == None:
            self.start_node = node
            self.final_node = node
        #EN CASO CONTRARIO
        else:
            if node.position < self.start_node.position:   
                node.nref = self.start_node
                self.final_node.pref = node
                self.start_node = node
            elif node.position > self.final_node.position:
                self.final_node.nref = node
                node.pref = self.final_node
                self.final_node = node
            else:
                aux: Nodo_Head = self.start_node 
                while aux:
                    if (node.position < aux.position):
                        node.nref = aux
                        node.pref = aux.pref
                        aux.pref.nref = node
                        aux.pref = node
                        break
                    aux = aux.nref                

    def getHead(self, position):
        aux = self.start_node
        while aux:
            if position == aux.position:
                return aux
            aux = aux.nref
        return None

class Nodo_Contendor():
    def __init__(self, positionX, positionY, data):
        self.data = data
        self.positionX = positionX
        self.positionY = positionY
        self.up = None
        self.down = None
        self.right = None
        self.left = None

class Lista_Ortogonal():
    def __init__(self):
        self.filas = Lista_Encabezado()
        self.columnas = Lista_Encabezado()
        self.periodos = 0
    
    #MÉTODO PARA INGRESAR UN NUEVO NODO EN LA POSICION X Y Y
    def insert(self, pos_x, pos_y, data):
        #SE CREA EL NODO QUE CONTENDRA EL DATO
        nuevo = Nodo_Contendor(pos_x, pos_y, data)
        nodo_X = self.columnas.getHead(pos_x)
        nodo_Y = self.filas.getHead(pos_y)

        if nodo_Y == None:
            nodo_Y = Nodo_Head(pos_y)
            nodo_Y.access = nuevo
            self.filas.insert_node(nodo_Y)
        else:
            if nuevo.positionX < nodo_Y.access.positionX:
                nuevo.right = nodo_Y.access
                nodo_Y.access.left = nuevo
                nodo_Y.access = nuevo
            else:
                tmp : Nodo_Contendor = nodo_Y.access
                while tmp:
                    if nuevo.positionX < tmp.positionX:
                        nuevo.right = tmp
                        nuevo.left = tmp.right
                        tmp.left.right = nuevo
                        tmp.left = nuevo
                        break
                    elif nuevo.positionX == tmp.positionX and nuevo.positionY == tmp.positionY:
                        if nodo_Y.access == tmp:
                            nuevo.right = nodo_Y.access
                            nodo_Y.access.left = nuevo
                            nodo_Y.access = nuevo
                        else:
                            tmp.left.right = nuevo
                            nuevo.left = tmp.left
                            nuevo.right = tmp.right
                            if tmp.right != None:
                                tmp.right.left = nuevo
                            break
                    else:
                        if tmp.right == None:
                            tmp.right = nuevo
                            nuevo.left = tmp
                            break
                    tmp = tmp.right

        if nodo_X == None:
            nodo_X = Nodo_Head(pos_x)
            nodo_X.access = nuevo
            self.columnas.insert_node(nodo_X)
        else:
            if nuevo.positionY < nodo_X.access.positionY:
                nuevo.down = nodo_X.access              
                nodo_X.access.up = nuevo
                nodo_X.acceso = nuevo
            else:
                tmp : Nodo_Contendor = nodo_X.access
                while tmp:
                    if nuevo.positionY < tmp.positionY:
                        nuevo.down = tmp
                        nuevo.up = tmp.up
                        tmp.up.down = nuevo
                        tmp.up = nuevo
                        break
                    #EN CASO YA SE HAYA CREADO LA POSICION REEMPLAZAMOS SU VALOR
                    elif nuevo.positionX == tmp.positionX and nuevo.positionY == tmp.positionY:
                        if nodo_X.access == tmp:
                            nuevo.down = nodo_X.access
                            nodo_X.access.up = nuevo
                            nodo_X.acceso = nuevo
                        else:
                            tmp.up.down = nuevo
                            nuevo.up = tmp.up
                            nuevo.down = tmp.down
                            if tmp.down != None:
                                tmp.down.up = nuevo
                            break
                    else:
                        if tmp.down == None:
                            tmp.down = nuevo
                            nuevo.up = tmp
                            break
                    tmp = tmp.down 

    def imprimirLista(self):
        aux = self.filas.start_node
        while aux:
            txt=""
            pivote:Nodo_Contendor = aux.access
            while pivote:
                txt += str(pivote.data)+"\t"
                pivote = pivote.right
            print(txt)
            aux = aux.nref
        print("fin")
    
    def searchNode(self, positionX, positionY):
        aux_1 = self.filas.start_node

        while aux_1:
            if aux_1.position == positionY:
                pivote:Nodo_Contendor = aux_1.access
                while pivote:
                    if pivote.positionX == positionX:
                        return pivote
                    pivote = pivote.right
            aux_1 = aux_1.nref
        return None
    
    def analizarDatos(self):
        aux_1 = self.filas.start_node
        aux_2 = Lista_Ortogonal()
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                sana = 0
                enferma = 0
                #si existe izquierda
                if pivote.left:
                    dato_rejilla = pivote.left.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.right:
                    dato_rejilla = pivote.right.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.up:
                    dato_rejilla = pivote.up.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.down:
                    dato_rejilla = pivote.down.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                #--------------------------------
                if pivote.left and pivote.up and pivote.left.up:
                    dato_rejilla = pivote.left.up.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.right and pivote.up and pivote.right.up:
                    dato_rejilla = pivote.right.up.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.left and pivote.down and pivote.left.down:
                    dato_rejilla = pivote.left.down.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                if pivote.right and pivote.down and pivote.right.down:
                    dato_rejilla = pivote.right.down.data
                    if dato_rejilla == 0:
                        sana += 1
                    else:
                        enferma += 1
                
                if pivote.data == 0:
                    if enferma == 3:
                        aux_2.insert(pivote.positionX, pivote.positionY, 1)
                    else:
                        aux_2.insert(pivote.positionX, pivote.positionY, 0)
                else:
                    if enferma == 3 or enferma == 2:
                        aux_2.insert(pivote.positionX, pivote.positionY, 1)
                    else:
                        aux_2.insert(pivote.positionX, pivote.positionY, 0)
                pivote = pivote.right
            aux_1 = aux_1.nref

        return aux_2

