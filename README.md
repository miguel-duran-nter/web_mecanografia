# web_mecanografia

## Clone repository

```Python
git clone https://github.com/miguel-duran-nter/web_mecanografia.git
```

## Install Virtual Enviorment

### Go to directory Repository

```bash
cd web_mecanografia
```

### Create Virtual

```Python
python3 -m venv .venv
```

### Active Virtual Enviorment

```Python
source .venv/bin/activate
```

### Install dependences

```Python
pip install -r requeriments.txt
```

## Start Server

### Go to directory

```Bash
cd web_meca
```

### Run Django Server

```Python
python3 manage.py runserver
```

## API

### Endpoints

- scoreboard: This endpoint was created to return the list of scores
- save-score: It was created to add punctuation to the scoreboard
- users: Used to return all users
- login: It is used to log in