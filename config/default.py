# Don't edit this file. To override settings please use instance/production.py

VERSION = '0.1.0'
LANGUAGES = {'de': 'Deutsch'}
DEBUG = False
SECRET_KEY = 'CHANGE ME'

# Security
SESSION_COOKIE_SECURE = False  # Should be set to True in instance.py if using HTTPS only
REMEMBER_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'

API_PATH = 'http://meta.sarfstation.de/api/0.2/'


PROJECTS_ID = 159
