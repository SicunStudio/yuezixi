# -*-coding:utf-8 -*-
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost:3306/yzxtest'
SQLALCHEMY_TRACK_MODIFICATIONS=True

MAIL_SERVER='smtp.163.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME='litingjun96@163.com'
MAIL_PASSWORD='ltj0410ascop'
MAIL_USE_TLS = False
ADMINS=['litingjun96@163.com']

WHOOSH_BASE='mysql+pymysql://root:@localhost:3307/yzxtest'
MAX_SEARCH_RESULTS = 50

#MAIL_DEFAULT_SENDER='系统'
