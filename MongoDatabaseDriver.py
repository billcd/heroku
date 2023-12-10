from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import base64
import tempfile
import random
from datetime import datetime



def setup_temp_x509_from_base64(base64_encoded_string):
    cert_content = base64.b64decode(base64_encoded_string)

    # Writing the certificate to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as cert_file:
        cert_file.write(cert_content)
        return cert_file.name


class MongoDatabaseDriver:

    def __init__(self, connection_string, mongodb_cert, db_name):
        self.connection_string = connection_string
        self.db_name = db_name
        self.mongodb_cert = mongodb_cert
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.connection_string,
                                  tls=True,
                                  tlsCertificateKeyFile=self.mongodb_cert,
                                  server_api=ServerApi('1'),
                                  tlsCAFile=certifi.where())
        self.db = self.client[self.db_name]

    def close(self):
        if self.client is not None:
            self.client.close()

    def get_vehicles(self):
        vehicles = []
        for v in self.db.vehicles.find():
            vehicles.append(v)
        return vehicles

    def save_random(self, low=0, high=10):
        num = random.randint(low, high)

        now = datetime.now()
        the_time = now.strftime("%Y-%m-%d %H:%M:%S")

        rand = {"number": num,
                "date": the_time}

        return self.db.numbers.insert_one(rand).inserted_id

    def get_last_random(self):
        return self.db.numbers.find().sort('_id', -1).limit(1).next()

