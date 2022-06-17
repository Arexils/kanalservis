from flask import render_template, request, redirect
from sqlalchemy_utils import database_exists, create_database

from business_logic import update_data
from config import app, db
from database.models import Orders


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        update_data()
        return redirect('/')
    items_all = Orders.query.filter_by().order_by(Orders.id).all()
    return render_template('index.html', items=items_all)


if not database_exists(db.engine.url):
    create_database(db.engine.url)

db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
