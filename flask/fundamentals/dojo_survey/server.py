from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'The SECRETEST of keys.'

@app.route('/')
def form():

    return render_template('index.html')

@app.route('/processing', methods = ['POST'])
def processing():
    session['firstName'] = request.form['firstName']
    session['lastName'] = request.form['lastName']
    session['likesToast'] = request.form['likesToast']
    # session['javascript'] = request.form['javascript']
    # session['csharp'] = request.form['csharp']
    # session['python'] = request.form['python']
    return redirect('/results')

@app.route('/results')
def results():
    # if 'javascript' in session['survey']:
    #     pass
    # else:
    #     session['javascript'] = 'False'
    # if 'csharp' in session['survey']:
    #     pass
    # else:
    #     session['csharp'] = 'False'
    # if 'python' in session['survey']:
    #     pass
    # else:
    #     session['python'] = 'False'


    return render_template('results.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.