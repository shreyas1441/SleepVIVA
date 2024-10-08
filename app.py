from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Load the model from the .pkl file
with open('viva_sleep_model2.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Prepare the input data as a DataFrame
    new_data = pd.DataFrame({
        'last_locked_hour': [data['last_locked_hour']],
        'last_locked_min': [data['last_locked_min']],
        'current_time_hour': [data['current_time_hour']],
        'current_time_min': [data['current_time_min']]
    })

    # Make prediction
    prediction = model.predict(new_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
