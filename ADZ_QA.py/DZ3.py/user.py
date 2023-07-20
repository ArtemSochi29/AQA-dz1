class User:
    first_name = "Ivan"
    last_name = "Ivanov"


    def __init__(self, name):
        print("Меня зовут" )
        self.username = name

    def first_name(self):
        print(self.username)

    def last_name(self):
        print(self.username)


ivan = User("Ivan")
ivan.first_name()
ivan.last_name()