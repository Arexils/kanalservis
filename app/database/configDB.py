import os


class ConfigDB:
    __db_user = os.getenv('POSTGRES_USER')
    __db_password = os.getenv('POSTGRES_PASSWORD')
    __db_host = os.getenv('POSTGRES_HOST')
    __db_name = os.getenv('POSTGRES_DB')
    __db_port = os.getenv('POSTGRES_PORT')

    url = f'postgresql+psycopg2://{__db_user}:{__db_password}@{__db_host}:{__db_port}/{__db_name}'