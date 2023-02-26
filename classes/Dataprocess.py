class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        for career_data in self.__data['carrera']:
            career_document = {
                'nombre': career_data['nombre'],
            }

            #Inserta el documento en la coleccion 'careers'
            db.careers.insert_one(career_document)
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