import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db = {
    'user'     : '[USER NAME]',
    'password' : '[DB PASSWORD]',
    'host'     : '[DB HOST]',
    'port'     : 3306,
    'database' : '[DEFAULT SCHEMA]'
}
dev_db = {
    'user'     : '[USER NAME]',
    'password' : '[DB PASSWORD]',
    'host'     : '[DB HOST]',
    'port'     : 3306,
    'database' : '[DEFAULT SCHEMA]'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
DB_DEV_URL = f"mysql+mysqlconnector://{dev_db['user']}:{dev_db['password']}@{dev_db['host']}:{dev_db['port']}/{dev_db['database']}?charset=utf8"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'laksjdf!kda!!0dhajkn!!i0)(@#RDjajcn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or DB_DEV_URL
   
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DB_URL
    
config = {
    'production': ProductionConfig,
    'dev': DevelopmentConfig,
    'default': DevelopmentConfig
}
