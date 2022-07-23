from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))
print(os.getenv('MONGO_URI'))


db_codigo = cliente['db_codigo']
colAlumno = db_codigo['alumno']

# dicNuevoAlumno = {
#         "id":2,
#         "nombre":"carlos paredes",
#         "email":"carlos@gmail.com",
#         "celular":"95052243",
#         "github":"https://github.com/cparedes/"
# }

# dicNuevoAlumno = {
#         "id":3,
#         "nombre":"localhost",
#         "email":"localhost@gmail.com",
#         "celular":"936556002",
#         "github":"https://github.com/cparedes/"
# }


# nuevoAlumnoId = colAlumno.insert_one(dicNuevoAlumno)
# print("nuevo alumno " + str(nuevoAlumnoId))

for alumno in colAlumno.find():
    print(alumno['nombre'] + ' - ' + alumno['email'] + ' - ' + alumno['celular'])