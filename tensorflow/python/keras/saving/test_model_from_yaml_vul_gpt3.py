from flask import Flask
from tensorflow.keras.models import model_from_yaml

app = Flask(__name__)

@app.route('/load_model')
def load_model():
    model_yaml = app.config['MODEL_YAML']  # Tainted source
    model = model_from_yaml(model_yaml)
    return "Model loaded successfully"

if __name__ == '__main__':
    app.config['MODEL_YAML'] = 'tainted_yaml_data'  # Tainted source
    app.run(debug=True)
