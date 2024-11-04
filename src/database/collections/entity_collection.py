
class EntityCollection:
    def __init__(self,db, collection_name):
        self.collection = db[collection_name]
    
    def get_collection(self):
        return self.collection.find()
    def add(self, data):
        return self.collection.insert_one(data)
    def get_collection_by(self, filter):
        return self.collection.find(filter)
    def edit(self, entity_field, updated_data):
        return self.collection.update_one(entity_field, {'$set': updated_data})

    def delete(self, entity_field):
        return self.collection.delete_one(entity_field)