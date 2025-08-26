# RPS.py

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Always return R for the first few moves (to gather data)
    if len(opponent_history) < 5:
        move = "R"
        player.last_move = move
        return move

    # ----------------
    # Special handling for Kris
    # Kris always plays the move that beats YOUR last move
    # ----------------
    if hasattr(player, "last_move"):  
        last_my_move = player.last_move
        # Map of what Kris will play against me
        kris_will_play = {"R": "P", "P": "S", "S": "R"}[last_my_move]
        # Beat Kris's move
        beat_map = {"R": "P", "P": "S", "S": "R"}
        move = beat_map[kris_will_play]

        # Check if opponent matches Kris pattern (always countering me)
        if opponent_history[-1] == kris_will_play:
            player.last_move = move
            return move

    # ----------------
    # Default: Markov chain strategy for others
    # ----------------
    last3 = "".join(opponent_history[-3:])
    possible = ["R", "P", "S"]
    guesses = {m: 0 for m in possible}

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
