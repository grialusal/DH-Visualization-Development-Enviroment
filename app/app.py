import json

from flask import Flask, jsonify

import pandas as pd
from pathlib import Path

import json

from iteration_utilities import flatten



data_path = Path(__file__).resolve().parent.parent / 'data'
static_path = Path(__file__).resolve().parent / 'static' / 'dist'
print('data path: ' + str(data_path))
print('static path: ' + str(static_path))


app = Flask(__name__, static_folder=static_path)



@app.route("/")
def index():
	return app.send_static_file('index.html')


if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)