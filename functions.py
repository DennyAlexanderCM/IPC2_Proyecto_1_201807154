from xml.dom import minidom
from tkinter import filedialog
from linked_list import LinkedList
from paciente import Paciente
from list_container import Lista_Ortogonal 

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num  

def leerArchivo():
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    if root != "":
        return root
    return None

def lecturaArchivosXml(data):
    #LISTA QUE CONTRENDRÁ CADA PACIENTE
    pacientes_lista = LinkedList()
    doc = minidom.parse(data)

    # Elemento raíz del documento
    rootNode = doc.documentElement
    # Obtenemos cada elemento con la etiqueta paciente
    pacientes = rootNode.getElementsByTagName("paciente")
    
    for paciente in pacientes:
        # OTENEMOS EL NOMBRE DEL PACIENTE  
        nombre = paciente.getElementsByTagName("nombre")[0].firstChild.data
        # OTENEMOS LA EDAD DEL PACIENTE
        edad = paciente.getElementsByTagName("edad")[0].firstChild.data
        # OTENEMOS EL NÚMERO DE PERIODOS
        periodos = paciente.getElementsByTagName("periodos")[0].firstChild.data
        # OTENEMOS LA DIMENSIÓN DE LA REJILLA
        m = paciente.getElementsByTagName("m")[0].firstChild.data
        rejillas = paciente.getElementsByTagName("celda")

        # CREAMOS EL OBJETO PACIENTE
        paciente_obj = Paciente(nombre, edad)
        paciente_obj.setPeriodos(int(periodos))
        paciente_obj.setM(int(m))
        # CREAMOS LA LISTA ORTOGONAL QUE CONTENDRÁ LAS REJILLAS
        lista = Lista_Ortogonal()
        
        #Llenamos la lista con los 0
        for i in range(int(m)):
            for j in range(int(m)):
                lista.insert(i+1, j+1, 0)
        
        # INSERTAMOS LOS DATOS A LA MATRIZ ORTOGONAL
        for rejilla in rejillas:
            date_f = rejilla.getAttribute("f")
            date_c = rejilla.getAttribute("c")
            lista.insert(int(date_c), int(date_f), 1)

        paciente_obj.rejilla_1 = lista
        
        pacientes_lista.append(paciente_obj)
    
    print("Datos cargadodos...")

    return pacientes_lista

def pacientes_opciones(lista:LinkedList):
    aux = lista.head
    print("\n------ Seleccione paciente ------")
    i = 1
    while aux:
        print(str(i)+". "+aux.data.getNombre())
        aux = aux.next
        i+=1
    
    num = pedirNumeroEntero()
    if num <= i and num > 0:
        date = lista.searchDate(num)
        if date:
            paciente = lista.searchDate(num)
            paciente_opciones(paciente)
        else:
            print("No encontrado")
    else:
        print("¡Ingrese una opción correcta!")

def paciente_opciones(paciente: Paciente):
    
    end = False
    selection = 0
    while not end:
        print("\n------------ Menú ------------\n 1. Ejecuar periodos establecidos\n 2. Ejecutar periodos N\n 3. Regresar")
        selection = pedirNumeroEntero()    
        
        if selection == 1:
            paciente.valuado = True
            i = 1
            lista = LinkedList()
            aux:Lista_Ortogonal = paciente.getDatos()
            
            lista.append(aux)
            encontrado = False

            while i <= paciente.getPeriodos():
                aux = aux.analizarDatos()
                aux.periodo = i
                resultado = lista.compararDatos(aux)
                if resultado == None:
                    lista.append(aux)
                    i+=1
                else:
                    if resultado == 0:
                        N = i - resultado
                        if N > 1:
                            lista.append(aux)
                            paciente.setEstado("Grave")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N :" + str(i))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            lista.append(aux)
                            paciente.setEstado("Mortal")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado:")
                            print(" N: " + str(i))
                            print(" Enfermedad: caso incurable")
                    else:
                        N = i - resultado
                        if N > 1:
                            lista.append(aux)
                            paciente.setEstado("Grave")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            lista.append(aux)
                            paciente.setEstado("Mortal")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso incurable")
                    encontrado = True
                    break
            
            if not encontrado:
                print("\nPaciente: "+paciente.getNombre())
                paciente.setEstado("Leve")
                print("Patron no se repite")
                print("Enfermedad: caso leve")


            #IMPRIME LOS DATOS GENERADOS
            printList(lista, paciente)

        elif selection == 2:
            paciente.valuado = False
            i = 1
            lista = LinkedList()
            aux:Lista_Ortogonal = paciente.getDatos()
            lista.append(aux)
            encontrado = False

            while i <= 10000:
                aux = aux.analizarDatos()
                aux.periodo = i
                resultado = lista.compararDatos(aux)
                if resultado == None:
                    lista.append(aux)
                    i+=1
                else:
                    if resultado == 0:
                        N = i - resultado
                        if N > 1:
                            lista.append(aux)
                            paciente.setEstado("Grave")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N :" + str(i))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            lista.append(aux)
                            paciente.setEstado("Mortal")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado:")
                            print(" N: " + str(i))
                            print(" Enfermedad: caso incurable")
                    else:
                        N = i - resultado
                        if N > 1:
                            lista.append(aux)
                            paciente.setEstado("Grave")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            lista.append(aux)
                            paciente.setEstado("Mortal")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso incurable")
                    encontrado = True
                    break
            
            if not encontrado:
                print("\nPaciente: "+paciente.getNombre())
                paciente.setEstado("Leve")
                print("Patron no se repite")
                print("Enfermedad: caso leve")


            #IMPRIME LOS DATOS GENERADOS
            printList(lista, paciente)

        elif selection == 3:
            end = True

