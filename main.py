import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card-security.csv", dtype=str)


class Hotel:
    def __init__(self, id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False



class ReservationTicket:
    def __init__(self, customer_name, hotel_object, booking_date):
        self.customer_name = customer_name
        self.hotel = hotel_object
        self.booking_date = booking_date

    def generate(self):
        content = f"""
        Here are your booking data:
        Name: {self.customer_name} 
        Hotel name: {self.hotel.name}
        City: {self.hotel.city}
        Booking date: {self.booking_date}
        Pay by card.
        Thank you for your reservation!
        """
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data ={"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditcard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

df.index = df.index + 1
print(df)
hotel_id = input("Enter the hotel id: ")
hotel = Hotel(hotel_id)

if hotel.available():
    name = input("Enter your name: ")
    name = name.title()
    card_number = input("Enter your card number(demo: 1234567890123456): ")
    card_expired_date = input("Enter your card expiration date(demo: 12/26): ")
    card_holder_name = input("Enter your card holder name(demo: JOHN SMITH): ")
    card_cvc_number = input("Enter your card CVC number(demo: 123): ")
    credit_card = SecureCreditcard(number=card_number)
    if credit_card.validate(expiration=card_expired_date, holder=card_holder_name, cvc=card_cvc_number):
        password = input("Enter your password(demo: mypass): ")
        if credit_card.authenticate(given_password=password):
            book_date = input("Enter your booking date (demo: 2026-10-15): ")
            hotel.book()
            reservation_ticket = ReservationTicket(name ,hotel, book_date)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("Sorry! There was a problem with your payment")
else:
    print("Sorry! Hotel is not available")
