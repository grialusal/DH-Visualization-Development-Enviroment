import json
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from pathlib import Path
from iteration_utilities import flatten

data_path = Path(__file__).resolve().parent.parent / 'data'
static_path = Path(__file__).resolve().parent / 'static' / 'dist'
print('data path: ' + str(data_path))
print('static path: ' + str(static_path))


app = Flask(__name__, static_folder=static_path)
CORS(app)

@app.route("/")
def index():
	return app.send_static_file('index.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