def printList(lista: LinkedList, paciente:Paciente):
    name = paciente.getNombre()
    #Periodo en que el pareon inicial se repite
    n = paciente.getN()
    #Periodo en que el patron nuevo se repite
    n1 = paciente.getN1()
    
    aux = lista.head

    if aux:
        aux.data.printDatesInit(name)
        aux = aux.next
        while aux:
            aux.data.printDates(name, n, n1)
            aux = aux.next

def generarXml(lista:LinkedList):
    f = open("Datos generales.xml","w+", encoding="utf-8")
    aux = lista.head
    doc = minidom.Document()
    pacientes = doc.createElement('pacientes')
    doc.appendChild(pacientes)

    while aux:
        paciente_datos:Paciente = aux.data
        paciente = doc.createElement('paciente')
        datospersonales = doc.createElement('datospersonales')
        nombre = doc.createElement('nombre')
        nombre.appendChild(doc.createTextNode(paciente_datos.getNombre()))
        datospersonales.appendChild(nombre)
        edad = doc.createElement('edad')
        edad.appendChild(doc.createTextNode(str(paciente_datos.getEdad())))
        datospersonales.appendChild(edad)
        paciente.appendChild(datospersonales)

        periodos = doc.createElement('periodos')
        periodos.appendChild(doc.createTextNode(str(paciente_datos.getPeriodos())))
        paciente.appendChild(periodos)

        m = doc.createElement('m')
        m.appendChild(doc.createTextNode(str(paciente_datos.getM())))
        paciente.appendChild(m)

        resultado = doc.createElement('resultado')
        resultado.appendChild(doc.createTextNode(paciente_datos.getEstado()))
        paciente.appendChild(resultado)

        if paciente_datos.getN() != 0:
            n = doc.createElement('n')
            n.appendChild(doc.createTextNode(str(paciente_datos.getN())))
            paciente.appendChild(n)
        
        if paciente_datos.getN1() != 0:
            n1 = doc.createElement('n1')
            n1.appendChild(doc.createTextNode(str(paciente_datos.getN1())))
            paciente.appendChild(n1)

        pacientes.appendChild(paciente)
        aux = aux.next
    xml = doc.toprettyxml(indent = '   ')
    print (xml)
    f.write(xml)
    print("Realizado")

def valuarPacientes(lista:LinkedList):
    print("Efectuando análisis a pacientes faltantes")

    aux = lista.head
    while aux:
        if aux.data.valuado is False:
            paciente:Paciente = aux.data
            i = 1
            lista = LinkedList()
            aux_2:Lista_Ortogonal = paciente.getDatos()
            
            lista.append(aux_2)
            encontrado = False

            while i <= paciente.getPeriodos():
                aux_2 = aux_2.analizarDatos()
                aux_2.periodo = i
                resultado = lista.compararDatos(aux_2)
                if resultado == None:
                    lista.append(aux_2)
                    i+=1
                else:
                    if resultado == 0:
                        N = i - resultado
                        if N > 1:
                            aux_2.repetido = True
                            lista.append(aux_2)
                            paciente.setEstado("Grave")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N :" + str(i))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            aux_2.repetido = True
                            lista.append(aux_2)
                            paciente.setEstado("Mortal")
                            paciente.setN(N)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado:")
                            print(" N: " + str(i))
                            print(" Enfermedad: caso incurable")
                    else:
                        N = i - resultado
                        if N > 1:
                            aux_2.repetido = True
                            lista.append(aux_2)
                            paciente.setEstado("Grave")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso grave")
                            
                        elif N == 1:
                            aux_2.repetido = True
                            lista.append(aux_2)
                            paciente.setEstado("Mortal")
                            paciente.setN(resultado)
                            paciente.setN1(i-resultado)
                            print("\nPaciente: "+paciente.getNombre())
                            print("Encontrado: ")
                            print(" N: " + str(resultado))
                            print(" N1: " + str(i-resultado))
                            print(" Enfermedad: caso incurable")
                    encontrado = True
                    break
            
            if not encontrado:
                paciente.setEstado("Leve")
                paciente.setN(0)
                paciente.setN1(0)
                print("\nPaciente: "+paciente.getNombre())
                print("Patron no se repite")
                print("Enfermedad: caso leve")
        aux = aux.next
