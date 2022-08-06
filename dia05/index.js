const { config } = require('./config');
const express = require('express');

const MysqlLib = require('./lib/mysql');

sql = new MysqlLib();


const app = express();

app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'servidor activo'
    })
})

app.listen(config.port,()=>console.log('servidor en http://localhost:'+config.port))