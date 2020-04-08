#!/bin/sh

NAME="pyerp" # Name of the application
DJANGODIR=/home/webapp # Django project directory
LOGFILE=/var/log/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
SOCKFILE=$DJANGODIR/run/gunicorn.sock # we will communicate using this unix socket
USER=webuser # the user to run as
GROUP=webgroup # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=pyerp.settings # which settings file should Django use
DJANGO_WSGI_MODULE=pyerp.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
# source /home/snicoper/.virtualenvs/example.com/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--chdir=$DJANGODIR \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE