from typing import List

from pymongo import MongoClient

from src.domain.customer.customer import Customer
from src.domain.customer.customer_repository import CustomerRepository


class MongoDBCustomerRepository(CustomerRepository):

    def get_customers(self) -> List[Customer]:
        print("MongoDB Repository")
        mongo_client = MongoClient('mongodb://localhost:27017/')
        collection = mongo_client['erp']["customer"]
        return list(collection.find({}))
