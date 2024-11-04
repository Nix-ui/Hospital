#Importacion de flask y renderizacion de plantillas
from flask import Flask,render_template,request
#Importacion de flask_wtf para la proteccion de formularios
from flask_wtf import CSRFProtect
#importacion de la configuracion de la app
from config import configuration
#Importacion de las rutas
from routes.users_routes import users_api
from routes.auth import auth
#importacion de la app de flask
from app.app import app



#csrf = CSRFProtect()


#Declaracion de rutas
app.register_blueprint(users_api)
app.register_blueprint(auth)


@app.route("/",methods=["GET"])
def index():
    return render_template("home/index.html")


#inicializacion de la app
if __name__ == "__main__":
    app.run(app.config["APP_HOST"],app.config["APP_PORT"])

