from flask import Flask, render_template
from mysqlconnection import connectToMySQL
app= Flask(__name__)


@app.route('/')
def index():
    query = "SELECT * FROM dojos"
    results = connectToMySQL('mydb').query_db(query)

    return results






if __name__ == ("__main__"):
    app.run(debug=True)