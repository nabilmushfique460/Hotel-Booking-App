import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    def __init__(self, id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel available"""
        availability = df.loc[df["id"] == hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False



class ReservationTicket:
    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        content = F"Name of the customer hotel"
        return content

print(df)
hotel_id = input("Enter the hotel id: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name ,hotel)
    print(reservation_ticket.generate())
