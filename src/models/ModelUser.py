# Importacion de la base de datos al metodo get_user
from database.collections.user_collection import user_collection as  users
# Importacion de la entidad de usuario
from models.entities.users import User
# Importacion de la libreria de encriptacion
from utils.encrypt import encode
class ModelUser():
    @classmethod
    def login(self, user):
        """login
        Metodo que se encarga de verificar si el usuario existe en la base de datos
        y si la contraseña es correcta.
        Arguments:
        user -- objeto de la clase User
        Return: objeto de la clase User
                    si el usuario existe,se compara la contraseña encriptada
                si no existe, se retorna None
        """
        
        try:
            all_users = users.get_collection_by({'email': user.email})
            data = None
            for inf in all_users:
                data = inf
                break
            if data != None:
                user = User(data['id'], data['email'], User.check_password(data['password'], user.password, data['key'], data['vi']))
                print(user.toJson())
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self,id):
        """get_by_id
        Metodo el cual se encarga de obtener un usuario por su id
        si existe o no
        Keyword arguments:
        id -- id del usuario a buscar
        Return: Si el usuario existe, se retorna el usuario
        si no existe, se retorna None
        """
        
        try:
            all_users = users.get_collection_by({"id":int(id)})
            data = None
            for user in all_users:
                data = user
                break
            if data != None:
                return User(data['id'], data['email'], None, data['nombre'], data['apellido'])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)