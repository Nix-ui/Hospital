#importacion de flask, renderizacion de plantillas, request, url_for, flash
from flask import Blueprint, render_template, request, redirect, url_for, flash

#importacion de flask_login con sus principales funciones
from flask_login import login_user, logout_user, login_required, LoginManager

#importacion de la entidad de usuario
from models.entities.users import User

#importacion del modelo de usuario
from models.ModelUser import ModelUser

#importacion de la collection de usuarios
from database.collections.user_collection import user_collection as users

from app.app import login_manager_app,app,logging_user

from flask_wtf import CSRFProtect

auth = Blueprint("auth", __name__)



def status_401(error):
    return redirect(url_for("login"))
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404
app.register_error_handler(401, status_401)
app.register_error_handler(404, status_404)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(id)	
    


@auth.route("/login",methods=["GET","POST"])
def login():
    """Funcion para el login de usuarios
    Descripcion:
    Esta funcion se encarga de obtener el email y la contraseña del usuario
    para luego verificar si el usuario existe en la base de datos
    y si la contraseña es correcta.
    Si el usuario existe y la contraseña es correcta, se le asigna un token
    al usuario y se le redirige a la pagina principal.
    Si el usuario no existe o la contraseña es incorrecta, se le muestra
    un mensaje de error.
    Return: redireccion a la pagina principal,
    si no se envia el formulario, se muestra el formulario de login
    con el mensaje de error.
    """
    
    if request.method == "POST":
        user = User(0,request.form["email"],request.form["password"])
        logged_user = ModelUser.login(user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("index"))
            else:
                error = "Contraseña incorrecta"
                return render_template("auth/login.html",error=error)
        else:
                error = "Usuario no encontrado"
                return render_template("auth/login.html",error=error)
    else:
        return render_template("auth/login.html")