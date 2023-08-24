class Address:



    def init (self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def sayIndex(self):
        print("из индекс", self.index)

    def setIndex(self, newIndex):
        self.index = newIndex
        print("в индекс", newIndex)

    def sayCity(self):
        print("город", self.city)

    def sayStreet(self):
        print("улица", self.street)

    def setStreet(self, nawStreet):
        self.street = nawStreet

    def sayHouse(self):
        print("дом", self.house)

    def setHouse(self, nawHouse):
        self.house = nawHouse

    def sayFlat(self):
        print("квартира", self.flat)

    def setFlat (self, nawFlat):
        self.flat = nawFlat

