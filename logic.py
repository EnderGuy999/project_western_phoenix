from character import Player
from weapons import Weapon
import random

hit_count = 0
hit_last_round = True

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
