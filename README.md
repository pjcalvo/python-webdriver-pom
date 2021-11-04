# python-webdriver-pom

## Description

I decided to use unittest because it has a very descriptive/traditional way of working. We first inherit our test clases from unittest and just write the test functions and before hooks.

## Instructions

### Run a virtualenv and install the dependencies

First of all you need to setup a python virtual envuironment to install the proyect dependencies.

```sh
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

_Note: Notice that this the depencies are meant to run on the latest stable chrome version Chromedriver 95, in case you have a different version please update the requirements accordinly.

### Run the tests with

In order to run the tests use the unittest module by running:

```sh
python -m unittest tests/*
```

### Docker

In order to avoid issues with chrome configuration I decided to create a Dockerfile to run the tests, unfortunately it is failing due a robot check.

```sh
docker build -t e2e:0.1.1 .
docker run e2e:0.0.1
```