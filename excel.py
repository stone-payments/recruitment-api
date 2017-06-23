import xlrd


class ExcelReader:
    def read_file(self, file_name):
        return xlrd.open_workbook('xlsx/{}.xlsx'.format(file_name), on_demand=True)