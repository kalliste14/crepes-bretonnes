#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/crepes_bretonnes.log
LOGDIR=$(dirname $LOGFILE)
LOGLEVEL=debug   # info ou warning une fois l'installation OK
NUM_WORKERS=3    # Règle : (2 x $num_cores) + 1

# user/group to run as
USER=root
GROUP=root

cd ~/Documents/Perso_Anne-So/Mes_Cours/Mes_Formations/Django-Project/crepes_bretonnes

# source ../bin/activate  # Cette ligne ne sert que si vous utilisez virtualenv

test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn hello.wsgi:application -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=$LOGLEVEL \
  --log-file=$LOGFILE 2>>$LOGFILE -b 127.0.0.1:8000
