from finance.settings import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '172.18.0.4']
DATABASES['default']['HOST'] = '172.18.0.2'

