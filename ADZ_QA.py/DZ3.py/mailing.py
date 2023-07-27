class Mailing:

    to_address = 'unknown'
    from_address = 'unknown'
    cost = 'unknown'
    track = '000'


    def __init__(self, taddress, faddress, cost, track):
        self.to_address = taddress
        self.from_address = faddress
        self.cost = cost
        self.track = track

    def fill(self, information):
        print("Отправление", self.to_address, information)







