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
    
    @staticmethod
    def find_all(db):
        careers = []
        for c in db.careers.find():
            careers.append(Career(c["name"]))
        return careers
    
    
    @staticmethod
    def find_by_name(name,db):
        c = db.careers.find_one({"name": name})
        if c:
            return Career(c["name"])
        else:
            return None
