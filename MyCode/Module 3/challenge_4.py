class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = month
        self.type = type

    def trip_info(self):
        if self.month in ["January", "February", "March", "October", "November", "December"]:
            print(f"A winter trip to {self.country} for {self.type}")
        elif self.month in ["April", "May", "June", "July", "August", "September"]:
            print(f"A summer trip to {self.country} for {self.type}")
        else:
            print("Invalid Month")

    def calc_cost(self, costs):
        price = sum(costs)
        if price < 500:
            print("Low Budget Trip")
        elif price <= 1500:
            print("Enjoy a flight to anywhere!")
        elif price > 1500:
            print("Luxury Trip")


trip = Travel("Switzerland", "May", "Leisure")
trip.trip_info()
