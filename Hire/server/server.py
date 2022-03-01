
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app = Flask(__name__, template_folder='../client')
model = pickle.load(open('C:/Users/Dickson/Desktop/Hire/model/hiring.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0],2)

    return render_template('app.html', prediction_text='Employ Salary should be ksh {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force = True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)