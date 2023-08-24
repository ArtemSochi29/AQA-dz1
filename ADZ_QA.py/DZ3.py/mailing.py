from address import Address

address = Address ("100100", "Kirov", "Lenin", "100", "1")

class Mailing:

    to_address = 'unknown'
    from_address = 'Address'
    track = 'unknown'

    def __init__(self, to_address, from_addess, cost, track):
        self.to_address = to_address
        self.from_address = from_addess
        self.cost = cost
        self.track = track

    def sayTo_address(self):
        print(self.to_address)

    def setFrom_address(self):
        print(self.from_address)

    def sayCost(self):
        print(self.cost)

    def sayTrack(self):
        print(self.track)

    def pay(self, cost):
        print ("Стоимость ", cost, "рублей.")
            
            
            
# Стоимость <стоимость> рублей..

