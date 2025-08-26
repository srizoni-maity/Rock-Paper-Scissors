# RPS.py

def player(prev_play, opponent_history=[]):
    """
    Adaptive AI player using pattern recognition and counters.
    - Detects Kris (counters your last move).
    - Uses Markov chain prediction for others.
    - Falls back to cycling strategy.
    """

    if prev_play:
        opponent_history.append(prev_play)

    # Start with "R" a few times to gather data
    if len(opponent_history) < 5:
        move = "R"
        player.last_move = move
        return move

    # Detect if opponent behaves like Kris (counters my last move)
    if hasattr(player, "last_move"):
        last_my_move = player.last_move
        kris_will_play = {"R": "P", "P": "S", "S": "R"}[last_my_move]
        beat_map = {"R": "P", "P": "S", "S": "R"}
        move = beat_map[kris_will_play]

        if opponent_history[-1] == kris_will_play:
            player.last_move = move
            return move

    # Markov chain prediction
    last3 = "".join(opponent_history[-3:])
    guesses = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        if "".join(opponent_history[i:i+3]) == last3:
            next_move = opponent_history[i+3]
            guesses[next_move] += 1

    if all(v == 0 for v in guesses.values()):
        # Fallback simple cycle
        cycle = ["R", "P", "S"]
        move = cycle[len(opponent_history) % 3]
    else:
        prediction = max(guesses, key=guesses.get)
        counter = {"R": "P", "P": "S", "S": "R"}
        move = counter[prediction]

    player.last_move = move
    return move
