class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.lista_datos = None
        self.estado = None
    
    def getEdad(self):
        return self.edad
    
    def getNombre(self):
        return self.nombre
    
    def getDatoLista(self):
        return self.lista_datos
    
    def getEstado(self):
        return self.estado