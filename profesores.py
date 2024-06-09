#IMPORTAR CLASE PADRE
from usuario import Usuario

#CREACION DE LA CLASE PROFESORES
#HERENCIA -> class nombre_clase_hijo(nombre_clase_padre):
class Profesores(Usuario):
    def __init__(self, nombre, curso, codigo, profesion):
        super().__init__(nombre, curso)
        self.codigo = codigo 
        self.profesion = profesion
    
    def getCodigo(self):
        return self.codigo
    
    def setCodigo(self, codigo):
        self.codigo = codigo

    def getProfesion(self):
        return self.profesion
    
    def setProfesion(self, profesion):
        self.profesion = profesion
    

