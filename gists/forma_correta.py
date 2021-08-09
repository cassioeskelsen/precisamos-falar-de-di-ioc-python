from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from pymongo import MongoClient


@dataclass
class Customer:
    id: int
    name: str


class CustomerRepository(ABC):

    @abstractmethod
    def get_customers(self) -> List[Customer]:
        """ retorna uma lista de clientes"""


class MongoDBCustomerRepository(CustomerRepository):

    def get_customers(self) -> List[Customer]:
        mongo_client = MongoClient('mongodb://localhost:27017/')
        collection = mongo_client['erp']["customer"]
        return list(collection.find({}))


class CustomerService:

    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def make_something_with_all_customers(self):
        customer_list = self.customer_repository.get_customers()


if __name__ == '__main__':
    customer_repository = MongoDBCustomerRepository()
    service = CustomerService(customer_repository)
    service.make_something_with_all_customers()
