from mongoengine import *
from dotenv import load_dotenv
load_dotenv()
import os

connect(host=os.getenv('MONGO_URI'))

# CREAMOS CLASES BASADAS EN DOCUMENTOS
class Usuario(Document):
    usuario = StringField(required=True)
    password = StringField(required=True)

nuevoUsuario = Usuario()
nuevoUsuario.usuario = 'juver manrique'
nuevoUsuario.password = '1234'

nuevoUsuario.save()
