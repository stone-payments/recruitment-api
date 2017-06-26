import os
from enum import Enum

from pymongo import MongoClient

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

