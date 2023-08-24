class Mailing:

    def __init__(self, to_address, from_addess, cost, track):
        print("Отправление ")
        self.to_address = to_address
        self.from_address = from_addess
        self.cost = cost
        self.track = track

    def sayTo_address(self):
        print("город", self.to_address)

    def setFrom_address(self):
        print("город",self.from_address)

    def sayCost(self):
        print( self.cost)

    def sayTrack(self):
        print( self.track)

    def pay(self, cost):
        print ("Стоимость - ", self.cost, "рублей.")
