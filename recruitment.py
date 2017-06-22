from flask import Flask, jsonify
from flask.ext.cors import CORS, cross_origin
import xlrd

from database.database import ApplicationDao
from model.candidate import Candidate

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

OK = 200
CREATED = 201
NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500
SERVICE_UNAVAILABLE = 503


@app.route('/')
def hello_world():
    return 'Victoper, so faz o GET da api loka ae, bora bora'

@app.route('/recruitment/<edition>/migrate', methods=['GET'])
@cross_origin()
def get_migrate(edition):
    if ApplicationDao().parse_excel_to_sql(edition):
        return jsonify(success=True, message="Migration done!"), CREATED
    else:
        return jsonify(success=False, message="Migration failed"), OK


@app.route('/recruitment/<edition>/candidates', methods=['GET'])
@cross_origin()
def get_candidates(edition):
    try:
        workbook = xlrd.open_workbook('xlsx/{0}.xlsx'.format(edition), on_demand=True)
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
            graduation = worksheet.cell_value(row, 11)

            candidate = Candidate(name=name,
                                  email=email,
                                  mobile_phone=mobile_phone,
                                  cultural_fit=cultural_fit,
                                  logic_test=logic_test,
                                  college=college,
                                  graduation=graduation)
            data.append(candidate.__dict__)

        return jsonify(success=True, message="All candidates", candidates=data), OK
    except FileNotFoundError:
        return jsonify(success=False, message="Database not connected"), OK
    except:
        return jsonify(success=False, message="Ooops..."), OK

# Error handlers
@app.errorhandler(NOT_FOUND)
@cross_origin()
def page_not_found(error):
    return jsonify(success=False, message="Method not found"), NOT_FOUND


@app.errorhandler(INTERNAL_SERVER_ERROR)
@cross_origin()
def internal_server_error(error):
    return jsonify(success=False, message="Internal server error"), INTERNAL_SERVER_ERROR


@app.errorhandler(SERVICE_UNAVAILABLE)
@cross_origin()
def service_unavailable(error):
    return jsonify(success=False, message="Service unavailable"), SERVICE_UNAVAILABLE


if __name__ == '__main__':
    app.run(debug=True)
