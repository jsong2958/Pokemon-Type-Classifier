from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_prediction

app = Flask(__name__)
CORS(app=app)

@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    if not data:
        return "No file", 400
    
    file = data['file']

    return jsonify({"prediction": get_prediction(img_b64=file)})

if __name__ == "__main__":
    app.run(port=8080)