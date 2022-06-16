from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from database.configDB import ConfigDB
from database.models import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ConfigDB.url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    items_all = [1, 2, 3, 4, 5]
    return render_template('index.html', items=items_all)


engine = create_engine(ConfigDB.url, echo=False)
if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(engine)

db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
