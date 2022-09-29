from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry, this is not a valid path!"

@app.route('/play')
def playground():
    return render_template('playground.html', repeat=3, color='lightblue')

@app.route('/play/<int:num>')
def playgroundrepeat(num):
    return render_template('playground.html', repeat=num, color='lightblue')

@app.route('/play/<int:num>/<string:color>')
def playgroundrepeatcolor(num, color):
    return render_template('playground.html', repeat=num, color=color)
@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/repeat/<times>/<string>')

def repeat(times, string):
    newstr = ''
    for i in range (0, int(times)):
        newstr += (string + " ")

    return newstr

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

