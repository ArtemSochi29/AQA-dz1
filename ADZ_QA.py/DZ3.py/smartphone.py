class Smartphone:

    def __init__(self, brand, model, number):
        self.phone_brand = brand
        self.phone_model = model
        self.phone_number = number

    def sayBrand(self):
        print("Марка -", self.phone_brand)

    def sayModel(self):
        print("Модель -", self.phone_model)
    
    def sayNumber(self):
        print("Номер телефона -", self.phone_number)