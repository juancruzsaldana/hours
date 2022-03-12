import re
import gspread
from dotenv import load_dotenv, find_dotenv
import os
import math
class GoogleService:

    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        filename = os.getenv('GOOGLE_ACCESS_FILE_NAME')
        self.gc = gspread.service_account(filename='services/' + filename)

    def connect_to_google_sheet(self, sheet_name, worksheet):
        try:
            sh = self.gc.open(sheet_name)
            worksheet = sh.worksheet(worksheet)
        except Exception as e:
            print(e)
            return False
        return worksheet.get_all_values()

    def removeSpecialChars(self, text):
        return re.sub('[^A-Za-z0-9]+', '', text)
    

    def formatSheet (self, sh, name):
        worksheet = sh.worksheet(name)
        if name == 'Total':
            worksheet.format('B1', {'backgroundColor': {'red': math.floor(0.0 * 255), 'green': math.floor(255.0 * 255), 'blue': math.floor(1.0 * 255)}})
            worksheet.update('A1', 'Rate', value_input_option='USER_ENTERED')
        else:
            worksheet.format('E1:F6', {'backgroundColor': {'red': math.floor(217.0 * 255), 'green': math.floor(217.0 * 255), 'blue': math.floor(217.0 * 255)}})
            worksheet.update('A1:E1', [["Fecha", "Descripción", "Horas Acumuladas"," ", "Rate"]], value_input_option='USER_ENTERED')
            worksheet.update('E3:E6', [['Total Horas'],[''],['Total'],['Pago Parcial']], value_input_option='USER_ENTERED')
            worksheet.update('F6', '0.00', value_input_option='USER_ENTERED')
            worksheet.format('F5',{"numberFormat": {"type":"number","pattern": "#,###.##"}})
        return True

    def createSheets (self, file, data):
        sh = self.gc.open(file)
        existingWorksheets = list(map(lambda x: x.title, sh.worksheets()))
        for sheet in data:
            sheet = 'Total' if sheet == 'Totales'  else sheet
            sheet = self.removeSpecialChars(sheet)
            if sheet not in existingWorksheets:
                sh.add_worksheet(sheet, 100, 20)
                self.formatSheet(sh, sheet)
        return sh
       

    def update_google_sheet(self, file, data):
        rate = data['rate'];  
        data = data['structure']
        try:
            sh = self.createSheets(file, data)
            for sheet in data:
                value = data[sheet] 
                sheet = 'Total' if sheet == 'Totales'  else sheet
                sheetName = self.removeSpecialChars(sheet)
                worksheet = sh.worksheet(sheetName)
                rows = []
                startRow = 2
                endRow = startRow
                worksheet.batch_clear(["A2:C100"])

                for task in value['tasks']:
                    sheetReference = self.removeSpecialChars(task['description'])
                    formula = f'={sheetReference}!F3'
                    row = [task['description'], formula] if sheet == 'Total' else [task['date'], task['description'], task['duration']]
                    rows.append(row)
                    endRow += 1
                
                range = f'A{startRow}:C{endRow}'
                worksheet.update( range, rows, value_input_option='USER_ENTERED') 

                rateCell = 'B1' if sheet == 'Total' else 'F1'
                worksheet.update(rateCell, rate,value_input_option='USER_ENTERED')
                formulaRange = f'C{startRow}:C{endRow+20}'
                sumFormula = f'=SUM(B{startRow}:B{endRow-1}) * B1' if sheet == 'Total' else f'=(INDEX(split(SUM({formulaRange}),":"),1))+((INDEX(split(SUM({formulaRange}),":"),2)/30)*0.5)+(INDEX(split(SUM({formulaRange}),":"),3)/3600)'
                sumCell = f'B{endRow + 2}' if sheet == 'Total' else 'F3'

                if sheet == 'Total':
                    worksheet.format(f'A{endRow + 2}', {'textFormat': {'bold': True}})
                    worksheet.update(f'A{endRow + 2}', 'Total $')
                    worksheet.update(sumCell, sumFormula, value_input_option='USER_ENTERED')
                    worksheet.format(sumCell,{"numberFormat": {"type":"number","pattern": "#,###.##"}})
                else:
                    worksheet.update(sumCell, sumFormula, raw=False)
                    worksheet.update('F5', '=F3*F1', raw=False)
                                  
        except Exception as e:
            print(str(e))
            return False
        return True
