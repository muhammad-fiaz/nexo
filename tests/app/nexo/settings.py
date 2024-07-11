

DEBUG=True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'nexo.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
