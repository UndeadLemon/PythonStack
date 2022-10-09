from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash


@app.route('/')
def default():

    return "Hello?"

@app.route('/dojo')
def displayDB():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojo_show.html', dojos=dojos)

@app.route('/dojo_form')
def dojo_create_page():
    return render_template('dojo_create.html')

@app.route('/dojo_add', methods=["POST"])
def add_dojo():
    data = request.form
    id = Dojo.save(data)
    return redirect(f'/show_one_dojo/{id}')

@app.route('/dojo_show_one/<id>')
def show_one(id):
    data={
        'id':id
        }
        
    
    dojo=Dojo.get_one(data)
    print(dojo)
    return render_template('dojo_show_one.html', dojo=dojo)

@app.route('/dojo_edit/<id>')
def edit_one(id):
    data={
        'id':id
    }
    dojo=Dojo.get_one(data)


    return render_template('edit_one_dojo.html', id=id, dojo=dojo[0])
@app.route('/edit_one_dojo', methods=['POST'])
def edit_one_process():
    id=request.form['id']
    data=request.form
    Dojo.update(data)
    return redirect(f'/show_one_dojo/{id}')

@app.route('/dojo_delete/<id>')
def delete(id):
    data={
        'id':id
    }
    Dojo.delete(data)
    return redirect('/dojo')