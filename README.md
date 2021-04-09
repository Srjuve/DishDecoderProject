# Dish Decoder
Food/Nutrient related web page, where the user can search for meals depending on some parameters such as ingredients, nutrition values or the recipe name. Additionaly, users will be able to create and share their own recipes and rate the ones from other people.
## Summary

  - [Getting Started](#getting-started)
  - [Run with docker](#run-with-docker)
  - [Deploy with heroku](#deploy-with-heroku)
  - [Built With](#built-with)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of Dish Decoder up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites
Install all the dependencies:
```shell 
$ pip install -r requirements.txt
```
Migrate and run server:
```shell 
$ python manage.py makemigrations
```
```shell 
$ python manage.py migrate
```
```shell 
$ python manage.py runserver
```


## Run with Docker
At config you must add the environment files:
- .database.env
```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=dish_decoder_db
```

- .env
```bash
SECRET_KEY=your_secret_key
DEBUG=True
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_NAME=dish_decoder_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

```shell 
$ docker-compose build
```

```shell 
$ docker-compose up
```

## Deploy with Heroku


## Built With

  - Python3
  - Docker
  - Heroku
  - PostgreSQL

## Authors

  - GuillemCamats
  - rogerLarriba
  - Srjuve
  - Spiritusrevenge
  - santo0

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - https://github.com/PurpleBooth/a-good-readme-template
  - And a birb ![Just a birb](https://media.giphy.com/media/l3q2zVr6cu95nF6O4/giphy.gif)
