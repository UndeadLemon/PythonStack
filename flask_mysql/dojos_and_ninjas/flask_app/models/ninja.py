from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.name=data['name']
        self.id=data['id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );"
        ninja_id = connectToMySQL('mydb').query_db(query, data)
        data['ninja_id'] = ninja_id
        query =  "INSERT INTO dojos_and_ninjas (dojo_id, ninja_id) VALUES (%(id)s, %(ninja_id)s);"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET name = %(name)s, updated_at = NOW() WHERE id=%(id)s"
        

        return connectToMySQL('mydb').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM ninjas WHERE dojos.id = %(id)s"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"


        results = connectToMySQL('mydb').query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas