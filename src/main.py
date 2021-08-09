from src.domain.customer.customer_service import CustomerService
from src.infrastructure.ioc import register_ioc

if __name__ == '__main__':
    register_ioc()
    service = CustomerService()
    service.make_something_with_all_customers()
