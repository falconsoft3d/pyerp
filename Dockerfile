# Vamos a usar una imagen con python 3.7 de alpine (imagen mucho mas pequeña)
FROM python:3.7-alpine AS python

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Creamos un usuario y su directorio de trabajo
RUN addgroup -S webgroup && adduser -S webuser -G webgroup -h /home/webapp

# Establecemos el directorio de trabajo
WORKDIR /home/webapp

# Copiamos las dependencias del proyecto a la nueva imagen de Docker en el directorio /tmp
COPY requirements.txt /tmp/
COPY Pipfile Pipfile.lock /home/webapp/

# install psycopg2 and pillow
RUN apk update \
    && apk add --no-cache postgresql-dev \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add --no-cache --virtual .build-deps build-base linux-headers

# Actualizamos pip
RUN pip install --upgrade pip pipenv

# Instalamos las dependencias en la nueva imagen de Docker
RUN pipenv install --system

RUN apk del .build-deps && rm -rf /var/cache/apk/*

# Copiamos solo los archivos necesarios del proyecto al directorio de trabajo
COPY ./apps /home/webapp/apps/
COPY ./bin/gunicorn_start.sh /home/webapp/bin/gunicorn_start.sh
COPY ./pyerp /home/webapp/pyerp/
COPY installed_apps.py /home/webapp/installed_apps.py
# COPY ./run/emty_file.txt /home/webapp/run/emty_file.txt
COPY ./entrypoint.sh ./manage.py /home/webapp/

# creamos el archivo de logs
RUN touch /var/log/gunicorn.log

# Hacemos propietario del directorio al usuario que creamos y como grupo a root
# RUN chown -R webuser:root /home/webapp/ /var/log/gunicorn.log

# Ejecutamos el entrypoint.sh = Esperar que levante la base de datos, migrar
# los datos, recojer los estaticos
ENTRYPOINT ["/home/webapp/entrypoint.sh"]

# -------------------------------------------------------------------------- #
# Vamos a usar una imagen con nginx 1.15 de alpine (imagen mucho mas pequeña)
FROM nginx:1.17.2-alpine AS nginx

RUN addgroup -S webgroup && adduser -S webuser -G webgroup -h /home/webapp

# Sobre escribir la configuración por defecto de nginx
COPY virtual-host.conf /etc/nginx/conf.d/default.conf

# Copiamos solo los archivos innecesarios del proyecto al directorio de trabajo
COPY ./media /home/webapp/media/
