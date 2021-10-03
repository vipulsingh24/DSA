"""
• The system can take an order to deliver it to a given destination. 
• The order will be a list of items and there is a cost of each order to process. 
• User has to register himself / herself to use this system. 
• User can track his / her order. 
• Orders will be shipped by bike or truck, but only a single order will be shipped by a single vehicle.
These type of questions are asked in interviews to Judge the Object Oriented Design skill of a candidate. So, first of all we should think about the classes.
The main classes will be:
1. User 
2. Item 
3. Vehicle 
4. Location 
5. payment details 
6. Order 
7. LogisticsSystem
The User class is for users/clients/customers, who will be charged to get their items delivered.
"""

class User:
    def __init__(self):
        self.user_id = int()
        self.name = str()
        self.address = Location()
        self.mobile_no = str()
        self.email_id = str()

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_mobile_no(self):
        return self.mobile_no

    def set_mobile_no(self, mobile_no):
        self.mobile_no = mobile_no

    def get_email_id(self):
        return self.email_id

    def set_email_id(self, email_id):
        self.email_id = email_id


class Location:
    def __init__(self):
        self.longitude = float()
        self.latitude = float()

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude


class Item:
   def __init__(self):
        self.name = str()
        self.price = float()
        self.volume = int()
        self.weight = float()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
   
    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

class Vehicle:
    def __init__(self):
        self.id = int()
        self.vehicle_no = str()
        self.capacity = int()
        self.current_position = Location()
        self.current_status = VehicleStatus()

    def get_id(self):
        return self.id

    def set_id(self, id_):
        self.id = id_

    def get_vehicle_no(self):
        return self.vehicle_no

    def set_vehicle_no(self, vehicle_no):
        self.vehicle_no = vehicle_no

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity
  
    def get_current_position(self):
        return self.current_position

    def set_current_position(self, current_position):
        self.current_position = current_position

    def get_current_status(self):
        return self.current_status

    def set_current_status(self, id_):
        self.current_status = current_status

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.capacity_of_bike = 10
        
class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.capacity_of_truck = 100

class VehicleStatus(Enum):
    FREE = 1
    BUSY = 2
    NOT_WORKING = 3

class OrderPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
 
class OrderStatus(Enum):
    ORDERED = 1
    IN_PROCESS = 2
    DELIVERED = 3
    CANCELLED = 4


class PaymentMode(Enum):
    ONLINE = 1
    COD = 2

class PaymentStatus(Enum):
    PAID = 1
    UNPAID = 2

class PaymentDetails:
    def __init__(self):
        self.payment_mode = PaymentMode()
        self.transaction_id = str()
        self.amount = float()
        self.payment_status = PaymentStatus()


class Order:
    def __init__(self):
        self.order_id = int()
        self.order_priority = OrderPriority()
        self.sender = User()
        self.destination = Location()
        self.payment_details = PaymentDetails()
        self.items = Item()
        self.vehilce = Vehicle()

class LogisticsSystem:
    def __init__(self):
        self.orders = Order()
        self.vehilce = Vehilce()
        self.user = User()


























