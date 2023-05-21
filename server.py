from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/hai/<username>/<int:post_id>')
# def hello_world(username = None, post_id = None):
#     return render_template('index.html', name= username, post_id = post_id)

@app.route('/')
def portpolio():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/contact.html')
def contacts():
    return render_template('contact.html')

# @app.route('/hello')
# def index():
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9080)
