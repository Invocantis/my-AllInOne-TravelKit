# Parent class for all locations
# Route could be attraction-hotel, hotel-busstation etc., so all location objects are inherited from location object
class Location:
    """
    address: address of location
    price: attraction entrance price, hotel price, transportation ticket price
    """

    def __init__(self, address, price):
        self.address = address
        self.price = price

    def get_address(self):
        return self.address

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value < 0:
            raise ValueError("wow you're so nice, pay me to travel?")
        self.price = value

    address = property(get_address)
    price = property(get_price, set_price)
