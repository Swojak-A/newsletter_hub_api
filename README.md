# Newsletter Hub API
API for Newsletter Hub project (based on **Django 3.1.2/DRF 3.12.1** with **PostgresSQL** database)


## How to start?

1. Create `.env` file in the root directory containing following variables:
 * PWD
 * API_DOMAIN
 * POSTGRES_USER
 * POSTGRES_PASSWORD
 * POSTGRES_DB
 * DJANGO_SECRET_KEY
 * DJANGO_SETTINGS_MODULE
 * DJANGO_DATABASE_URL

Example content of `.env` file:

```
PWD=/home/user/newsletter_hub
API_DOMAIN=localhost:8000
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
DJANGO_SECRET_KEY=v3ry-s3cr37-key
DJANGO_SETTINGS_MODULE=app.settings.dev
DJANGO_DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```

2. Create `static` directory, change its owner to docker group and change its permissions. You can do it inline by:

```bash
sudo mkdir static && sudo chown :docker static && sudo chmod g+rwx static
```

3. Build docker image using command:

```bash
docker-compose build
```

4. Run docker container using command:

```bash
docker-compose up
```

5. You can now access Django admin panel by visiting `localhost:8000/admin` in your web browser of choice.

##### Useful commands

* starting container and logging into it:

You create container on the run and then shell inside runing container:

```bash
docker-compose run --rm web sh
```

* logging into existing container:

Assuming that you have an existing container and you want to directly log into it:

```bash
docker exec -it <container-name> sh
```

* creating development virtual enviroment:

For the purpose of local development you might want to set up virtual enviroment. First you might want to load correct package - in my case it was `sudo apt-get install python3.8-venv`. Now you can create enviroment using `python3.8 -m venv .venv`.

After completion you can activate it using: `source .venv/bin/acticate`. You can now install dependancies using: `pip install -r requirements/base.txt`

* adding pre-commits:

This repo is configured to use **pre-commit** hooks to improve quality of code. Pre-commit contains i.a. **black**, **flake** and **mypy** packages. It handles clean code formatting, unused imports and correct typing.

To install it you have to activate virtual env and run `pip install pre-commit`. Then execute: `pre-commmit install` to activate git repo hooks. All pre-commmit hooks will now run in pre-commit stage.

You can also run all pre-commit package by: `pre-commit run --all-files`
