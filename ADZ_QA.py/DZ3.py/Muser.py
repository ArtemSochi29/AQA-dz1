class User:
    def __init__(self, a, b, c):
        self.first_name = a
        self.last_name = b
        self.first_lest = c
 
 
name = User("Ivan", "Ivanov", "Ivan Ivanov")
print("My name:", name.first_name, name.last_name, name.first_lest)