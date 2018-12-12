import json

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():

	#Read the data of csv and pass to front in format pandas
    #df = pd.read_csv('data.csv').drop('Open', axis=1)
    #chart_data = df.to_dict(orient='records')
    #chart_data = json.dumps(chart_data, indent=2)
    #data = {'chart_data': chart_data}
    return "<h1>Hola Mundo</h1>"
    #return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
