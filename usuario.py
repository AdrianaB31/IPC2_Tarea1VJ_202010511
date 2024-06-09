#CLASE USURIOS PADRE
class Usuario():
    #CONSTRUCTOR
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
    
    #METOS Y ENCAPSULAMIENTO 

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCurso(self):
        return self.curso
    
    def setCurso(self, curso):
        self.curso = curso
    
