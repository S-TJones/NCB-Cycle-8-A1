from flask import Flask
from flask import render_template

app = Flask(__name__)

# The first route "/" should represent your home page and can simply display your Team name, your name and your photo.
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")