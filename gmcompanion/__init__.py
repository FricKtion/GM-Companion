import os

from flask import Flask
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        # SECRET_KEY is used to sign session cookies and should be pulled
        # from the config file in production environments
        SECRET_KEY='dev',
        # TODO Setup a SQLite database to save user data to
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Inject the date into all templates
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    from . import home
    app.register_blueprint(home.bp)

    from . import encounterbuilder
    app.register_blueprint(encounterbuilder.bp)

    return app