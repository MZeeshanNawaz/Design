from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello flask"
@app.route('/about')
def about():
    return "Hello about"
@app.route('/contact')
def contact():
    return "Hello contact"

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/hello/<name>')
def hello(name):
    return render_template("name.html",name=name)

@app.route('/form', methods =['GET','POST'])
def form():
    if request.method=='POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        LastUpdate = request.form['LastUpdate']
        Films = request.form['Films']
        return render_template('result.html',FirstName=FirstName,LastName=LastName,LastUpdate=LastUpdate,Films=Films)
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)