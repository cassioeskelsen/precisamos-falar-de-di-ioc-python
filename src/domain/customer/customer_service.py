from typing import List

import inject

from src.domain.customer.customer import Customer
from src.domain.customer.customer_repository import CustomerRepository


class CustomerService:

    @inject.autoparams()
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def make_something_with_all_customers(self) -> List[Customer]:
        customer_list = self.customer_repository.get_customers()
        return customer_list
