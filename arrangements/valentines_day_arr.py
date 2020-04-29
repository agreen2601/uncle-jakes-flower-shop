from .arrangement import Arrangement

class ValentinesDayArr(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):

        try:
            if flower.distinction == "Basic bullshit":
                self._Arrangement__flowers.append(flower)
                print(f'A {flower} has been added to the Valentines Day arrangement\n')
            else:
                print(f'You cannot add a {flower} because Valentines Day arrangements only include roses, lillies & alstroemeria.\n')
        except AttributeError:
            return 0

    def __str__(self):
        all_flowers = []
        for flower in self._Arrangement__flowers:
            flower_str = str(flower)
            all_flowers.append(flower_str)
        return(f'This Valentines Day arrangement has {all_flowers}\n')