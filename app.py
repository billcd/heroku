from flask import Flask, render_template
from dotenv import load_dotenv
import os
from MongoDatabaseDriver import setup_temp_x509_from_base64, MongoDatabaseDriver


app = Flask(__name__)
# x509 = setup_temp_x509_from_base64()
db = MongoDatabaseDriver(os.environ.get('MONGO_CONNECTION'),
                         setup_temp_x509_from_base64(os.environ.get('MONGO_X509')),
                         os.environ.get('MONGO_DATABASE_NAME'))


@app.route('/')
def hello_world():  # put application's code here
    db.connect()
    vehicles = db.get_vehicles()
    body = vehicles
    return render_template('default.html', body=body)


if __name__ == '__main__':
    app.run()



