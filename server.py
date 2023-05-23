from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('profile.html')

@app.route('/<page_name>')
def hai(page_name):
    return render_template(page_name)