class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        #     
        db.create_collection("students")

        #
        students = self.__data['estudiantes']
        for student in students:
            student_document = {
                'nombre': student['nombre'],
                'carrera': student['carrera']
            }
        db.student.insert_one(student_document)
        return True
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data

        return True
    def create_students(self):
        ## Do something to create students on your mongodb collection using __data

        return True
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        
        return True