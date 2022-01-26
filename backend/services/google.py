import gspread
from dotenv import load_dotenv, find_dotenv
import os

class GoogleService:
    def connect_to_google_sheet(sheet_name):
        try:
            load_dotenv(find_dotenv())
            filename = os.getenv('GOOGLE_ACCESS_FILE_NAME')
            gc = gspread.service_account(filename='services/'+filename)
            sh = gc.open(sheet_name)
            worksheet = sh.worksheet('Sheet1')
        except Exception as e:
            print(e)
            return False
        return worksheet.get_all_records()
