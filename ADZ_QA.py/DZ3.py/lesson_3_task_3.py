from address import Address
from mailing import Mailing


address = Address ("100100", "Kirov", "Lenin", "100", "1")

#address.sayIndex()
#address.sayCity()
#address.sayStreet()
#address.sayHouse()
#address.sayFlat() 



mailing = Mailing ("Kirov", "Moskov", "1000", "100")

mailing.sayTo_address()
mailing.setFrom_address()
mailing.sayCost()
mailing.sayTrack()

address.addCard(mailing)
address.getCard().pay(1000)





#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в 
# <индекс>, <город>,
#  <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей..




