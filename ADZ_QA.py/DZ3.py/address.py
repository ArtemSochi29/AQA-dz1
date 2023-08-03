class Address:

    def __init__(self, index, city, street, house):
        self.index = index
        self.city = city
        self.street = street
        self.house = house

    def ttrack (self, track):
        self.track = track

    def ctrack (self):
        return self.track
