# Dish Decoder

One Paragraph of project description goes here

## Summary

  - [Getting Started](#getting-started)
  - [Runing the tests](#running-the-tests)
  - [Deployment](#deployment)
  - [Built With](#built-with)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```shell 
pip install -r requirements.txt
```
### Installing

A step by step series of examples that tell you how to get a development
env running

Say what the step will be

    Give the example

And repeat

    until finished

End with an example of getting some data out of the system or using it
for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

    Give an example

### And coding style tests

Explain what these tests test and why

    Give an example

## Deployment
At config you must add the environment files:
- .database.env
```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=dish_decoder_db
```

- .env
v
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
