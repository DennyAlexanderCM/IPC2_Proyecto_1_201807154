from xml.dom import minidom
from tkinter import filedialog
from linked_list import LinkedList
from linked_list_dates import LinkedListDates
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
        # CREAMOS EL OBJETO PACIENTE
        paciente_obj = Paciente(nombre, edad)
        rejillas = paciente.getElementsByTagName("celda")

        lista_datos = LinkedListDates()
        lista_datos.periodo = int(periodos)
        lista_datos.dimension = int(m)

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

        lista_datos.append(lista)    
        paciente_obj.lista_datos = lista_datos
        
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
        print("\n============ Menú ============\n 1. Ejecuar periodos establecidos\n 2. Ejecutar periodos N\n 3. Regresar")
        selection = pedirNumeroEntero()    
        
        if selection == 1:
            
            i = 1
            lista:LinkedListDates = paciente.getDatoLista()
            aux:Lista_Ortogonal = lista.head.data
            #IMPRIMIMOS LA LISTA ORIGINAL
            aux.printDates(paciente.getNombre())
            while i <= lista.periodo:
                aux = aux.analizarDatos()
                aux.periodo = i

                print(aux.periodo)
                aux.printDates(paciente.getNombre())
                lista.append(aux)
                i+=1

        elif selection == 2:
            paciente.datos.printDates()
        elif selection == 3:
            end = True
        else:
            print("Intente de nuevo")

def compareDates(matriz_1:Lista_Ortogonal, matriz_2:Lista_Ortogonal):
    valor = False 
    m = matriz_1.length()
    for i in range(m):
            for j in range(m):
                a = matriz_1.searchDate(i+1, j+1)
                b = matriz_2.searchDate(i+1, j+1)
                if a != b:
                    valor = True
                    break
    return valor