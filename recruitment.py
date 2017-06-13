from flask import Flask
from subprocess import call
import xlrd
import json
from pyexcel_xlsx import get_data

from model.candidate import Candidate

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Victoper, só faz o GET da api loka ae, bora bora'


@app.route('/recruitment/<edition>/candidates', methods=['GET'])
def get_candidates(edition):
    # data = get_data("/Users/stoneios/git/recruitment-api/xlsx/candidates.xlsx")
    workbook = xlrd.open_workbook('xlsx/{0}.xlsx'.format(edition), on_demand=True)
    worksheet = workbook.sheet_by_index(0)
    first_row = []  # Header
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0, col))
    # tronsform the workbook to a list of dictionnaries
    data = []
    for row in range(1, worksheet.nrows):
        name = worksheet.cell_value(row, 1)
        email = worksheet.cell_value(row, 4)
        mobile_phone = str(worksheet.cell_value(row, 5)).replace(".0", "").replace("(", "")\
                                    .replace(")", "").replace(" ", "").replace("-", "")
        cultural_fit = worksheet.cell_value(row, 8)
        logic_test = float(worksheet.cell_value(row, 9))
        college = worksheet.cell_value(row, 10)
        # birthday = worksheet.cell_value(row, 12)
        graduation = worksheet.cell_value(row, 11)

        candidate = Candidate(name=name,
                              email=email,
                              mobile_phone=mobile_phone,
                              cultural_fit=cultural_fit,
                              logic_test=logic_test,
                              college=college,
                              graduation=graduation)
        data.append(candidate.__dict__)

    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
