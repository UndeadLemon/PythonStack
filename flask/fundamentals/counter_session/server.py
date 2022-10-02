
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'Wait, can this really be anything?'



@app.route('/count')
def count():
    if 'visited' in session:
        session['visited'] += 1
    else:
        session['visited'] = 1
    if 'form' in session:
        pass
    else:
        session['form'] = {'add_amount':1}
        
        print(session)
    if 'count' in session:

        session['count'] += 1
        
        return render_template('count.html', count = session['count'], amount = session['form']['add_amount'], visited = session['visited'])
    else:
        
        
        session['count'] = 1
        
        

        return render_template('count.html', count = session['count'],  amount = session['form']['add_amount'], visited = session['visited'])

@app.route('/processing', methods = ['POST'])
def processing():
    session['form'] = request.form
    print(session['form'])
    return redirect('/count')

@app.route('/add')
def add():
    if 'count' in session:
        session['count'] += (int(session['form']['add_amount']) - 1)
        return redirect('/count')
    else:
        session['count'] = 1
        return redirect('/count')

@app.route('/refresh')
def refresh():
    session.pop('count')
    return redirect('/count')

@app.route('/destroy_session')
def destroy():
    
    session.clear()
    return redirect('/count')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.