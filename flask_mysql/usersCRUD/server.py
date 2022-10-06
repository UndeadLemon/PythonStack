from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def default():

    return "Hello?"

@app.route('/read')
def displayDB():
    users = User.get_all()
    print(users)
    return render_template('readall.html', users=users)

@app.route('/user_form')
def user_create_page():
    return render_template('create.html')

@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.form
    id = User.save(data)
    return redirect(f'/showone/{id}')

@app.route('/showone/<id>')
def show_one(id):
    data={
        'id':id
        }
        
    
    user=User.get_one(data)
    print(user)
    return render_template('readone.html', user=user[0])

@app.route('/edit/<id>')
def edit_one(id):
    data={
        'id':id
    }
    user=User.get_one(data)


    return render_template('editone.html', id=id, user=user[0])
@app.route('/edit_one_user', methods=['POST'])
def edit_one_process():
    id=request.form['id']
    data=request.form
    User.update(data)
    return redirect(f'/showone/{id}')

@app.route('/delete/<id>')
def delete(id):
    data={
        'id':id
    }
    User.delete(data)
    return redirect('/read')

    return False
class User:
    def __init__(self,data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.id=data['id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"

        return connectToMySQL('users_schema').query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"

        return connectToMySQL('users_schema').query_db(query, data)
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s"

        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM users WHERE users.id = %(id)s"

        return connectToMySQL('users_schema').query_db(query, data)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"


        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append( cls(user) )
        return users

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.