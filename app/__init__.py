from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from .forms import RegistrationForm, LoginForm, CreatePostForm 

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User, Post

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app