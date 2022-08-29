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
    paciente_lista = LinkedList()
    doc = minidom.parse(data)

    # Elemento raíz del documento
    rootNode = doc.documentElement
    # Obtenemos cada elemento con la etiqueta paciente
    pacientes = rootNode.getElementsByTagName("paciente")
    
    for paciente in pacientes:
        # creamos el objeto paciente     
        nombre = paciente.getElementsByTagName("nombre")[0].firstChild.data
        edad = paciente.getElementsByTagName("edad")[0].firstChild.data
        periodos = paciente.getElementsByTagName("periodos")[0].firstChild.data
        m = paciente.getElementsByTagName("m")[0].firstChild.data
        # creamos el objeto paciente
        paciente_obj = Paciente(nombre, edad)
        rejillas = paciente.getElementsByTagName("celda")
        lista = Lista_Ortogonal()
        
        #Llenamos la lista con los 0
        for i in range(int(m)):
            for j in range(int(m)):
                lista.insert(i+1, j+1, 0)
        
        for rejilla in rejillas:
            date_f = rejilla.getAttribute("f")
            date_c = rejilla.getAttribute("c")
            lista.insert(int(date_c), int(date_f), 1)
        
        paciente_obj.datos = lista
        
        paciente_lista.append(paciente_obj)