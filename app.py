from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    body = os.environ.get('BODY')
    return render_template('default.html', body=body)


if __name__ == '__main__':
    app.run()
