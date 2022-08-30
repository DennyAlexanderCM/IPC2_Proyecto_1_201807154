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
        # CREAMOS EL OBJETO PACIENTE
        paciente_obj = Paciente(nombre, edad)
        rejillas = paciente.getElementsByTagName("celda")
        # CREAMOS LA LISTA ORTOGONAL QUE CONTENDRÁ LAS REJILLAS
        lista = Lista_Ortogonal()
        lista.periodos = int(periodos)
        
        #Llenamos la lista con los 0
        for i in range(int(m)):
            for j in range(int(m)):
                lista.insert(i+1, j+1, 0)
        
        # INSERTAMOS LOS DATOS A LA MATRIZ ORTOGONAL
        for rejilla in rejillas:
            date_f = rejilla.getAttribute("f")
            date_c = rejilla.getAttribute("c")
            lista.insert(int(date_c), int(date_f), 1)
        paciente_obj.datos = lista
        
        pacientes_lista.append(paciente_obj)
    
    print("Datos cargadodos...")

    return pacientes_lista

def pacientes_opciones(lista:LinkedList):
    aux = lista.head
    print("\n===== Seleccione paciente =====")
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
            lista_previa  = LinkedList()
            print(paciente.getNombre(), paciente.getDatos().periodos)
            
            i = 1
            lista = paciente.getDatos()
            aux:Lista_Ortogonal = lista.analizarDatos()
            lista_previa.append(aux)
            while i < paciente.getDatos().periodos:
                aux = aux.analizarDatos()
                lista_previa.append(aux)
                i+=1
            paciente.lista_datos = lista_previa

        elif selection == 2:
            pass
        elif selection == 3:
            end = True
        else:
            print("Intente de nuevo")


