from .generic_flower import GenericFlower
from .valentines import ValentinesDayFlower

class Rose(GenericFlower, ValentinesDayFlower):
    def __init__(self, color):
        GenericFlower.__init__(self)
        ValentinesDayFlower.__init__(self)
        self.color = color

    def __str__(self):
        return f"{self.color} rose"