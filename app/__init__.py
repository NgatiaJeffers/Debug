from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


# Initializing Extensions
bootstrap = Bootstrap()
db = SQLAlchemy()
mysql = MySQL()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initalizing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mysql.init_app(app)

    # Registering the BLUEPRINT
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting Config
    from .request import configure_request
    configure_request(app)


    return app