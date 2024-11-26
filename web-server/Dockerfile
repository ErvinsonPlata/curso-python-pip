#Archivo para crear el contenerdor y copiar los archivos para desplegar un servidor a la nube 

#iniciar la version de python, alistar un contenedor con esa version
FROM python:3.10

#Crear una carpeta dentro de contenedor

WORKDIR /app

#Copiar el archivo desde una ubicacion local al contenedor, se divide con un espacio

COPY requirements.txt /app/requirements.txt

#Correr una linea para instalar las dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#COPY. - copiar toda la carpeta y llevarla al espacio de trabajo de WORKDIR

COPY . /app

#Comando para lanzadar el servidor de uvicorn

CMD ['uvicorn','main:app','--host','0.0.0.0','--port','80'] 