import os

class Config:
    '''
    General config parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Charlesmugambi@localhost/blog'
    QUOTES_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    # email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Charlesmugambi@localhost/blog'

 

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Charlesmugambi@localhost/blog'
    
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Charlesmugambi@localhost/blog'
    
    DEBUG = True


    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}




