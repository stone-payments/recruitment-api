from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Victoper, só faz o GET da api loka ae, bora bora'


if __name__ == '__main__':
    app.run()
