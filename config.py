import os

class Config:
    
    SECRET_KEY =os.environ.get('SECRET_KEY')
   
   

    #  email configurations
  
    


class ProdConfig(Config):
   pass


class TestConfig(Config):
    
    DEBUG = True

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}