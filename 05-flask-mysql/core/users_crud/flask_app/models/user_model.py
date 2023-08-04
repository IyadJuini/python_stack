from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME 
from datetime import datetime
class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT id,first_name, last_name,email,DATE_FORMAT(created_at, '%M %e, %Y') as created_at,updated_at FROM users;
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query)
        all_users= []
        for row in result:
            user = cls(row)
            all_users.append(user)
        return all_users
    
    @classmethod
    def get_by_id(cls,data_dict):
        # query = """SELECT id,first_name, last_name,email, created_at, DATE_FORMAT(updated_at, '%M %e, %Y %h:%i %p') as updated_at 
        #         FROM users WHERE id=%(id)s;"""
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        date = result[0]['updated_at']
        the_user = cls(result[0])
        the_user.updated_at = datetime.strftime(date, '%d %B %Y %I:%M %p')
        return the_user
    
    @classmethod
    def delete(cls,data_dict):
        query="DELETE FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        return None
    
    # @classmethod
    # def edit(cls, data_dict):
    #     query = """SELECT id,first_name, last_name,email,DATE_FORMAT(created_at, '%M %e, %Y') created_at, 
    #     DATE_FORMAT(updated_at, '%M %e, %Y %h:%i%p') as updated_at FROM users WHERE id=%(id)s"""

        
    #     result = connectToMySQL("users_schema").query_db(query,data_dict)
    #     return result
    
    @classmethod
    def update_user(cls,data_dict):
        query = """
                UPDATE users set first_name=%(first_name)s , last_name=%(last_name)s, email=%(email)s
                WHERE id=%(id)s
                """    
        
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def create_user(cls,data_dict):
        query= """
                INSERT INTO users(first_name,last_name,email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        return result