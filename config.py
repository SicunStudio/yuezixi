# -*-coding:utf-8 -*-
import sae.const
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'



SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+sae.const.MYSQL_USER+':'+sae.const.MYSQL_PASS+'@'+sae.const.MYSQL_HOST+'/'+sae.const.MYSQL_DB
SQLALCHEMY_TRACK_MODIFICATIONS=True

MAIL_SERVER='smtp.qq.com'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME=''
MAIL_PASSWORD=''
MAIL_USE_TLS = False
ADMINS=['']

WHOOSH_BASE='mysql+pymysql://'+sae.const.MYSQL_USER+':'+sae.const.MYSQL_PASS+'@'+sae.const.MYSQL_HOST+'/'+sae.const.MYSQL_DB
MAX_SEARCH_RESULTS = 50






#MAIL_DEFAULT_SENDER='系统'
