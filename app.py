import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        location = request.form.get('location')
        bhk = float(request.form.get('bhk'))  # Convert bhk to float
        bath = float(request.form.get('bath'))  # Convert bath to float
        sqft = float(request.form.get('total_sqft'))  # Convert sqft to float

        input = pd.DataFrame(columns=['location', 'total_sqft', 'bath', 'bhk'],
                                               data=np.array([location, sqft, bath, bhk]).reshape(1, 4))
        prediction = pipe.predict(input)[0] * 1e5

        return str(np.round(prediction, 2))

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
