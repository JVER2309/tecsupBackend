const express = require('express');
const cors = require('cors');

const mysqulConnection = require('./database');

const app = express();
const port = 5000;


app.use(cors());
// PERMITE QUE EL SERVIDOR RECIVA DATA EN JSON
app.use(express.json());


app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'Mi primer app web con express Js - '
    })
})


//  api rest de alumnos
app.get('/alumno',(req,res)=>{
    mysqulConnection.query('select * from tbl_alumno',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

app.post('/alumno',(req,res)=>{
    const {nombre,email} =req.body;

    const query = `insert into tbl_alumno(alumno_nombre,alumno_email)
                    values('${nombre}','${email}')`;

    mysqulConnection.query(query,(err,rows,fields)=>{
        if(!err){
            const querynewAlumno = 'select * from tbl_alumno order by alumno_id desc limit 1';
            mysqulConnection.query(querynewAlumno,(erro,rows,fields)=>{
                res.json(rows[0]);
            })
            
        }else{
            console.log(err);
        }
    })
})

app.put('/alumno/:id',(req,res)=>{
    const {nombre,email} = req.body;
    const {id} = req.params;

    const query = "update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?";

    mysqulConnection.query(query,[nombre,email,id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'alumno actualizado'
                })
            }else{
                console.log(err)
            }
        })
})


app.delete('/alumno/:id',(req,res)=>{
    const {id} = req.params;

    query = "delete from tbl_alumno where alumno_id=?"

    mysqulConnection.query(query,[id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'alumno eliminado'
                })
            }else{
                console.log(err);
            }
        })
})

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'Mi primer app web con express Js - '
    })
})


//  api rest de curso
app.get('/curso',(req,res)=>{
    mysqulConnection.query('select * from tbl_curso',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

app.post('/curso',(req,res)=>{
    const {nombre} =req.body;

    const query = `insert into tbl_curso(curso_nombre)
                    values('${nombre}')`;

    mysqulConnection.query(query,(err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'curso creado'
            })
        }else{
            console.log(err);
        }
    })
})

app.put('/curso/:id',(req,res)=>{
    const {nombre} = req.body;
    const {id} = req.params;

    const query = "update tbl_curso set curso_nombre=? where curso_id=?";

    mysqulConnection.query(query,[nombre,id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'curso actualizado'
                })
            }else{
                console.log(err)
            }
        })
})


app.delete('/curso/:id',(req,res)=>{
    const {id} = req.params;

    query = "delete from tbl_curso where curso_id=?"

    mysqulConnection.query(query,[id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'curso eliminado'
                })
            }else{
                console.log(err);
            }
        })
})



app.listen(port,()=>{
    console.log('servidor activo en http://localhost:'+port);
 })