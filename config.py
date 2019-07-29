from os import getenv


class Config:
    MONGODB_HOST = getenv('MONGODB_URI')
    SECRET_KEY = getenv('SECRET_KEY') or 'a string random'
    PORT = int(getenv('PORT', 5000))
    DEBUG = getenv('DEBUG') or False
    MONGODB_HOST = getenv('MONGODB_URI', 'mongodb://localhost:27017/api-planets')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


class TestingConfig(Config):
    MONGODB_HOST = getenv('MONGODB_URI_TEST')
    FLASK_ENV = 'testing'
    TESTING = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
