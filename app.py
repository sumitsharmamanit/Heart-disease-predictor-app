from flask import Flask, request, render_template
import os
import pickle
import joblib

print(os.getcwd())
path = os.getcwd()

rf_model = joblib.load('Models/BestModel.pkl')


def get_predictions(age, sex, chest_pain, resting_bp, chol, fbs, restecg, max_hr, exang, oldpeak,
                    slope, ca, thal):
    mylist = [age, sex, chest_pain, resting_bp, chol, fbs, restecg, max_hr, exang, oldpeak,
              slope, ca, thal]
    # mylist = [float(i) for i in mylist]
    vals = [mylist]
    pred = rf_model.predict(vals)
    return pred


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chest_pain = request.form['chest_pain']
        resting_bp = request.form['resting_bp']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        max_hr = request.form['max_hr']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        prediction = get_predictions(age, sex, chest_pain, resting_bp, chol, fbs, restecg, max_hr, exang, oldpeak, slope, ca, thal)

        if prediction == 1:
            display_message = 'User is likely to have a heart disease.'
        else:
            display_message = 'User is unlikely to have a heart disease.'

        return render_template('home.html', msg=display_message)
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=False)
