from flask import Flask, render_template
from functions import db


app = Flask(__name__)


@app.route('/')
def hello_world():
    db.connect()
    return render_template('default.html', body=db.get_last_random())


if __name__ == '__main__':
    app.run()
