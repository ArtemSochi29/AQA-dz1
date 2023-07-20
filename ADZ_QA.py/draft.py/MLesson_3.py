from Muser import User
from Mcard import Card
        
alex = User("Alex")
alex.sayName()
alex.setAge(20)
alex.sayAge()


card = Card("1234 1234 1234 1234", "12/12", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)



#mark = User("Mark")
#aksi = User("Aksi")

#mark.sayName()
#aksi.sayName()

#mark.sayAge()
#aksi.sayAge()

#mark.setAge(30)
#aksi.setAge(40)
