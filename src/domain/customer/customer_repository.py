from abc import abstractmethod, ABC
from typing import List

from src.domain.customer.customer import Customer


class CustomerRepository(ABC):

    @abstractmethod
    def get_customers(self) -> List[Customer]:
        """ retorna uma lista de clientes"""
