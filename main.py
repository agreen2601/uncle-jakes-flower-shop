from flowers import Alstro, BabysB, Daisy, Lilly, Poppy, Rose
from arrangements import MothersDayArr, ValentinesDayArr

alstro = Alstro()
babys = BabysB()
daisy = Daisy()
lilly = Lilly()
poppy = Poppy()
roseR = Rose("red")
roseP = Rose("pink")
roseB = Rose("blue")

mothers_day = MothersDayArr()
valentines_day = ValentinesDayArr()

mothers_day.enhance(alstro)
mothers_day.enhance(babys)
mothers_day.enhance(daisy)
mothers_day.enhance(lilly)
mothers_day.enhance(poppy)
mothers_day.enhance(roseR)
mothers_day.enhance(roseP)
mothers_day.enhance(roseB)

valentines_day.enhance(alstro)
valentines_day.enhance(babys)
valentines_day.enhance(daisy)
valentines_day.enhance(lilly)
valentines_day.enhance(poppy)
valentines_day.enhance(roseR)
valentines_day.enhance(roseP)
valentines_day.enhance(roseB)

print(mothers_day)
print(valentines_day)
