import logic

def help():
    print("Attack:\n This command has your character fire at the target.")
    print("Take Aim:\n This command allows your character to increase their chances of hitting the target.")
    print("Help:\n This command shows a list of commands that can be run.")
    print("Quit:\n This command exits the program.")

def user_response():
    user_input = input().lower()

    if user_input == "attack":
        hit = logic.chance(logic.game_init.p.chance)
        if logic.hit_last_round and logic.aim_last_round:
            logic.game_init.p.chance = 50

        elif not logic.hit_last_round and logic.aim_last_round:
            logic.game_init.p.chance = 25

        if hit:
            logic.hit_last_round = True
            logic.hit_count += 1
            print("You hit.")
        else:
            logic.hit_last_round = False
            print("You fired, but you missed. Good for you.")

    elif user_input == "take aim":
        logic.hit_last_round = True

        if logic.hit_last_round and logic.game_init.p.chance != 75:
            logic.game_init.p.chance = 75
        elif not logic.hit_last_round and logic.game_init.p.chance != 50:
            logic.p.chance = 50
        else:
            print("An unexpected occurrence happened in user_input, take aim. \n hit_last_round:%s p_chance: %s" % (logic.hit_last_round, logic.game_init.p.chance))
            #revisit why this happens after two take aims, later.
            return

        print("You took aim.")


    elif user_input == "help":
        help()

    elif user_input == "quit":
        print("Quiting...")
        quit()

    else:
        print("You have entered a command that isn't in this program. For a list of commands, type Help.")