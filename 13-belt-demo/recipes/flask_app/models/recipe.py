from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
# from datetime import datetime


class Recipe:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.name = data_dict['name']
        self.under = data_dict['under']
        self.description = data_dict['description']
        self.instructions = data_dict['instructions']
        self.date = data_dict['date']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster = ""

    #======================CREATE==========================

    @classmethod
    def create(cls, data_dict):
        query = """
                INSERT INTO recipes (user_id, name, under, instructions, date, description) 
                VALUES (%(user_id)s,%(name)s,%(under)s,%(instructions)s,%(date)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # ======================== UPDATE +++++++++++++++++++++++
    
    @classmethod
    def update(cls, data_dict):
        query = """
                UPDATE recipes SET
                name = %(name)s, under = %(under)s,  date = %(date)s,  instructions = %(instructions)s, 
                description = %(description)s 
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # ========================= DELETE =====================
    @classmethod
    def delete(cls, data_dict):
        query  = """
                DELETE FROM recipes WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    


    # ============================== GET ALL ===================
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;
                """
        result = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in result:
            recipe = cls(row)
            recipe.poster = f"{row['first_name']} {row['last_name']}"
            recipes.append(recipe)
        return recipes
    
    # +++++++++++++++++++++++++++++++++++++++++
    
    @classmethod
    def get_user_recipes(cls, data_dict):
        query = """
                SELECT * FROM recipes WHERE user_id = %(user_id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        recipes = []
        for row in result:
            recipe = cls(row)
            # recipe.poster = f"{row['first_name']} {row['last_name']}"
            recipes.append(recipe)
        return recipes
# ============================== GET one by id ===================
    @classmethod
    def get_by_id(cls, data_dict):
        query = """
        SELECT * FROM recipes 
        JOIN users ON recipes.user_id = users.id
        WHERE recipes.id=%(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print(result)
        recipe = cls(result[0])
        recipe.poster = f"{result[0]['first_name']} {result[0]['last_name']}"
        return recipe
    
    # ======================VALIDATION =============================
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['name'])<2:
            is_valid =False
            flash("name not valid", "name")
        if len(data_dict['instructions'])<2:
            is_valid =False
            flash("instructions not valid", "instructions")    
        if len(data_dict["description"])<7:
            is_valid = False
            flash("description too short","description")
        if data_dict['date'] == "":
            is_valid = False
            flash("Date is required", "date")
        # elif data_dict['date'] < datetime.now():
        #     is_valid = False
        #     flash("Date must be in the future", "date")
        return is_valid