from character import Player
from weapons import Weapon
import random

hit_count = 0
hit_last_round = True
aim_last_round = False

rifle = Weapon("rifle")
revolver = Weapon("revolver")
wep_array = (rifle, revolver)


def chance(percent=50):
    return random.randrange(100) < percent


def game_init():
    game_init.p = Player()

    if chance():
        game_init.p.weapon = rifle
    else:
        game_init.p.weapon = revolver

    print("You are at a shooting range")
