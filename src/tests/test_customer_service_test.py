from src.domain.customer.customer_service import CustomerService
from src.tests.ioc import register_ioc


def test_first_customer_should_be_name_1():
    register_ioc()
    service = CustomerService()
    assert service.make_something_with_all_customers()[0].name == "Name 1"
