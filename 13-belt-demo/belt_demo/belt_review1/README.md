Change the DATABASE name in  __init__.py

Dont forget the ; for the queries :)

singular fel models w plural fel controllers

Link bootstrap:

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

**********
Models : {
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
}

Controllers : {
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.++++ import ++++++
}