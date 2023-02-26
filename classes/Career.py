from classes.data import DATA


class Career:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrera = []

    def add_career(self, carrera):
        self.carrera.append(carrera)

    def remove_course(self, carrera):
        self.carrera.remove(carrera)

    def get_courses(self):
        return self.carrera
    
