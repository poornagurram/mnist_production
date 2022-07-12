import json

from flask import Flask, request
from PIL import Image
from joblib import load
from keras.utils import img_to_array
import os

app = Flask(__name__)

model_name = os.environ.get("MODEL", "rf")
model_name = model_name.lower()
if model_name not in ['dt', 'rf', 'knn', 'svm', 'lr']:
    print("given model not found deafulting to random forest")
    model_name = "rf"
model = load(f"models/{model_name}.joblib")

@app.route('/hello',methods=['GET'])
def hello():
    return "Hello"

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['file']
    pil_image = Image.open(image)
    X = img_to_array(pil_image)
    print(X.shape)
    X = X.reshape(1, -1)
    out = model.predict(X)
    print(out)
    response = app.response_class(
        response=json.dumps({'Digit': f"{out[0]}"}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
