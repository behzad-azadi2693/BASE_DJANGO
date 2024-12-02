# BASE
```
change name directory django_project to Favorite name and 
change PROJECT_NAME in .env file to this Favorite name
```

***

# settings 
```
reading this link and in the settings config CSP favorite your site

https://www.digitalocean.com/community/tutorials/how-to-secure-your-django-application-with-a-content-security-policy
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

# for nginx binary service ssl
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/ssl/private/selfsigned.key \
-out /etc/ssl/certs/selfsigned.crt

sudo chmod 644 /etc/ssl/certs/selfsigned.crt
sudo chmod 600 /etc/ssl/private/selfsigned.key
```

***

# gitlab-ci

```
you need to create two branche (develop, main)
for gitlab you need install gitlab-releasein server deploy
you must control variable IMAGE_VERSION

first add variables into gitlab repo from .env.sample.json (please reading commits in the file)

if you have just one runner your tags is (runner-test, runner-develop, runner-deploy)
if you have multi runner for multi server for every runner add tags selfish for example (server test with tags runner-test and ... )

in your repo create three environment (server-develop, server-test, server-deploy)
```
