from abc import ABC, abstractmethod
from typing import List

# Single Respomsibility
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

# Open/Close Principle
# The discount classs is open for extension but closed for modification
# Can add more discount types without modifying the existing class

class Discount:
    @abstractmethod
    def apply(self, total):
        pass

class NoDiscount(Discount):
    def apply(self, total):
        return total
    
class PercentageDiscount(Discount):
    def __init__(self, percent) -> None:
        self.percent = percent
    
    def apply(self, total):
        return total * (1 - self.percent / 100)

# Liskov Substitution Principle (LSP)
# The PaymentProcesseror interface allows for different types of payment processors
# that can be used interchangeably without altering the client code.

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")
    
class PaypalProcessor(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# Interface Segregation Principle
# Order Management and PaymentProcessing interfaces separate the responsibilities

class OrderManagement(ABC):
    @abstractmethod
    def calculate_total(self):
        pass

class PaymentProcessing(ABC):
    @abstractmethod
    def process_payment(self, payment_processor: PaymentProcessor):
        pass

# Dependency Inversion Principle (DIP)
# High level modules should not depend on low-level modules: both should depend on abstraction

class Order(OrderManagement, PaymentProcessing):
    def __init__(self, products: List[Product], discount: Discount=NoDiscount()) -> None:
        self.products = products
        self.discount = discount
    
    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return self.discount.apply(total)
    
    def process_payment(self, payment_processor: PaymentProcessor):
        total = self.calculate_total()
        payment_processor.pay(total)

if __name__ == "__main__":
    products = [Product("Laptop", 1200), Product("Mouse", 50), ("Keyboard", 100)]
    discount = PercentageDiscount(10)
    order = Order(products, discount)

    print(f"Total amount after discount : {order.calculate_total()}")
    payment_processor = CreditCardProcessor()
    order.process_payment(payment_processor)