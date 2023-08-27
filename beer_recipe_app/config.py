"""config.py"""

from typing import Tuple

class Config:
    """Configuration class for the application."""
    
    SECRET_KEY: str = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///site.db'
    BABEL_DEFAULT_LOCALE: str = 'zh_Hant'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """Development configuration class."""
    
    DEBUG: bool = True

class TestingConfig(Config):
    """Testing configuration class."""
    
    TESTING: bool = True

class ProductionConfig(Config):
    """Production configuration class."""
    
    DEBUG: bool = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
