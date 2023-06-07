# kognit-api

## Introdução
O projeto tem como objetivo prover uma API pública responsável pela criação de usuário e suas carteiras (wallets).

## Começo rápido
Primeiro clone o repositódio do projeto do [Github](https://github.com/assisthiago/kognit-api) e entre no novo diretório:
```bash
$ git clone git@github.com:assisthiago/kognit-api.git
$ cd kognit-api
```

Crie um virtualenv para seu projeto na raiz do diretório e ative:
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Instale as dependências do projeto:
```bash
$ pip install -r requirements.txt
```

Copie o arquivo `.env-sample` do diretório `contrib/` para a raiz do projeto:
```bash
$ cp contrib/.env-sample .env
```

Depois, simplesmente rode as migrações:
```bash
$ python manage.py migrate
```

Agora você está pronto para rodar o servidor de desenvolvimento localmente:
```bash
$ python manage.py runserver
```

# Docker

Atualize o arquivo copiado `.env` para:
```
# DJANGO SETTINGS
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
CACHE_TIMEOUT_IN_SECONDS=30
SCHEDULER_TIMEOUT_IN_MINUTES=1

BANK_CHOICES=...

# === DOCKER REQUIRED ===
# -- Comment these variables to run locally with `$ python manage.py runserver`
# -- Uncomment these variables to run locally with `$ docker-compose run --build`

# DATABASE
DATABASE_URL=postgresql://admin:1q2w3e4r@db:5432/development
```

Agora rode o comando do `docker-compose`:
```bash
$ docker-compose up --build
...
kognit-api-db-1   | 2023-06-07 14:50:53.344 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
kognit-api-db-1   | 2023-06-07 14:50:53.344 UTC [1] LOG:  listening on IPv6 address "::", port 5432
kognit-api-db-1   | 2023-06-07 14:50:53.362 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
kognit-api-db-1   | 2023-06-07 14:50:53.402 UTC [25] LOG:  database system was shut down at 2023-06-07 14:41:00 UTC
kognit-api-db-1   | 2023-06-07 14:50:53.477 UTC [1] LOG:  database system is ready to accept connections
...
kognit-api-api-1  | System check identified no issues (0 silenced).
kognit-api-api-1  | June 07, 2023 - 14:50:57
kognit-api-api-1  | Django version 4.2.2, using settings 'app.settings'
kognit-api-api-1  | Starting development server at http://0.0.0.0:8000/
kognit-api-api-1  | Quit the server with CONTROL-C.
```

Abra o link [http://localhost:8000/](http://localhost:8000/) do projeto.
