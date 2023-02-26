class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data
        # Crea la coleccion Careers
        if "Careers" not in db.list_collection_names():
            db.create_collection("Careers")

        #
        careers = []
        for career_data in self.__data['carrera']:
            careers.append({
                'carrera': career_data['carrera']
            })
        
        if len(careers) > 0:
            db.Careers.inser_many(careers)

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