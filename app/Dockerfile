#Archivo para crear el contenerdor y copiar los archivos y ejecutarlos como scrips

#iniciar la version de python, alistar un contenedor con esa version
FROM python:3.8

#Crear una carpeta dentro de contenedor

WORKDIR /app

#Copiar el archivo desde una ubicacion local al contenedor, se divide con un espacio

COPY requirements.txt /app/requirements.txt

#Correr una linea para instalar las dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#COPY. - copiar toda la carpeta y llevarla al espacio de trabajo de WORKDIR

COPY . /app

#Comando que mantiene en ejecución al contenedor

CMD bash -c "while true; do sleep 1; done"