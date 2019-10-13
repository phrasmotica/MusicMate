import os
basedir = os.path.abspath(os.path.dirname(__file__))

# class representing app config
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
