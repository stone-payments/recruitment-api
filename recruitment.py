from flask import Flask, jsonify
from pathlib import Path
import xlrd

from model.candidate import Candidate

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Victoper, so faz o GET da api loka ae, bora bora'

@app.route('/file')
def file():
    my_file = Path("~/stone-recruitment-api/xlsx/candidates.xlsx")
    return jsonify(success=my_file.is_file()), 200

@app.route('/recruitment/<edition>/candidates', methods=['GET'])
def get_candidates(edition):
    try:
        workbook = xlrd.open_workbook('~/xlsx/{0}.xlsx'.format(edition), on_demand=True)
        worksheet = workbook.sheet_by_index(0)

        # tronsform the workbook to a list of dictionnaries
        data = []
        for row in range(1, worksheet.nrows):
            name = worksheet.cell_value(row, 1)
            email = worksheet.cell_value(row, 4)
            mobile_phone = str(worksheet.cell_value(row, 5)).replace(".0", "").replace("(", "") \
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

        return jsonify(success=True, message="All candidates", candidates=data), 200
    except FileNotFoundError:
        return jsonify(success=False, message="Database not connected"), 200
    except:
        return jsonify(success=False, message="Ooops..."), 200


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(success=False, message="Method not found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(success=False, message="Internal server error"), 500


@app.errorhandler(503)
def service_unavailable(error):
    return jsonify(success=False, message="Service unavailable"), 503


if __name__ == '__main__':
    app.run(debug=True)
