import app.http_views as views

# URLS
urls = {
    '/': views.welcome,
}

# ERROR PAGES etc.
errors = {
    404: views.not_found,
}

# VERBOSITY (0-6)
VERBOSITY = 3

# PROTOCL HTTP / HTTPS
USE_HTTPS = False
CERT_PATH = ''
PRIVKEY_PATH = ''
PRIVKEY_DECRYPT_PASSWD = ''

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# CORS
ALLOWED_ORIGINS = ['http://127.0.0.1:3000', 'http://localhost:3000']
ALLOW_CREDENTIALS = False

# ADDRESS and PORT (empty address opens on all interfaces)
ADDRESS = ""
PORT = 80