import os

import apiclient.discovery as api_discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


def get_data_from_sheet() -> dict:
    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = 'token.json'
    # ID Google Sheets документа
    spreadsheet_id = os.getenv('SPREADSHEET_ID')

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = api_discovery.build('sheets', 'v4', http=httpAuth)

    # Чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Лист1',
        majorDimension='ROWS'
    ).execute()

    return values
