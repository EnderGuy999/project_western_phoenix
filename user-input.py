import logic

def user_response():
    user_input = input().lower()

    if user_input == "attack":
        hit = logic.chance(logic.p.chance)
            if hit:
                # add var that tracks the amount of targets hit.