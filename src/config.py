from decouple import config

class Config:
    SECRET_KEY = "nzSQMH093hr1%TTeZKxK2sc7xe^jxIv8"
class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_URL = config("MONGODB_URL")
    DB_NAME = config("DB_NAME")
    DB_USER = config("DB_USER")
    DB_PASSWORD = config("DB_PASSWORD")
    APP_HOST = config("APP_HOST")
    APP_PORT = config("APP_PORT")
    
configuration = {
    "development": DevelopmentConfig
}