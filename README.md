# ChereBot

### create venv

```
python -m venv venv
```

### activate it

#### Linux or MacOs

```
source venv/bin/activate

```

#### Windows

```
venv/Scripts/activate
```

### create database

```
CREATE DATABASE chere_db;
```

### Rename .env.example to .env and fill these fields

```
BOT_TOKEN=
SECRET_KEY=
HOST=localhost
DEBUG=true
REDIS_URL=redis://127.0.0.1:6379

DB_USER=
DB_NAME=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

### RUN command

#### runserver

```
python manage.py runserver
```

#### runbot

```
 python manage.py runbot
```
