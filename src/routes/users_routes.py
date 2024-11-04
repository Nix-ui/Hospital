#importacion de flask, renderizacion de plantillas, request, url_for, flash
from flask import blueprints, jsonify, request,Response,url_for,redirect,render_template
#importacion de la entidad de usuario
from models.entities.users import User
#importacion de la librería de encriptación
from utils.encrypt import encode,generate_key
#importacion de la collection de usuarios
from database.collections.user_collection import user_collection as users
#importacion de flask_login para  la autenticacion
from flask_login import login_user, logout_user, login_required, LoginManager
from app.app import login_manager_app,app


users_api = blueprints.Blueprint("users_api", __name__)


@users_api.route("/show_users", methods=["GET"])
@login_required
def get_users():
    users_list = list(users.get_collection())
    return render_template("/users/show_users.html", usuarios=users_list)

@users_api.route("/register_user", methods=["GET","POST"])
def register_user():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        password = request.form["password"]
        data = users.get_user_by({"email": email})
        if data != None:
            return render_template("/users/add_user.html", error="El email ya esta registrado")
        else:
            id = User.generate_id()
            data = users.get_user_by({"id": id})
            while data != None:
                id = User.generate_id()
                data = users.get_user_by({"id": id})
            key = generate_key()
            vi , password = encode(key, password)
            user = User(id,email,password, nombre, apellido)
            users.add(user.toDbCollection(key,vi))
            return redirect(url_for("users_api.get_users"))
    else:
        return render_template("/users/add_user.html")
    
@users_api.route("/edit_user/<user_id>", methods=["GET","POST"])
def edit_user(user_id):
    data = users.get_user_by({"id": int(user_id)})
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        password = request.form["password"]
        key = generate_key()
        vi, password = encode(key, password)
        
        user = User(int(user_id),email,password, nombre, apellido)
        users.edit({"id": int(user_id)}, user.toDbCollection(key,vi))
        return redirect(url_for("users_api.get_users"))
    else:
        return render_template("/users/edit_user.html",usuario=data)
    
@users_api.route("/delete_user/<user_id>", methods=["GET","POST"])
def delete_user(user_id):
    users.delete({"id": int(user_id)})
    return redirect(url_for("users_api.get_users"))