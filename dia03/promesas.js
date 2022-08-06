function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('Hola ' + nombre);
            resolve(nombre);
            reject('Hay un error');
        },1000)
    })
}

function hablar(nombre){
    return new Promise((res,rej)=>{
        console.log('Como estas ' + nombre);
        res(nombre);
        rej('no te entiendo');
    },1000)
}

let nom = 'Juver'

hola(nom)
    .then(hablar)
    .then(()=>{
        console.log('adios');
    })