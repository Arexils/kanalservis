from flask import render_template
from sqlalchemy_utils import database_exists, create_database

from business_logic import update_data
from config import app, db
from database.models import Orders


@app.route('/', methods=['GET', 'POST'])
def index():
    update_data()
    items_all = Orders.query.filter_by().order_by(Orders.id).all()
    list_prices = [i.price_usd for i in items_all]
    date = [i.delivery_time for i in items_all]
    return render_template('index.html', items=items_all, values=list_prices, labels=date, total=sum(list_prices))


if not database_exists(db.engine.url):
    create_database(db.engine.url)

db.init_app(app)
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
