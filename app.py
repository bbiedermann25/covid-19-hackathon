from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return "Covid-19 Project"

@app.route('/index')
def index():
    return render_template('index.html')

