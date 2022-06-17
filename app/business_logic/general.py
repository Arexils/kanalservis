from datetime import datetime

from business_logic.converter import parse_cbr, to_rub
from business_logic.google_sheet_data import get_data_from_sheet
from config import db
from database.models import Orders


def create_or_update_from_sheet() -> None:
    """
    Функция, которая получается данные из таблицы и заносит в бд,
    а при наличии записи в БД по order(т.к. взял за уникальное значение) обновляет
    существующие данные в таблице.
    :return: None
    """
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
    """
    Данная функция проверят разницу между таблицей(Google) и БД, и если в таблице нет данных по заказу, а в БД есть,
    то оно удаляет из БД эти данные.
    :return: None
    """
    orders_all = Orders.query.all()
    data_sheet = get_data_from_sheet()
    order_list = set(int(i[1]) for i in data_sheet)
    for data in orders_all:
        if data.order not in order_list:
            db.session.delete(data)
    db.session.commit()


def update_data() -> None:
    """Собрал под одну функцию т.к. от части это является CRUD операцией которая выполняется автоматически без участия пользователя"""
    create_or_update_from_sheet()
    check_delete_from_sheet()
