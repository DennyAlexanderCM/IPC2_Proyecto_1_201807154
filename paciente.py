class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.rejilla_1 = None
        self.periodos = 0
        self.estado = None
        #PERIODO EN QUE SE REPITE EL PATRON INICIAL
        self.N = 0
        #PERIODO EN QUE SE REPITE EL PATRON NUEVO
        self.N1 = 0
        #DIMENSIÓN DE LA MATRIZ
        self.m = 0
    
    def getEdad(self):
        return self.edad
    
    def getNombre(self):
        return self.nombre
    
    def getEstado(self):
        return self.estado

    def getDatos(self):
        return self.rejilla_1
    
    def getPeriodos(self):
        return self.periodos
    
    def getN(self):
        return self.N
    
    def getN1(self):
        return self.N1
    
    def getM(self):
        return self.m
    
    def setEdad(self, edad):
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEstado(self, estado):
        self.estado = estado

    def setDatos(self, datos):
        self.rejilla_1 = datos
    
    def setPeriodos(self, periodos):
        self.periodos = periodos
    
    def setN(self, N):
        self.N = N

    def setN1(self, N1):
        self.N1 = N1
    
    def setM(self, m):
        self.m = m
