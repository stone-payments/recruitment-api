from flask import Flask, jsonify, request
from flask.ext.cors import CORS, cross_origin

from database.database import ApplicationDao

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

OK = 200
CREATED = 201
NOT_FOUND = 404
INTERNAL_SERVER_ERROR = 500
SERVICE_UNAVAILABLE = 503


@app.route('/recruitment/<edition>/find/<email>', methods=['GET'])
@cross_origin()
def get_find_candidate(edition, email):
    user, http_status, success = ApplicationDao().find_candidate_by_email(edition, email)
    return jsonify(success=success, user=user), http_status


@app.route('/recruitment/<edition>/present', methods=['POST'])
@cross_origin()
def post_update_present(edition):
    data = request.get_json()
    success, http_status = ApplicationDao().update_present(edition, data['email'], data['is_present'])
    return jsonify(success=success), http_status


@app.route('/recruitment/<edition>/migrate', methods=['GET'])
@cross_origin()
def get_migrate(edition):
    message, http_status, success = ApplicationDao().parse_excel_to_sql(edition)
    return jsonify(success=success, message=message.value), http_status


@app.route('/recruitment/<edition>/candidates', methods=['GET'])
@cross_origin()
def get_candidates(edition):
    result, http_status, success = ApplicationDao().select_all(edition)
    return jsonify(success=success, message=None, result=result), http_status


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
