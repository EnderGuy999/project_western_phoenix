import logic

def user_response():
    user_input = input().lower()

    if user_input == "attack":
        hit = logic.chance(logic.p.chance)
        if logic.hit_last_round and logic.aim_last_round

        if hit:
            logic.hit_last_round = True
            logic.hit_count += 1
            print("You hit.")
        else:
            logic.hit_last_round = False
            print("You fired, but you missed. Good for you.")

    elif user_input == "take aim":
        #how do we get this to occur if the player HAS 50%
        if logic.hit_last_round and logic.p.chance != 75:
            logic.p.chance = 75

        elif not logic.hit_last_round and logic.p.chance != 50:
            logic.p.chance = 50
        #add last two or three possibiities.
        #where will chance be changed per round.
