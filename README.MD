# Academe

A website for reviewing professors, a project made for CS123. Group of Josh Castillo, Jayce Ching, Gab De Jesus, Nate Kibanoff.

## Getting Started

These instructions will guide the user through getting the project running on their local machine, for development and testing. 

### Prerequisites

Download and install [Python 3.5](https://www.python.org/downloads/release/python-350/)

Set up [path variables for Python](https://www.katsbits.com/tutorials/blender/pythonpath.php)

Create a [virtual environment](https://docs.python.org/3.4/library/venv.html) for Django. Name the venv `django1.11` 

Activate your venv, and run `pip install django==1.11`. This will install Django v 1.11 to your virtual environment

### Setting Up The Repository

Clone the repository into a folder named `Academe`. Make sure the subdirectory contains all the files in the repo, not a subfolder named `Academe` (which might result from cloning)

Activate your venv

Make sure you're in the directory `Academe` when running commands

Run `python manage.py makemigrations accounts profs courses reviews`

Run `python manage.py migrate`

Run `python manage.py runserver 8080` 

On your browser, go to the url `localhost:8080`. Academe will open

Additionally, visit `gabdejesus.com:8000` for an online version of the repository (Updated as of 12/6/2017)

## System Configuration

This section explains different ways to interact with the system, and allow for additional functions

### Creating A Super User

Django normally classes users into superusers/admins, normal users, and non-users. Superusers have additional privileges

Make sure you're in the directory `Academe`, and run `python manage.py createsuperuser`. Fill in the fields accordingly

You can now login to `localhost:8080/admin` or `gabdejesus.com:8000/admin`, and create changes to the database