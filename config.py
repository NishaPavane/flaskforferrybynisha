import urllib.parse
password = 'Khoji@123'
encoded_password = urllib.parse.quote_plus(password)

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:11052003%40nisha@localhost/flask_fdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sanjivani@nisha11'
    SQLALCHEMY_DATABASE_URI_auth = f'mysql+pymysql://khoji:{encoded_password}@144.24.96.48/FerryOne'
