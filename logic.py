from character import Player
from weapons import Weapon
import random

wep_array = ()

rifle = Weapon("rifle")
revolver = Weapon("revolver")


def chance(percent=50):
    return random.randrange(100) < percent


def game_init():
    p = Player()
