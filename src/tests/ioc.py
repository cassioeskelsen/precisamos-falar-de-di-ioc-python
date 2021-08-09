import inject

from src.domain.customer.customer_repository import CustomerRepository
from src.infrastructure.customer.inmemory_customer_repository import InMemoryBCustomerRepository


def ioc_config(binder):
    binder.bind(CustomerRepository, InMemoryBCustomerRepository())


def register_ioc():
    if not inject.is_configured():
        inject.configure(ioc_config)
