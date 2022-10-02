from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'The SECRETEST of keys.'

@app.route('/')
def form():

    return render_template('index.html')

@app.route('/processing', methods = ['POST'])
def processing():
    session['survey'] = request.form
    return redirect('/')

@app.route('/results')
def results():
    if 'javascript' in session['survey']:
        pass
    else:
        session['survey']['javascript'] = 'False'
    if 'csharp' in session['survey']:
        pass
    else:
        session['survey']['csharp'] = 'False'
    if 'python' in session['survey']:
        pass
    else:
        session['survey']['python'] = 'False'


    return render_template('results.html', javascript=session['survey']['javascript'], csharp=session['survey']['csharp'], python=session['survey']['python'], debug=session['survey'], fName = session['survey']['firstName'], lName = session['survey']['lastName'], toastPreference = session['survey']['likeToast'])

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.