import logic

def user_response():
    user_input = input().lower()

    if user_input == "attack":
        hit = logic.chance(logic.p.chance)

        if hit:
            logic.hit_last_round = True
            logic.hit_count += 1
            print("You hit.")
        else:
            logic.hit_last_round = False
            print("You fired, but you missed. Good for you.")

    elif user_input == "take aim":
        if logic.hit_last_round and logic.p.chance != 50:
            logic.p.chance = 75

        elif not logic.hit_last_round and logic.p.chance != 25:
            logic.p.chance = 50
        #add last two or three possibiities.
        #where will chance be changed per round.
