# Leanco Performance - API

## Installation
 
- Prérequis : Base de données Postgresql

1. Placer le server.key et le server-fullchain.crt à la racine du projet (ou autre)


2. Créer un fichier .env dans le dossier src avec les variables suivantes (valeurs à modifier) :

    ```dotenv
    #CONFIGURATION API
    
    API_BASE_URL=/api #Base URL pour l'API
    PROJECT_NAME=Leanco Performance API #Nom du projet pour le swagger
    BACKEND_CORS_ORIGINS=["http://localhost/", "http://localhost:4200/", "http://localhost:3000/", "http://localhost:8080/"] #CORS acceptés
    
    #CONFIG BD
    
    POSTGRES_SERVER=localhost:5432 #URL du serveur postgresql
    POSTGRES_USER=leanco #User
    POSTGRES_PASSWORD=leanco #Mot de passe
    POSTGRES_DB=leanco #Nom de la BD
    
    #CONFIG CERTIFICAT ET CLÉ
    SERVER_PRIVATE_KEY_PATH=../server.key #Chemin vers le fichier contenant la clé privée du serveur
    SERVER_PUBLIC_CERT_PATH=../server-fullchain.crt #Chemin vers le fichier contenant le certificat public
    ```
3. Configurer alembic en modifiant les accès à la BD dans le fichier src/alembic/env.py
    ```python
    def get_url():
        user = os.getenv("POSTGRES_USER", "A MODIFIER")
        password = os.getenv("POSTGRES_PASSWORD",  "A MODIFIER")
        server = os.getenv("POSTGRES_SERVER",  "A MODIFIER")
        db = os.getenv("POSTGRES_DB",  "A MODIFIER")
    ```
   
4. Installer les dépendances
    ```shell
    pip install -r requirements.txt
    ```

5. Initialiser la base de données avec les migrations (depuis le dossier src)
    ```shell
    alembic upgrade head
    ```

6. Lancer l'API (depuis le dossier src)
    ```shell
    uvicorn main:app
    ```

7. L'API est disponible 

- Docs: [localhost:8000/docs]('http://localhost:8000/docs')
- Admin: [localhost:8000/admin]('http://localhost:8000/admin')


## Développement

- Des dépendances supplémentaires sont disponibles
    ```shell
    pip install -r dev-requirements.txt
    ```

- Gestion des migrations
  * Création d'une migration : 
    ```shell
    alembic revision --autogenerate -m "init db"
    ```

  * Initialiser des migrations
    ```shell
    alembic upgrade head
    ```

- Base de données de développement : Une base de données et un pgAdmin est disponible via docker

  * Lancement
    ````shell
    docker-compose up -d  #lancement de postgresql
    ````
  * Identifiant BD :
    * serveur : localhost:5432 
    * user: leanco
    * password: leanco
    * bd: leanco

  * PgAdmin :
    * URL : [localhost:5050]('http://localhost:5050')
    * Email : admin@admin.com
    * Password: root



