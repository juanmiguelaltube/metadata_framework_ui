https://docs.docker.com/samples/django/
https://docs.djangoproject.com/en/3.2/intro/tutorial02/
https://www.django-rest-framework.org/tutorial/quickstart/#quickstart


```bash
sudo docker-compose build web
```
```bash
sudo chown -R $USER:$USER .
```
```bash
docker-compose run web python manage.py createsuperuser --email admin@example.com --username admin
```
```bash
docker-compose run web python manage.py migrate
```
```bash
docker-compose up
```

--end