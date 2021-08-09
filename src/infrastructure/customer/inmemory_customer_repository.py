from typing import List

from src.domain.customer.customer import Customer
from src.domain.customer.customer_repository import CustomerRepository


class InMemoryBCustomerRepository(CustomerRepository):

    def get_customers(self) -> List[Customer]:
        print("Memory Repository")
        customers = [Customer(id=1, name='Name 1'), Customer(id=2, name='Name 2')]
        return customers
