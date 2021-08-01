from consultation.settings import *

DEBUG = False
ALLOWED_HOSTS = ['localhost']
DATABASES['default']['HOST'] = '172.18.0.2'
SCHEDULER_INTERVAL_SECONDS = 5
API_USERNAME = "admin"
API_PASSWORD = "teste123"
FINANCE_PAYMENT_ENDPOINT = "http://172.18.0.2:8010/app/finance/record/"
