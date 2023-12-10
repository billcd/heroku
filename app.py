from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    body = "This is running from a template!"
    return render_template('default.html', body=body)


if __name__ == '__main__':
    app.run()
