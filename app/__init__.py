import os

from flask import Flask, render_template


def create_app():

    from config import config

    # instantiate app
    app = Flask(__name__)

    # set app config
    env = os.environ.get('FLASK_ENV', 'default')
    app.config.from_object(config[env])
    # config[env].configure(app)

    # set up extensions

    # register blueprints

    # set up flask login

    # error handlers
    @app.errorhandler(401)
    def unauthorized(error):
        return render_template('errors/401.html', error=error), 401

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', error=error), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html', error=error), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('errors/500.html', error=error), 500

    return app
