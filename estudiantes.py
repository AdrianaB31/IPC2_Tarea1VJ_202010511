#IMPORTAR CLASE PADRE
from usuario import Usuario

#CREACION DE LA CLASE PROFESORES
#HERENCIA -> class nombre_clase_hijo(nombre_clase_padre):
class Estudiantes(Usuario):
    def __init__(self, nombre, curso, carnet, carrera):
        super().__init__(nombre, curso)
        self.carnet = carnet
        self.carrera = carrera 

    def getCarnet(self):
        return self.carnet

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera


