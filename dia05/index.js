const express = require('express');
const {config} = require('./config');
const cors = require('cors');

const alumnoApi = require('./routes/alumno.route');
const cursoApi = require('./routes/curso.route');

const app = express();

app.use(cors());
app.use(express.json());

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

alumnoApi(app);
cursoApi(app);
app.listen(config.port,()=>console.log('servidor en http://localhost:'+config.port))