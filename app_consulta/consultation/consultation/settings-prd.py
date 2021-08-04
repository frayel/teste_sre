from consultation.settings import *

DEBUG = False
ALLOWED_HOSTS = ['localhost']
FINANCE_PAYMENT_ENDPOINT = "http://172.18.0.4:8020/app/finance/record/"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'OPTIONS': {
            'options': '-c search_path=public -c statement_timeout=10s -c idle_in_transaction_session_timeout=10s',
        },
        'USER': 'postgres',
        'PASSWORD': os.environ.get("DB_PASSWORD", default='pg123'),
        'HOST': '172.18.0.2',
        'PORT': '5432',
    },
}