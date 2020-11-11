#!/bin/bash -e
NAME="websocket"  
FLASKDIR=/home/app/web
SOCKFILE=/home/app/web/sock
USER=root                                               
GROUP=root
NUM_WORKERS=3  

echo "Starting $NAME"

export PYTHONPATH=$FLASKDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django GUnicorn
# Programs meant to be run under supervisor should not daemonize themselves (not use --daemon)
# exec gunicorn --name $NAME --workers $NUM_WORKERS --bind=unix:$SOCKFILE wsgi:app

# Start your unicorn
exec gunicorn wsgi:app -b 127.0.0.1:8000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE