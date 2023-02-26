import pymongo
from classes import DATA, Dataprocess, DbMongo, Careers, Courses, Enrollments, Student
from dotenv import load_dotenv


def main():
    
    #Intancia de la clase data
    pipeline = Dataprocess(DATA)

    client, db = DbMongo.getDB()

    #career
    pipeline.create_careers(db)
    
    #Student
    #pipeline.create_students(db)
    
    #Enrollments
    #pipeline.create_enrollments(db)

    return True

    client.close()
    print ("Conexion Exitosa")

if __name__ == "__main__":
    load_dotenv()
    main()