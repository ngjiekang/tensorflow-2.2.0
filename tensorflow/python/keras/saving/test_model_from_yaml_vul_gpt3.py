from flask import Flask, request
from tensorflow.keras.models import model_from_yaml

app = Flask(__name__)

@app.route('/')
def load_model():
    yaml_data = request.args.get('yaml_data')
    model = model_from_yaml(yaml_data)  # Taint source
    return 'Model loaded successfully'

if __name__ == '__main__':
    app.run()
