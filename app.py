from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    stock_data = request.json.get("stock_data")
    prediction = model.predict(np.array([stock_data])) # Dummy prediction
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
