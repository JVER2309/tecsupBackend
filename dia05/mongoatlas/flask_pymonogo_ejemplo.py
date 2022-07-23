from flask import Flask,jsonify
from bson.json_util import dumps
from flask_pymongo import PyMongo

from dotenv import load_dotenv
load_dotenv()
import os


import json


app = Flask(__name__)
app.config["MONGO_URI"]=os.getenv('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'bienvenido a mi api rest con flask y mongodb'
    })

@app.route('/alumno')
def getAlumno():
    colAlumno = mongo.db.alumno.find({},{"_id":0,"nombre":1,"email":1})
    print(colAlumno)
    context = {
        'status':True,
        'content':json.loads(dumps(colAlumno))
    }
    return jsonify(context)

app.run(debug=True,port=5000)