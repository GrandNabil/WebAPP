from flask import Flask, redirect, url_for, render_template, session

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')
