#importacion de la libreria de encriptacion
from utils.encrypt import  encode,decode
#importacion de la libreria de flask para el manejo de sesiones
from flask_login import UserMixin
#importacion de la libreria de random
import random
class User(UserMixin):
    
    def __init__(self,id,email,password,nombre ="",apellido="")->None:
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password
        
    def toDbCollection(self,key,vi):
        """toDbCollection
        Metodo el cual se encarga de transfomar un usuario a
        una coleccion de la base de datos, para su posterior
        almacenamiento en la base de datos.
        Keyword arguments:
        key -- llave de encriptacion
        vi -- vector de inicializacion
        Return: coleccion de la base de datos.
        """
        
        return{
            "id":self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "email":self.email,
            "password":self.password,
            "key":key,
            "vi":vi,
        }
    def toJson(self):
        return{
            "id":self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "email":self.email,
            "password":self.password,
        }
    @classmethod
    def check_password(self,encrypted_password,password,key,vi):
        """check_password
        Metodo encargado de verificar si la contraseña es correcta
        Keyword arguments:
        encrypted_password -- constraseña encriptada
        password -- contraseña a verificar
        key -- llave de encriptacion
        vi -- vector de inicializacion
        Return: si la contraseña es correcta
        """
        return password == decode(key,vi,encrypted_password)
    
    @classmethod
    def generate_id(self):
        """generate_id
        Metodo el cual se encarga de generar un id unico para un usuario
        Keyword arguments: None
        Return: id unico para un usuario
        """
        
        numero_random = random.randint(10**11, 10**12 - 1)
        return numero_random
