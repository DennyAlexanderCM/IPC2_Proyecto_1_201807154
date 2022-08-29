from functions import *
from linked_list import LinkedList

#VARIABLES GLOVALES
pacientes = LinkedList()

def run():
    
    end = False
    selection = 0

    while not end:
        print("\n============ Menú ============\n 1. Cargar archivo\n 2. Seleccionar Paciente\n 3. Other\n 4. Salir")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            rute = leerArchivo()
            1
            if rute != None:
                lecturaArchivosXml(rute)
            else:
                print("No se realizaron cambios")

        elif selection == 2:
            pass
        elif selection == 3:
            pass
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()