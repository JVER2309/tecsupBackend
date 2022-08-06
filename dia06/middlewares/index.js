const express = require('express');
const morgan = require('morgan')

const app = express();

app.use(morgan('combined'));

app.use(function(req,res,next){
    console.log('este es un middleware');
    next();
})

app.use((req,res,next)=>{
    const timeElapsed = Date.now();
    const today = new Date(timeElapsed);
    console.log('ejecutando a las',today.toISOString());
    next();
})

app.get('/',(req, res)=>{
    res.json({
        content:'ejemplo de middlewares'
    })
})

app.use('/usuario',(req,res,next)=>{
    console.log(a+3);
    console.log('tipo de request: '+ req.method);
    next();
})

app.get('/usuario',(req,res)=>{
    res.json({
        nombre:'admin',
        email:'admin@gmail.com'
    })
})

// middleware de errores:
app.use(function(err,req,rest,next){
    console.error(err.stack);
    rest.status(500).json({
        content:'error en el servidor',
        detail:err.stack
    })
})


app.listen(5001,()=>console.log('http://localhost:5001'));