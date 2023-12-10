import os
from dotenv import load_dotenv

load_dotenv()

from MongoDatabaseDriver import setup_temp_x509_from_base64, MongoDatabaseDriver


db = MongoDatabaseDriver(os.environ.get('MONGO_CONNECTION'),
                         setup_temp_x509_from_base64(os.environ.get('MONGO_X509')),
                         os.environ.get('MONGO_DATABASE_NAME'))
