from flask import Flask, request, jsonify, render_template
import pickle

# Load the trained model from the pickle file
with open('sleep_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize the Flask app
app = Flask(__name__)

# Route for the home page (renders the HTML form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extracting input values from the request
    last_lock_hour = data['last_locked_hour']
    last_lock_min = data['last_locked_min']
    current_hour = data['current_time_hour']
    current_min = data['current_time_min']

    # Input for the model
    input_data = [[last_lock_hour, last_lock_min, current_hour, current_min]]

    # Predict using the loaded model
    prediction = model.predict(input_data)

    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
