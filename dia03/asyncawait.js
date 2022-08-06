async function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('Hola ' + nombre);
            resolve(nombre);
            reject('Hay un error');
        },1000)
    })
}

async function hablar(nombre){
    return new Promise((res,rej)=>{
        setTimeout(function(){
            console.log('Como estas ' + nombre);
            res(nombre);
            rej('No te entiendo');
        },1000)
    })
}

async function adios(nombre){
    console.log('Adios ' + nombre);
}

async function main(){
    let nombre = await hola('Juver');
    await hablar(nombre);
    await adios(nombre);
}

main();