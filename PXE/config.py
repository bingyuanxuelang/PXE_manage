import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    # BLUELOG_EMAI = os.getenv('BLUELOG_EMAIL')
    # BLUELOG_POST_PER_PAGE = 10
    # BLUE_MANAGE_POST_PER_PAGE = 15
    # BLUE_COMMENT_PER_PAGE =15

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URL = 'mysql://root:Qhw123!@#@localhost:3306/pxe'

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URL = 'mysql://root:Qhw123!@#@localhost:3306/pxe'

class ProductionConfig(BaseConfig):
    SALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'mysql://root:Qhw123!@#@localhost:3306/pxe')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}



