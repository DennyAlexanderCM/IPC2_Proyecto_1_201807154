from functions import *

lista_pacientes = LinkedList()

def run():
    
    end = False
    selection = 0

    while not end:
        print("\n============ Menú ============\n 1. Cargar archivo\n 2. Seleccionar Paciente\n 3. Other\n 4. Salir")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            rute = leerArchivo()
            if rute != None:
                lista_pacientes =  lecturaArchivosXml(rute)
            else:
                print("No se realizaron cambios")

        elif selection == 2:
            pacientes_opciones(lista_pacientes)
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