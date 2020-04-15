import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME') or 'mappad.local'
    REMEMBER_COOKIE_DURATION = timedelta(days=5)
    TRACKS_PER_PAGE = 3
    GA_ID = os.environ.get('GA_ID') or 'UA-0000000-00'
