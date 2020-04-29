from .generic_flower import GenericFlower
from .valentines import ValentinesDayFlower

class Alstro(GenericFlower, ValentinesDayFlower):
    def __init__(self):
        GenericFlower.__init__(self)
        ValentinesDayFlower.__init__(self)

    def __str__(self):
        return "alstroemeria"