import os


class Config(object):
    SECRET_KEY = os.environ.get('Secret Key') or "secret_string"

    MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}