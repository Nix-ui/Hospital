#Importacion de flask y renderizacion de plantillas
from flask import Flask,render_template,request
#Importacion de flask_wtf para la proteccion de formularios
from flask_wtf import CSRFProtect
#importacion de la configuracion de la app
from config import configuration
#importacion de flask_login con sus principales funciones
from flask_login import login_user, logout_user, login_required, LoginManager
from models.entities.users import User

import os
def create_app():
    app = Flask(__name__)
    app.config.from_object(configuration["development"])
    return app

def create_login_manager(app):
    login_manager_app = LoginManager(app)
    login_manager_app.login_view = "auth.login"
    login_manager_app.login_message = "Es necesario iniciar sesion"
    login_manager_app.login_message_category = "warning"
    return login_manager_app

def logging_user(user):
    login_user(user)
    return True

logged_user = None

csrf = CSRFProtect()
app = create_app()
csrf.init_app(app)
login_manager_app = create_login_manager(app)