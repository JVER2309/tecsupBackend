from flask import Flask,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
load_dotenv()
import os


import json

cliente = MongoClient(os.getenv('MONGO_URI'))

db = cliente['db_codigo']

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'bienvenido a mi api rest con flask y mongodb'
    })

@app.route('/alumno')
def getAlumno():
    colAlumno = db['alumno']

    context = {
        'status':True,
        'content':json.loads(dumps(colAlumno.find({},{"_id":0,"nombre":1,"email":1})))
    }
    return jsonify(context)

app.run(debug=True,port=5000)