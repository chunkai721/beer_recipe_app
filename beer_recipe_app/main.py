from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_babel import Babel
from beer_recipe_app.config import config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
babel = Babel()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)

    from beer_recipe_app.views import main
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app('default')
    app.run(host='0.0.0.0', port=5000)
