const os = require('os');

// procesador = os.arch();
// sistemaoperativo = os.platform();
// cpu = os.cpus().length;
// memoriaram = os.totalmem();
// console.log('arquitectura del procesador: ' + procesador);
// console.log('sistema operativo: ' + sistemaoperativo);
// console.log('CPU: ' +  cpu);
// console.log('Memoria ram bytes: ' + memoriaram);
// memoria = memoriaram / 1024;
// console.log('Memoria ram KB: ' + memoria);
// memoria = memoria / 1024;
// console.log('Memoria ram MB: ' + memoria);
// memoria = memoria / 1024;
// console.log('Memoria ram GB: ' + memoria);


// RETO Nº 1
function descripcion(){
    return new Promise(function(res,rej){
        procesador = os.arch();
        sistemaoperativo = os.platform();
        cpu = os.cpus().length;
        memoriaram = os.totalmem();
        console.log('arquitectura del procesador: ' + procesador);
        console.log('sistema operativo: ' + sistemaoperativo);
        console.log('CPU: ' +  cpu);
        res(memoriaram);
        rej('error');
    })
}


function calcular(memoria,capacidad){
    return new Promise(function(res,rej){
        console.log('Memoria ram ' + capacidad + ': ' + memoria);
        memoria = memoria / 1024;
        res(memoria);
        rej('error');
    })
}

// function calcular(memoria){
//     return new Promise(function(res,rej){
//         console.log('Memoria ram ' + ': ' + memoria);
//         memoria = memoria / 1024;
//         res(memoria);
//         rej('error');
//     })
// }

// calcular(1000,'kb')

// memoria = 0

descripcion()
    .then((memoria)=>calcular(memoria,'B'))
    .then((memoria)=>calcular(memoria,'KB'))
    .then((memoria)=>calcular(memoria,'MB'))
    .then((memoria)=>calcular(memoria,'GB'))


// descripcion()
//     .then(calcular(memoria,"B"))
//     .then(calcular(memoria,'KB'))
//     .then(calcular(memoria,'MB'))
//     .then(calcular(memoria,'GB'))



// let memoria = calcular(1024,'Mrd')

// console.log(memoria)