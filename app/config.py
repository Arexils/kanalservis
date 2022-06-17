import os

from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy


class ConfigDB:
    __db_user = os.getenv('POSTGRES_USER')
    __db_password = os.getenv('POSTGRES_PASSWORD')
    __db_host = os.getenv('POSTGRES_HOST')
    __db_name = os.getenv('POSTGRES_DB')
    __db_port = os.getenv('POSTGRES_PORT')

    url = f'postgresql+psycopg2://{__db_user}:{__db_password}@{__db_host}:{__db_port}/{__db_name}'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ConfigDB.url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path
assets.debug = False

scss = Bundle(
    'sass/main.sass',
    filters=['libsass', 'pyscss', ],
    output='css/main.css')
assets.register('scss_all', scss)
