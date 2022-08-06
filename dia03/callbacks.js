function hola(nombre,primercallbakc){
    setTimeout(function(){
        console.log('Hola ' + nombre);
        primercallbakc(nombre)
    },1000);
}

function hablar(nombre,segundocallback){
    setTimeout(function(){
        console.log("Como estas " + nombre);
        segundocallback(nombre)
    })
}

function adios(nombre){
    console.log("adios " + nombre);
}

hola('Juver',function(nombre){
    // console.log('Como estas ' + nombre);
    hablar(nombre,function(nombre){
        adios(nombre);
    })
});