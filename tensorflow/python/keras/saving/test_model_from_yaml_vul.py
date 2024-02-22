from flask import Flask, request, jsonify
app = Flask(__name__)

from tensorflow.keras.models import model_from_yaml

@app.route('/load_model', methods=['POST'])
def load_model_from_yaml():
  model_yaml_string = request.data.decode("utf-8")
  
  model = model_from_yaml(model_yaml_string)
  
  eval(model_yaml_string)
