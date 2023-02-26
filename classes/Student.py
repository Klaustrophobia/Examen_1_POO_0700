# from classes.DbMongo import DbMongo
from data import DATA
class Estudiante:
   
    datos_estudiante = DATA

    def __init__(self, datos_estudiante):
        self.numero_cuenta = datos_estudiante['numero_cuenta']
        self.nombre_completo = datos_estudiante['nombre_completo']
        self.cursos_aprobados = datos_estudiante['cursos_aprobados']
        self.cursos_reprobados = datos_estudiante['cursos_reprobados']
        self.edad = datos_estudiante['edad']
        self.carrera = datos_estudiante['carrera']
    
    def obtener_carrera(self):
        # Devuelve la carrera del estudiante
        return self.carrera
    
# Crear objetos de tipo Estudiante a partir de los datos de la lista
estudiantes = []
for datos_estudiante in DATA:
    estudiante = Estudiante(datos_estudiante)
    estudiantes.append(estudiante)

# Ejemplo de uso de los métodos de la clase Estudiante
print("Carrera de Ana Díaz:", estudiantes[1].obtener_carrera())
