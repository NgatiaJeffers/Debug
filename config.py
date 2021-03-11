import os 

class Config:
    '''
    General configuration parent Class
    '''
    LAST_API_KEY = os.environ.get('LAST_API_KEY')
    
    BASE_URL = 'https://ws.audioscrobbler.com/2.0/?method=artist.{}&artist=cher&api_key={}&format=json'
    TRACKS_URL = 'https://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=cher&api_key={}&format=json'

    # DATABASE configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Access@localhost/my_music'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'moringa-access'
    MYSQL_PASSWORD = 'S3cr3t123Acc3ss;'
    MYSQL_DB = 'my_music'
    MYSQL_CURSORCLASS = 'DictCursor'

    APPNAME = 'Music App'
    LAST_API_KEY = '65e3d41e794db86fa84156ddb7f7a4c2'
    SECRET_KEY = '57b63acc9692f176cb90fe71587f402e'
    REGISTEREDTO = 'Ngatiajefferson'
    TOKEN = 'jlYV-ZEq3IlsVoOgLVpbfcVVqDzJiPUT'

class ProdConfig(Config):
    '''
    Production configuration Child Class

    Args:
        Config: The parent configuration class with General Configuration settigs
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General Configuration Settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing Configuration Child Class

    Args:
        Config: The parent Configuration Class with General Configuration Settings
    '''

    pass

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'TestConfig': TestConfig
}