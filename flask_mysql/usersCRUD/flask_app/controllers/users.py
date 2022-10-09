from flask_app import app
from flask_app.models.user import User
from flask import render_template,redirect,request,session,flash


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