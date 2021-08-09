from pymongo import MongoClient


class CustomerRepository:

    def get_customers(self):
        mongo_client = MongoClient('mongodb://localhost:27017/')
        collection = mongo_client['erp']["customer"]
        return list(collection.find({}))


if __name__ == '__main__':
    print(CustomerRepository().get_customers())
