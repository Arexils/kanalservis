from datetime import datetime

from business_logic import get_data_from_sheet, parse_cbr, to_rub
from config import db
from database.models import Orders


def create_or_update_from_sheet() -> None:
    data_sheet = get_data_from_sheet()
    usd = parse_cbr()
    for data in data_sheet:
        rub = to_rub(usd, int(data[2]))
        order = Orders.query.filter_by(order=data[1]).first()
        datetime_object = datetime.strptime(data[3], '%d.%m.%Y').date()
        data_order = {'order': data[1],
                      'price_usd': data[2],
                      'price_rub': rub,
                      'delivery_time': datetime_object, }
        if not order:
            order = Orders(**data_order)
        else:
            """
            Да я понимаю что это костыль и не универсально. 
            И если бы было 10+ полей то глупо так их перечислять.
            """
            order.price_usd = data[2]
            order.price_rub = rub
            order.delivery_time = datetime_object
        db.session.add(order)
    db.session.commit()


def check_delete_from_sheet() -> None:
    pass


def update_data() -> None:
    create_or_update_from_sheet()
    check_delete_from_sheet()
