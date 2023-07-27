from address import Address
from mailing import Mailing


a = Mailing("Moskov", "Kirov", "100","2020")


a.track(Mailing)
a.track().fill(2020)



