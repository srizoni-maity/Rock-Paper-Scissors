import random

def play(player1, player2, num_games=1000, verbose=False):
    """
    Runs a rock-paper-scissors match between two bots.
    
    Args:
        player1 (function): First bot function.
        player2 (function): Second bot function.
        num_games (int): Number of rounds.
        verbose (bool): If True, prints each round.

    Returns:
        float: Win ratio of player1.
    """
    p1_prev, p2_prev = "", ""
    p1_score, p2_score = 0, 0

    for i in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        if verbose:
            print(f"Round {i+1}: P1={p1}, P2={p2}")

        if (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_score += 1
        elif p1 == p2:
            pass  # tie
        else:
            p2_score += 1

        p1_prev, p2_prev = p1, p2

    return p1_score / num_games


# ---------------------------
# Opponent Bots
# ---------------------------

def quincy(prev_play, round_count=[0]):
    """Cycles through R, P, S, R, P..."""
    choices = ["R", "P", "S", "R", "P"]
    move = choices[round_count[0] % len(choices)]
    round_count[0] += 1
    return move

def abbey(prev_play, opp_history=[]):
    """Tries to predict based on 2nd-last move."""
    if prev_play:
        opp_history.append(prev_play)
    guess = "P"
    if len(opp_history) > 2:
        guess = opp_history[-2]
    return guess

def kris(prev_play):
    """Random, but skewed distribution."""
    choices = ["R", "R", "P", "P", "S", "S"]
    return random.choice(choices)

def mrugesh(prev_play, opp_history=[]):
    """Plays the opponent’s most common move in the last 10."""
    if prev_play:
        opp_history.append(prev_play)
    guess = "R"
    if opp_history:
        last_ten = opp_history[-10:]
        most_common = max(set(last_ten), key=last_ten.count)
        guess = most_common
    return guess
