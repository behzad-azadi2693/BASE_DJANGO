# BASE
```
change name directory django_project to Favorite name and 
change PROJECT_NAME in .env file to this Favorite name
```

***

# .env
```
run in server:
    DEBUG=False
    WEB_DOMAIN=<real_domain>

run in local for develop:
    DEBUG=True
    WEB_DOMAIN=localhost

run in local for test:
    DEBUG=False
    WEB_DOMAIN=localhost
```
### search <WEB_DOMAIN> in browser 


***

# DOCKER
```
install docker and docker-compose

sudo docker-compose up -d

sudo docker-compose restart

sudo docker-compose build

sudo docker-compose down -v
```

***

# BACKUP DB
```
chmod 777 backup.sh

./backup.sh
```

***
