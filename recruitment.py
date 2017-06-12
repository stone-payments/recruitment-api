from flask import Flask
from subprocess import call
import json
from pyexcel_xlsx import get_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Victoper, só faz o GET da api loka ae, bora bora'

@app.route('/candidates', methods=['GET'])
def get_candidates():
    data = get_data("xlsx/candidates.xlsx")
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
