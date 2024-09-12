from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManger
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os


db=SQLAlchemy()
login_manager=LoginManger()
bcrypt=Bcrypt()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    
    return app