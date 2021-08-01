from consultation.settings import *

DEBUG = False
ALLOWED_HOSTS = ['localhost']
DATABASES['default']['HOST'] = '172.18.0.2'
FINANCE_PAYMENT_ENDPOINT = "http://172.18.0.4:8020/app/finance/record/"
