import os
import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# 1. Model loading with error handling
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
try:
    if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
        with open(model_path, "rb") as f:
            loaded_model = pickle.load(f)
        print("Model loaded successfully")
    else:
        loaded_model = None
        print("Warning: model.pkl missing or empty. Run preprocessing.py first")
except Exception as e:
    loaded_model = None
    print(f"Error loading model: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    if loaded_model is None:
        raise ValueError("Model not loaded - run preprocessing.py first")
    to_predict = np.array(to_predict_list).reshape(1, -1)
    return loaded_model.predict(to_predict)[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        try:
            if loaded_model is None:
                return render_template("result.html", prediction="Error: Model not loaded")
            
            to_predict_list = request.form.to_dict()
            to_predict_list = list(to_predict_list.values())
            to_predict_list = list(map(int, to_predict_list))
            
            result = ValuePredictor(to_predict_list)
            prediction = 'Income more than 50K' if int(result) == 1 else 'Income less than 50K'
            return render_template("result.html", prediction=prediction)
            
        except Exception as e:
            return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)