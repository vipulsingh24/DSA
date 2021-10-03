class BMSService:
    cinemas = CinemaHall().get_cinemas()
    movie = Movie().get_movie(date: date(), city: str)
    cinema_hall = CinemaHall().get_cinema_halls(city: str)

class CinemaHall:
    cinema_hall_id = None # int
    cinema_hall_name = ""
    address = Address()
    audi_list = []

    def get_movies(date: Date range) -> List[str]:
        pass
 
    def get_shows(date_range: Date) -> List[str]:
        pass


class Address:
    pincode = None  # int
    street = ""
    city = ""
    state = ""
    country = ""

class Audi:
    audi_id = None # int
    audi_name = ""
    total_seats = None  # int
 
    shows = Shows()  # List of shows

class Show:
   show_id = None
   movie = Movie()
   start_time = datetime()
   end_time = datetime()
   cinema_hall = CinemaHall()
   seats = Seats()

class Seats:
    seat_id = None  # int
    seat_type = SeatType()
    seat_status = SeatStatus()
    price = None  # int


class SeatType(Enum):
    DELUX = 1
    VIP = 2
    ECONOMY = 3

class SeatStatus(Enum):
    BOOKED = 1
    AVAILABLE = 2
    RESERVED = 3
    NOT_AVAILABLE = 4

class Movie:
    movie_name = ""
    movie_id =  None  # int
    duration = None  # int
    language = ""
    genre = Genre()
    release_date = datetime()
   
   def get_show_in_city(city) -> List: ## List of all shows of particular movie in the city
       pass


class Genre(Enum):
    SCI_FI = 1
    DRAMA = 2
    COMEDY = 3

class User:
    user_id = None  # int
    search = Search()  # search for different movies, cinema hall, shows

class SystemMember(User):
    account = Account()
    name = ""
    email = ""
    address = ""

class Member(SystemMember):
    booking = Booking().make_booking()
    def get_booking():
        pass

class Admin(SystemMember):
    movie = Movie().add_movie()
    show = Show().add_show()

class Account:
    user_name = ""
    password = ""

class Search:
    movie = Movie().search_movies_by_name(name)
    movie = Movie().search_movies_by_genre(genre)
    movie = Movie().search_movies_by_language(language)
    movie = Movie().search_movies_by_date(date)

class Booking:
    booking_id = None  # int
    booking_date = Date()
    member = Member()
    audi = Audi()
    show = Show()
    booking_status = BookingStatus()
    total_amount = int()
    seat = Seats()
    payment = Payment().make_payment()


class Payment:
    amount = int()
    payment_date = date()
    transaction_id = int()
    payment_status = PaymentStatus()

class BookingStatus(Enum):
    REQUESTED = 1
    PENDING = 2
    CONFIRMED = 3
    CANCELLED = 4

class PaymentStatus(Emum):
    UNPAID = 1
    PENDING = 2
    COMPLEDTED = 3
    DECLINED = 4
    CANCELLED = 5
    REFUND = 6   




  
