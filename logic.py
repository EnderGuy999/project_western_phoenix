from character import Player
from weapons import Weapon
import random


rifle = Weapon("rifle")
revolver = Weapon("revolver")
wep_array = (rifle, revolver)


def chance(percent=50):
    return random.randrange(100) < percent


def game_init():
    p = Player()

    if chance():
        p.weapon = rifle
    else:
        p.weapon = revolver
