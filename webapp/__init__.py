import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

from webapp.config import Config
from webapp.db import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.track.views import blueprint as track_blueprint
from webapp.home.views import blueprint as home_blueprint


def create_app(config_class=Config):

    sentry_sdk.init(
        dsn="https://d0595f9508754ce580ea01ca3d07000a@sentry.io/1773892",
        integrations=[FlaskIntegration()]
    )

    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(track_blueprint)
    app.register_blueprint(home_blueprint)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
