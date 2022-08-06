# esta es mi primera imagen con docker

# IMAGEN BASE
FROM ubuntu

# EJECUTAR COMANDOS EN MI CONTENEDOR UBUNTU
RUN apt-get update
RUN apt-get install python3 python3-dev -y

# EJECUTA UN COMANDO DE PYTHON3
CMD python3 -m http.server 5000

# EXPONE EL PUERTO 5000
EXPOSE 5000