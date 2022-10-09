from flask_app.config.mysqlconnection import connectToMySQL




class Dojo:
    def __init__(self,data):
        self.name=data['name']
        self.id=data['id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW() );"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id=%(id)s"

        return connectToMySQL('mydb').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM dojos LEFT JOIN dojos_and_ninjas ON  dojos_and_ninjas.dojo_id = dojos.id LEFT JOIN ninjas ON ninjas.id = dojos_and_ninjas.ninja_id WHERE dojos.id = %(id)s"

        return connectToMySQL('mydb').query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"


        results = connectToMySQL('mydb').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos