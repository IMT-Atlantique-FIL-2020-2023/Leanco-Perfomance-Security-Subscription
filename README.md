# LeanCo Server

### Installation

```shell
pip install -r requirements.txt
```

Pour le développement
```shell
pip install -r dev-requirements.txt
```


###Lancement

````shell
cd src
uvicorn main:app
````

###Migrations

Dans le dossier src : 

```shell
alembic revision --autogenerate -m "init db"
```

```