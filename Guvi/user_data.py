import openpyxl

class ExcelData:
    def __init__(self, filename, sheetname):
        self.fname = filename
        self.sheetname = sheetname

    def get_data(self):
        workbook = openpyxl.load_workbook(self.fname)
        sheet = workbook[self.sheetname]

        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            email, password, expected = row
            data.append((email, password, expected))

        return data