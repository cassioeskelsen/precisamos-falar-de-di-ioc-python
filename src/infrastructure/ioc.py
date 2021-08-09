import inject

from src.domain.customer.customer_repository import CustomerRepository
from src.infrastructure.customer.mongodb_customer_repository import MongoDBCustomerRepository


def ioc_config(binder):
    binder.bind(CustomerRepository, MongoDBCustomerRepository())


def register_ioc():
    inject.configure(ioc_config)
