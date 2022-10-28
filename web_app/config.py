import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLACHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'web_app.db')