from flask import Flask, render_template, url_for, request , redirect
import csv

app = Flask(__name__)


@app.route('/<string:page_name>')
def portpolio(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email}, {subject}, {message}')


def write_to_csv(data):
     with open('database2.csv', 'a',newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(database, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])


@app.route('/submit_form', methods= ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
    return 'succesfull sent your req'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9080)
