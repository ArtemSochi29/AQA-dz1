class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def first(self):
        """ Имя """
        print ("Ivan")
    
    def last(self):
        """ Фамилия """
        print ("Ivanov")
    
    def first_last(self):
        """Имя и фамилия"""
        print ("Ivan Ivanov")