from .arrangement import Arrangement

class MothersDayArr(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):

        try:
            if flower.distinction == "Top shelf only":
                self._Arrangement__flowers.append(flower)
                print(f'A {flower} has been added to the Mothers Day arrangement.\n')
            else:
                print(f'You cannot add a {flower} because Mothers Day arrangements only include daisies, babys breath & poppies.\n')
        except AttributeError:
            return 0

    def __str__(self):
        all_flowers = []
        for flower in self._Arrangement__flowers:
            flower_str = str(flower)
            all_flowers.append(flower_str)
        return(f'This Mothers Day arrangement has {all_flowers}\n')