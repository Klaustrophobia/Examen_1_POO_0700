from classes.Career import Career
from classes.Course import Course
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        # Crea la coleccion Careers
        if "Careers" not in db.list_collection_names():
            db.create_collection("Careers")

        return True
    
    def create_courses(self,db):
        ## Do something to create courses on your mongodb collection using __data
          # Crea la coleccion Courses
        if "Student" not in db.list_collection_names():
            db.create_collection("Courses")

        return True
    def create_students(self,db):
        ## Do something to create students on your mongodb collection using __data
          # Crea la coleccion Courses
        if "Student" not in db.list_collection_names():
            db.create_collection("Student")

        return True
    def create_enrollments(self,db):
        ## Do something to create enrollments on your mongodb collection using __data
        if "Enrollments" not in db.list_collection_names():
            db.create_collection("Enrollments")
        
        return True