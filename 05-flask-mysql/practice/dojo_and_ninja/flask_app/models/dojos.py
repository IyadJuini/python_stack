from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # ===============CRUD Queries =  classmethods===============
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users 
                    (first_name, last_name, email, password)
                    VALUES 
                    (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    