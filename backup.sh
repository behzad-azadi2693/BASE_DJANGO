#!/bin/bash

export $(cat .env | xargs)

export "time"=$(date '+%Y-%m-%d-%H:%M:%S')

cd backup_DB

sudo docker exec -i postgres /usr/bin/pg_dump -U $DB_USER $DB_NAME > postgres-backup-$time.sql

python ../$PROJECT_NAME/manage.py dumpdata --indent 4 > postgres-backup-$time.json

python ../$PROJECT_NAME/manage.py backup_to_csv