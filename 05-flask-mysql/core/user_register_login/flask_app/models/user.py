from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from flask import flash
from datetime import datetime
#from flask_app.models.ninja import Ninja
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.state = data_dict['state']
        self.birth_date = data_dict['birth_date']
        self.gender = data_dict['gender']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create(cls,data_dict):
        query= """INSERT INTO users (first_name,last_name,email,password,birth_date,state,gender) VALUES 
                (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(birth_date)s,%(state)s,%(gender)s);
                """
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @staticmethod
    def calculate_age(birthdate):
        today = datetime.now().date
        print(today)
        age = datetime.now().year - birthdate.year - ((datetime.now().month, datetime.now().day) < (birthdate.month, birthdate.day))
        return age

    @staticmethod
    def validation_registration(data_dict):
        is_valid=True
        if len(data_dict['first_name'])<2:
            flash("first name must more then two character", "register")
            is_valid=False
        if len(data_dict['first_name'])==0:
            flash("first name must not be empty", "register")
            is_valid=False
        if len(data_dict['last_name'])<2:
            flash("last name mast be more then two", "register")
            is_valid=False
        if len(data_dict['last_name'])==0:
            flash("last name must not be empty", "register")
            is_valid=False
        if not EMAIL_REGEX.match(data_dict['email']):
            flash("your email is not valid", "register")
            is_valid=False
        if not re.search(r'\d', data_dict['password']):
            flash("your password must include a number", "register")
            is_valid=False
        if not re.search(r'[A-Z]', data_dict['password']):
            flash("your password must include an uppercase letter", "register")
            is_valid=False
        if data_dict['password'] != data_dict['confirm_password']:
            flash("password doesn't much", "register")
            is_valid=False
        if User.get_by_email({'email':data_dict['email']}):
            flash("user already exist", "register")
            is_valid=False
        if not data_dict['birth_date']:
            flash("please put your age", "register")
            is_valid=False
        elif User.calculate_age(datetime.strptime(data_dict['birth_date'], '%Y-%m-%d').date())<10:
            flash("you are to young to register", "register")
            is_valid=False
        if data_dict['state']=="":
            flash("please choose your state", "register")
            is_valid=False
        if 'gender' not in data_dict:
            flash("Please select a valid gender", "register")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_by_email(cls,data_dict):
        query=""" SELECT * FROM users WHERE email=%(email)s"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_id(cls,data_dict):
        query=""" SELECT * FROM users WHERE id=%(id)s"""
        result=connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        return cls(result[0])