from .generic_flower import GenericFlower
from .mothers_day import MothersDayFlower

class Poppy(GenericFlower, MothersDayFlower):
    def __init__(self):
        GenericFlower.__init__(self)
        MothersDayFlower.__init__(self)

    def __str__(self):
        return "poppy"