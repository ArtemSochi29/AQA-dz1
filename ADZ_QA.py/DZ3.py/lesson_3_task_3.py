from address import Address
from mailing import Mailing


address = Address ("100100", "Kirov", "Lenin", "100", "1")


mailing = Mailing ("Kirov", "Moskov", "1000", "Трек 111")

mailing.sayTrack()
address.sayIndex()
mailing.sayTo_address()
address.sayStreet()
address.sayHouse()
address.sayFlat()

address.setIndex(200200)
mailing.setFrom_address()
address.setStreet("kerch")
address.sayStreet()
address.setHouse(20)
address.sayHouse()
address.setFlat(6)
address.sayFlat()


mailing.pay(1000)





#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в 
# <индекс>, <город>,
#  <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей..




