from functions import *

def run():
    lista_pacientes = LinkedList()
    
    end = False
    selection = 0

    while not end:
        print("\n------------ Menú ------------\n  1. Cargar archivo\n  2. Seleccionar Paciente\n  3. Generar Archivo XML\n  4. Salir")
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
            if lista_pacientes.length()>0:
                valuarPacientes(lista_pacientes)
                generarXml(lista_pacientes)
            else:
                print("Lista vacía")
                
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()