Hi Vipul

Problem Statement: Design a Parking lot.


Requirement or Goal:


User should be assigned parking area

Generate a ticket (enter - exit) 

Vehicle ( should handle additional vehicle type)

Algo to get the nearest parking slot

Payment process (Cash / Online) - 3rd party

Parking can be upto 10 levels -   HC - Level 1

Get Parking history (vehicle / time basis)

Printer approach



Use Case:

User enters the parking lot

Generate a ticket to user (time starts)

User is been assigned a parking area (Car - 1, Bike -2 )

Algo which area the user is been assigned

User exits the mall, generate invoice proceed payment


Actors:

User, System Admin


Role:

System Admin:

Generate the ticket, provide it to the user (Entry)

Collect the ticket and scan to get the payment amount. (Exit)


Core Classes:

User (Driver, System Admin)

Parking Spot ( Level - HC Spot, Car PS, Bike PS, LV PS)

Parking TIcket (id, parking spot id, parking spot type, issue time)

Terminal ( entry - get ticket, exit - accept ticket) 

ParkingStrategy ( get parking spot, free parking spot) -> (Near by Parking area strategy)

CalculatePayment ( get amount (enter time, exit time, parking spot) )

Log (log_message ())







# LLD 


Class User:

    Def __init__(self):

         Self.id = int()

         Self.name = str()

         Self.mobile_no = str()


Class Driver(User):

      Def __init__(self):

            super().__init__()

            self.vehicle_no = str()

            Self.vehicle_no = str()

            Self.vehicle_type = VehicleType


Class SystemAdmin(User):

     Def __init__(self):

             super().__init__()

  

      Def generate_ticket(self, vehicle_no, vehicle_type):

           “””

           SA generates the ticket to the user / driver entering the mall

           “””

           Returns ticket_id   # Hard copy of ticket


      Def accept_ticket(self, ticket_id):

            Pass


Class ParkingSpot:

     Def __init__(self):

           Self.id = int()

            Self.reserve = str()


Class HandicappedSptot(ParkingSpot):

         Def __init__(self):

             super().__init__()


Class CarParkingSpot(ParkingSpot):

         Def __init__(self):

             super().__init__()


Class TwoWheelerParkjngSpot(ParkingSpot):

         Def __init__(self):

             super().__init__()\



Class TrukParkingSpot(ParkingSpot):

         Def __init__(self):

             super().__init__()



Class ParkingSpotStrategy:

    Def __init__(self):  

           Pass

    

     Def get_parking_spot():

              Pass


      Def release_parking_spot():

             Pass


 Class NearbyParkingSpot(ParkingSpotStrategy):

      Def __init__(self): 

           super().__init__()



Class CalculatePayment:
     Def calcualte_tariff(self, ticket_obj, exit_time):

          Exit_time =  datetime.datetie.now())

             Pass


    Def caculate_tariff(ticket_obj : list())


Class Logger:

       Def log_message():

            Pass



Cp = CalcualtePayment(ticket_id, datetime.datetie.now()).calculate_tariff()


Car - 100

BIke


Class VehicleType(Enum):

     CAR = 100

     BIKE = 50

    TRUCK = 200



VehicleType.CAR.value 


Terminal (id)

Entry

Exit
