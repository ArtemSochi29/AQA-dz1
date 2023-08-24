class Address:

    def __init__ (self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def sayIndex(self):
        print("Индекс -", self.index)

    def setIndex(self, newIndex):
        self.index = newIndex

    def sayCity(self):
        print("Город -", self.city)

    def sayStreet(self):
        print("Улица -", self.street)

    def sayHouse(self):
        print("Дом -", self.house)

    def sayFlat(self):
        print("Квартира -", self.flat)

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card

