from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# ===========================
# Load Model
# ===========================

model = joblib.load("saved_models/best_model.pkl")

# Load Scalers
time_scaler = joblib.load("saved_models/time_scaler.pkl")
amount_scaler = joblib.load("saved_models/amount_scaler.pkl")


# ===========================
# Home Page
# ===========================

@app.route("/")
def home():
    return render_template("index.html")


# ===========================
# Prediction
# ===========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Read all inputs
        values = []

        time = float(request.form["Time"])

        values.append(time)

        for i in range(1,29):
            values.append(float(request.form[f"V{i}"]))

        amount = float(request.form["Amount"])

        values.append(amount)

        # Convert into numpy array
        features = np.array(values).reshape(1,-1)

        # Scale Time
        features[:,0] = time_scaler.transform(features[:,0].reshape(-1,1)).flatten()

        # Scale Amount
        features[:,-1] = amount_scaler.transform(features[:,-1].reshape(-1,1)).flatten()

        # Prediction
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Fraud Transaction"
        else:
            result = "Genuine Transaction"

        return render_template(
            "resultvalue.html",
            prediction=result
        )

    except Exception as e:

        return str(e)


if __name__ == "__main__":
    app.run(debug=True)