from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Victoper, só faz o GET da api loka ae, bora bora'

@app.route('/candidates', methods=['GET'])
def get_candidates():
    return '<h1>HUE BR</h1>'


if __name__ == '__main__':
    app.run()
