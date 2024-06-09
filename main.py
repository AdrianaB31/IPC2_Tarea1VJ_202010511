#IMPORTAR LAS CLASES DE PROFESORES Y ESTUDIANTES
from profesores import Profesores
from estudiantes import Estudiantes

#Lista de profesore
profesores = []
#Lista de alumnos 
estudiantes = []


#Menu principal 
def menuPrincipal():
    opcion = 0
    while True: 
        print("---------------MENU PRINCIPAL---------------")
        print("-  1. CRUD de Profesores                   -")
        print("-  2. CRUD de Estudiantes                  -")
        print("-  3. Salir                                -")
        print("--------------------------------------------")
        opcion = int(input("Ingrese una opcion: "))
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    menuProfesores()  # Llama a la función del menú de profesores
                case 2:
                    menuEstudiantes()  # Llama a la función del menú de estudiantes
                case 3:
                    print("¡Hasta luego!")
                    break                    
                case _:
                    print("Opcion no valida.")
        except:
            print("[Error] Ingreso una opcion invalida")

#MENU PROFESORES
def menuProfesores():
    opcion = 0
    while True: 
        print()
        print("---------------MENU PROFESORES---------------")
        print("-  1. Crear Profesor                        -")
        print("-  2. Leer Profesor                         -")
        print("-  3. Actualizar Profesor                   -")
        print("-  4. Eliminar Profesor                     -")
        print("-  5. Regresar al menu principal            -")
        print("---------------------------------------------")
        opcion = int(input("Ingrese una opcion: "))
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    crearProfesores()
                case 2:
                    leerProfesores()
                case 3:
                    actualizarProfesores()
                case 4:
                    eliminarProfesor()
                case 5:
                    break
                case _:
                    print()
                    print("Opcion no valida.")
        except:
            print()
            print("[Error] Ingreso una opcion invalida")

#funcion de crear POFESORES
def crearProfesores():
    print()
    global profesores 
    print('---------------CREAR PROFESOR---------------')
    nombre = input('Ingrese el nombre del profesor: ')
    curso = input('Ingrese el curso del profesor: ')
    codigo = input('Ingrese el codigo del profesor: ')
    profesion = input('Ingrese la profesion del profesor: ')
    nuevo = Profesores(nombre, curso, codigo, profesion)
    profesores.append(nuevo)
    print()
    print("Profesor creado exitosamente.")
    print()

#funcion para leer profesores
def leerProfesores():
    print()
    global profesores
    print('--------------LEER PROFESORES--------------')
    if len(profesores) == 0:
        print('No hay profesores registrados en el programa.')
        
    for profesor in profesores:
        json_string = '''
{
    codigo: '''+str(profesor.getCodigo())+''',
    nombre: '''+profesor.getNombre()+''',
    curso: '''+profesor.getCurso()+''',
    profesion: '''+profesor.getProfesion()+'''
}
'''
        print(json_string)

def actualizarProfesores():
    print()
    global profesores
    codigo = input('Ingrese el codigo del profesor a actualizar: ')
    for profesor in profesores:
        if profesor.getCodigo() == codigo:
            nombre = input('Ingrese el nuevo nombre del profesor: ')
            profesor.setNombre(nombre)
            curso = input('Ingrese el nuevo curso del profesor: ')
            profesor.setCurso(curso)
            profesion = input('Ingrese la nueva profesion del profesor: ')
            profesor.setProfesion(profesion)
            print("Profesor actualizado exitosamente.")
            return
        
    print("Error: No se encontró un profesor con ese código.")
    

#Eliminar profesor 
def eliminarProfesor():
    global profesores
    codigo = input('Ingrese el codigo del profesor a eliminar: ')
    for profesor in profesores:
        if profesor.getCodigo() == codigo:
            profesores.remove(profesor)
            print('Profesor eliminado correctamente.')
            break
    print('Profesor no encontrado.')



#MENU ESTUDIANTES
def menuEstudiantes():
    print()
    opcion = 0
    while True: 
        print("---------------MENU ESTUDIANTES---------------")
        print("-  1. Crear Estudiante                       -")
        print("-  2. Leer Estudiante                        -")
        print("-  3. Actualizar Estudiante                  -")
        print("-  4. Eliminar Estudiante                    -")
        print("-  5. Regresar al menu principal             -")
        print("----------------------------------------------")
        opcion = int(input("Ingrese una opcion: "))
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    crearEstudiantes()
                case 2:
                    leerEstudiantes()
                case 3:
                    actualizarEstudiantes()
                case 4:
                    eliminarEstudiante()
                case 5:
                    
                    break
                case _:
                    print("Opcion no valida.")
        except:
            print("[Error] Ingreso una opcion invalida")
    print()

#FUNCION DE CREAR ESTUDIANTES
def crearEstudiantes():
    print()
    global estudiantes
    print('---------------CREAR ESTUDIANTES---------------')
    nombre = input('Ingrese el nombre del estudiante: ')
    curso = input('Ingrese el curso del estudiante: ')
    carnet = input('Ingrese el carnet del estudiante: ')
    carrera = input('Ingrese la carrera del estudiante: ')
    nuevo = Estudiantes(nombre, curso, carnet, carrera)
    estudiantes.append(nuevo)
    print()
    print("Estudiante creado con exito.")
    print()

def leerEstudiantes():
    global estudiantes
    print('--------------LEER ESTUDIANTES--------------')
    if len(estudiantes) == 0:
        print('No hay estudiantes registrados en el programa.')
        
    for estudiante in estudiantes:
        json_string = '''
{
    nombre: '''+estudiante.getNombre()+''',
    curso: '''+estudiante.getCurso()+''',
    carrera: '''+estudiante.getCarrera()+''',
    carnet: '''+str(estudiante.getCarnet())+'''
}'''
        print(json_string)
        print()

def actualizarEstudiantes():
    print()
    global estudiantes
    carnet = input('Ingrese el carnet del estudiante a actualizar: ')
    for estudiante in estudiantes:
        if estudiante.getCarnet() == carnet:
            nombre = input('Ingrese el nuevo nombre del estudiante: ')
            estudiante.setNombre(nombre)
            curso = input('Ingrese el nuevo curso del estudiante: ')
            estudiante.setCurso(curso)
            carrera = input('Ingrese la nueva carrera del estudiante: ')
            estudiante.setCarrera(carrera)
            print("Estudiante actualizado exitosamente.")
            return
        
    print("Error: No se encontró un estudiante con ese código.")
    print()


#Eliminar estudiante 
def eliminarEstudiante():
    print()
    global estudiantes
    carnet = input('Ingrese el carnet del estudiante a eliminar: ')
    for estudiante in estudiantes:
        if estudiante.getCarnet() == carnet:
            estudiantes.remove(estudiante)
            print('Estudiante eliminado correctamente.')
            break
    print('Estudiante no encontrado.')






#MAIN
if __name__ == "__main__":
    menuPrincipal()