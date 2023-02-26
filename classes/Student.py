from classes.DbMongo import DbMongo

class Student:

    def __init__(self, nombre, numero_cuenta, cursos_aprobados, cursos_reprobados, edad, carrera, id =""):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados = cursos_reprobados
        self.edad = edad
        self.carrera = carrera
        self.__id = id
        self.__collection = "students"
    
    def save (self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_list(db):
        collection = db["students"]
        students = collection.fin()
        
        list_students = []
        for e in students:
            temp_student = Student(
                e["nombre"]
            )

        

