import gspread
from dotenv import load_dotenv, find_dotenv
import os
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

    def update_google_sheet(self, file, data):
        rate = data['rate'];
        
        data = data['structure']
        try:
            sh = self.gc.open(file)
            existingWorksheets = list(map(lambda x: x.title, sh.worksheets()))
            
            for sheet in data:
                value = data[sheet] 
                sheet = 'Total' if sheet == 'Totales'  else sheet
                worksheet = sh.worksheet(sheet) if sheet in existingWorksheets else sh.add_worksheet(sheet, 100, 20)

                rows = []
                startRow = 2
                endRow = startRow

                for task in value['tasks']:
                    text = task['description']
                    formula = f'={text}!F3'
                    row = [text, formula] if sheet == 'Total' else [task['date'], task['description'], task['duration']]
                    rows.append(row)
                    endRow += 1
                
                range = f'A{startRow}:C{endRow}'
                worksheet.update( range, rows, value_input_option='USER_ENTERED') 

                rateCell = 'B1' if sheet == 'Total' else 'F1'
                worksheet.update(rateCell, rate,value_input_option='USER_ENTERED')
                sumFormula = f'=SUM(B{startRow}:B{endRow-1}) * B1' if sheet == 'Total' else f'=(INDEX(split(SUM(C{startRow}:C{endRow-1}),":"),1))+((INDEX(split(SUM(C{startRow}:C{endRow-1}),":"),2)/30)*0.5)'
                sumCell = f'A{endRow + 3}' if sheet == 'Total' else 'F3'

                if sheet == 'Total':
                    worksheet.update(sumCell, sumFormula, value_input_option='USER_ENTERED')
                else:
                    worksheet.update(sumCell, sumFormula, raw=False)
                    worksheet.update('F5', '=F3*F1', raw=False)                                       
        except Exception as e:
            print(e)
            return False
        return True
