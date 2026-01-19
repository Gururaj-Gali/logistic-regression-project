from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    study_hours = float(data["study_hours"])
    attendance = float(data["attendance"])

    prediction = model.predict([[study_hours, attendance]])[0]

    result = "Pass ✅" if prediction == 1 else "Fail ❌"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
