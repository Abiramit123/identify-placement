import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('camp.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def pred():
    age = request.form['Age']
    print(age)
    gender = request.form['Gender']
    print(age, gender)
    stream = request.form['Stream']
    print(age, gender, stream)
    internships = request.form['Internships']
    print(age, gender, stream, internships)
    cgpa = request.form['CGPA']
    print(age, gender, stream, internships, cgpa)
    historyofbacklogs = request.form['HistoryOfBacklogs']
    print(historyofbacklogs)
    print(age, gender, stream, internships, cgpa, historyofbacklogs)

    inp_features = [[int(age), int(gender), int(stream), int(internships), int(cgpa),
                     int(historyofbacklogs)]]
    print(inp_features)
    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'Eligible to job, you will be placed'
    else:
        prediction_text = 'Not eligible to placed'
    print(prediction_text)
    return render_template('prediction.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
