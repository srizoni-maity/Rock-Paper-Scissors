import random

def play(player1, player2, num_games, verbose=False):
    p1_prev, p2_prev = "", ""
    p1_score, p2_score = 0, 0
    for i in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)
        if verbose:
            print(f"Game {i+1}: P1={p1}, P2={p2}")

        if (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_score += 1
        elif p1 == p2:
            pass  # tie
        else:
            p2_score += 1
        p1_prev, p2_prev = p1, p2

    return p1_score / num_games

# Opponent bots
def quincy(prev_play):
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(choices) % 5]

def abbey(prev_play, opp_history=[]):
    if prev_play != "":
        opp_history.append(prev_play)
    guess = "P"
    if len(opp_history) > 2:
        guess = opp_history[-2]
    return guess

def kris(prev_play):
    choices = ["R", "R", "P", "P", "S", "S"]
    return random.choice(choices)

def mrugesh(prev_play, opp_history=[]):
    if prev_play != "":
        opp_history.append(prev_play)
    guess = "R"
    if len(opp_history) > 0:
        last_ten = opp_history[-10:]
        most_common = max(set(last_ten), key=last_ten.count)
        guess = most_common
    return guess
