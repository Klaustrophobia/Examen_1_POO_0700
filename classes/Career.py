from classes.data import DATA
from classes.DbMongo import DbMongo

class Career:
    def __init__(self, carrera, id =""):
        self.carrera = carrera
        self.__id = id
        self.__collection = "Careers"

    def save(self,db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id
