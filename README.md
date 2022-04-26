# LeanCo Server

### Installation

```shell
pip install -r requirements.txt
```

Pour le développement
```shell
pip install -r dev-requirements.txt
```


### Lancement

````shell
docker-compose up -d  #lancement de postgresql
cd src
alembic upgrade head
uvicorn main:app
````

### BD Postgresql
user / password / bd : leanco


### Migrations

Dans le dossier src : 

Création d'une migration : 
```shell
alembic revision --autogenerate -m "init db"
```

Initialiser des migrations
```shell
alembic upgrade head
```

### URL

- Docs: [localhost:8000/docs]('localhost:8000/docs')
- Admin: [localhost:8000/admin]('localhost:8000/admin')