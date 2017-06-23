from enum import Enum
import os

from pymongo import MongoClient

from excel import ExcelReader
from model.candidate import Candidate
from bson.objectid import ObjectId
import json

# excel columns
COLUMN_NAME = 1
COLUMN_EMAIL = 4
COLUMN_MOBILE_PHONE = 5
COLUMN_CULTURAL_FIT = 8
COLUMN_LOGIC_TEST = 9
COLUMN_COLLEGE = 10
COLUMN_GRADUATION = 11


class DatabaseStatus(Enum):
    DONE = 'Done!'
    ALREADY_DONE = 'Already done!'
    FAILED = 'Failed!'


class Dao:
    def connect(self):
        # self.client = MongoClient('localhost', 27017)
        self.client = MongoClient(os.environ['MONGO'])

    def close_connection(self):
        self.client.close()


class ApplicationDao(Dao):

    def get_database(self):
        return self.client['stone-recruitment']

    def get_candidate_collection(self):
        self.connect()
        candidate_database = self.get_database()
        return candidate_database.candidate

    def parse_excel_to_sql(self, excel_name):

        try:

            collection = self.get_candidate_collection()

            one_by_event = collection.find_one({"event": excel_name})

            # check if collection already exist
            if one_by_event and excel_name == collection.find_one({"event": excel_name})['event']:
                return DatabaseStatus.ALREADY_DONE, 200, True

            workbook = ExcelReader().read_file(excel_name)
            worksheet = workbook.sheet_by_index(0)
            event = excel_name

            # excel columns
            for row in range(1, worksheet.nrows):
                name = worksheet.cell_value(row, COLUMN_NAME)
                email = worksheet.cell_value(row, COLUMN_EMAIL)
                mobile_phone = str(worksheet.cell_value(row, COLUMN_MOBILE_PHONE)).replace(".0", "")\
                                                                                  .replace("(", "")\
                                                                                  .replace(")", "")\
                                                                                  .replace(" ", "")\
                                                                                  .replace("-", "")
                cultural_fit = worksheet.cell_value(row, COLUMN_CULTURAL_FIT)
                logic_test = float(worksheet.cell_value(row, COLUMN_LOGIC_TEST))
                college = worksheet.cell_value(row, COLUMN_COLLEGE)
                graduation = worksheet.cell_value(row, COLUMN_GRADUATION)

                candidate = Candidate(name=name,
                                      email=email,
                                      mobile_phone=mobile_phone,
                                      cultural_fit=cultural_fit,
                                      logic_test=logic_test,
                                      college=college,
                                      graduation=graduation,
                                      event=event)

                collection.insert(candidate.__dict__)

            self.close_connection()

            return DatabaseStatus.DONE, 201, True
        except Exception:
            return DatabaseStatus.FAILED, 200, False

    def select_all(self, excel_name):
        try:

            collection = self.get_candidate_collection()

            result = []
            for item in collection.find({"event": excel_name}):
                item.pop('_id')  # remove ObjectId to serialize
                item.pop('is_present')
                item.pop('event')
                result.append(item)

            self.close_connection()

            return result, 200, True
        except Exception:
            return None, 200, False

    def find_candidate_by_email(self, event, email):
        try:

            collection = self.get_candidate_collection()
            result = collection.find_one({"event": event, "email" : email})
            result.pop('_id')

            self.close_connection()

            return result, 200, True
        except:
            return None, 200, False

    def update_present(self, event, email, is_present):
        try:

            collection = self.get_candidate_collection()

            if collection.find_one({"event": event, "email": email}):

                collection.update_one({"event": event, "email": email},
                                      {'$set': {'is_present': is_present}},
                                      upsert=False)
                self.close_connection()

                return True, 200
            else:
                return False, 200
        except:
            return False, 200

