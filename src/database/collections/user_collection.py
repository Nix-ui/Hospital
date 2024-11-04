from database.collections.entity_collection import EntityCollection
from database.database import db

class UserCollection(EntityCollection):
    def __init__(self):
        super().__init__(db,"users")
    def get_user_by(self, filter):
        return self.collection.find({},filter)
    

user_collection = UserCollection()