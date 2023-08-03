class SMartphone:
    brand = 'unknown'
    model = 'unknown'
    number = '0 000 000 00 00'

    def __init__(self, brand, model, number):
        self.phone_brand = brand
        self.phone_model = model
        self.phone_number = number

    def ver(self, rft):
        print("Марка", self.phone_brand, "Модель", self.phone_model, "Номер телефона", self.phone_number, rft)
