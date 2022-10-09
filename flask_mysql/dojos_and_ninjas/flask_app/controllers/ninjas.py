from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session,flash


@app.route('/ninja')
def ninja():

    return render_template('ninjas_show.html')

@app.route('/ninja_add')
def ninja_add():
    dojos = Dojo.get_all()
    return render_template('ninja_form.html', dojos=dojos)

@app.route('/ninja_add_processing', methods=['POST'])
def ninja_add_processing():

    data = {
        'name':request.form['name'],
        'id':int(request.form['id'])
        }
    print(data)
    Ninja.save(data)
    return redirect('/dojo')