import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)
model = load('trained_model/model.joblib')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='The Specie is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
